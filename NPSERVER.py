import socket
import threading
import tkinter as tk
import asyncio
import google.generativeai as genai  

# Configure the API key globally
genai.configure(api_key="AIzaSyCn2cEOZ625Gt6reE-mfqUDFceWskk0qe8")

class ServerWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Server Output")

        # Create a Text widget to display server output
        self.server_output_text = tk.Text(self.master, height=10, width=80)
        self.server_output_text.pack()

        # Create a socket object
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to a specific address and port
        server_address = ('localhost', 12345)
        self.server_socket.bind(server_address)

        # Listen for incoming connections
        self.server_socket.listen(5)
        self.server_output_text.insert(tk.END, "Server is listening for connections...\n")

        # Start a thread to accept and handle clients
        threading.Thread(target=self.accept_clients).start()

    def accept_clients(self):
        while True:
            # Accept a connection from a client
            client_socket, client_address = self.server_socket.accept()

            # Print the accepted connection in the server output
            self.server_output_text.insert(tk.END, f"Accepted connection from {client_address}\n")
            self.server_output_text.yview(tk.END)

            # Create a new thread to handle the client
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

    def handle_client(self, client_socket, client_address):
        while True:
            try:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break

                # Print the received message in the server output
                received_message = f"Received from {client_address}: {data.decode()}\n"
                self.server_output_text.insert(tk.END, received_message)
                self.server_output_text.yview(tk.END)

                # Send the message to Gemini API using asyncio.run
                gemini_response = asyncio.run(self.get_gemini_response(data.decode()))

                # Print the Gemini response in the server output
                response_message = f"Gemini response to {client_address}: {gemini_response}\n"
                self.server_output_text.insert(tk.END, response_message)
                self.server_output_text.yview(tk.END)

                # Send the Gemini response back to the client
                client_socket.sendall(gemini_response.encode())

            except socket.error:
                # Handle socket errors, e.g., when the client disconnects
                self.server_output_text.insert(tk.END, f"Connection from {client_address} closed.\n")
                self.server_output_text.yview(tk.END)
                client_socket.close()
                break

    async def get_gemini_response(self, message):
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]

        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            safety_settings=safety_settings,
            generation_config=generation_config,
        )

        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [message],
                },
            ]
        )

        response = chat_session.send_message(message)
        return response.text.strip().lower()

if __name__ == "__main__":
    root = tk.Tk()
    server_window = ServerWindow(root)
    root.mainloop()
