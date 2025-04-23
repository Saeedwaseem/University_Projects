import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Client")

        # Create a frame for the messages and scrollbar
        self.messages_frame = tk.Frame(self.master)
        self.messages_frame.pack(pady=10)

        # Create a Text widget with a scrollbar to display messages
        self.messages_text = scrolledtext.ScrolledText(self.messages_frame, wrap=tk.WORD, height=20, width=80)
        self.messages_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Disable the Text widget for direct user editing
        self.messages_text.config(state=tk.DISABLED)

        # Create a frame for the entry and send button
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(pady=10)

        # Create an Entry widget for user input
        self.entry = tk.Entry(self.input_frame, width=60)
        self.entry.grid(row=0, column=0, padx=10)

        # Create a Send button to send messages
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message, width=10)
        self.send_button.grid(row=0, column=1)

        # Bind the Enter key to the send_message function
        self.entry.bind("<Return>", lambda event: self.send_message())

        # Create a socket object
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        server_address = ('localhost', 12345)
        self.client_socket.connect(server_address)
        print("Connected to the server.")

        # Start a thread to receive messages from the server
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

    def send_message(self):
        # Send a message to the server
        message = self.entry.get()
        if message:  # Ensure the message is not empty
            self.client_socket.sendall(message.encode())

            # Display the sent message in the Text widget
            self.display_message(f"Client: {message}\n")

            # Clear the entry field
            self.entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                # Receive data from the server
                data = self.client_socket.recv(1024)
                if not data:
                    break

                # Display the received message in the Text widget
                self.display_message(f"Server: {data.decode()}\n")
            except socket.error:
                # Handle socket errors, e.g., when the server is closed
                self.display_message("Server connection closed.\n")
                self.client_socket.close()
                break

    def display_message(self, message):
        # Enable the Text widget to insert the message
        self.messages_text.config(state=tk.NORMAL)
        self.messages_text.insert(tk.END, message)
        self.messages_text.yview(tk.END)
        # Disable the Text widget after inserting the message
        self.messages_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    client_app = ChatClient(root)
    root.mainloop()
