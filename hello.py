import socket
import whisper

def receive_audio_file(port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = None  # Initialize the connection variable
    
    try:
        # Bind the socket to a specific address and port
        server_socket.bind(('10.20.200.177', port))
        
        # Listen for incoming connections
        server_socket.listen(1)
        print("Waiting for incoming audio file...")
        
        # Accept the connection from Device 1
        connection, address = server_socket.accept()
        
        # Receive the audio data
        audio_data = connection.recv(1024)
        
        # Save the received audio data as a file
        received_file = 'received_audio.wav'
        with open(received_file, 'wb') as file:
            file.write(audio_data)
        
        print("Audio file received successfully!")
        
        # Perform audio-to-text conversion
        model = whisper.load_model("base")
        result = model.transcribe("received_audio.wav")
        
        # Send the text back to Device 1
        connection.sendall(result["text"].encode())
        print("Text sent back to Device 1:", result["text"])
        
    except Exception as e:
        print("An error occurred:", str(e))
        
    finally:
        # Close the connection and socket
        if connection:
            connection.close()
        server_socket.close()

# Example usage
port = 12345

receive_audio_file(port)