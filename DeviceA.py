import socket
import os

def send_audio_file(filepath, hostname, port):
    # Read the audio file as binary data
    with open(filepath, 'rb') as file:
        audio_data = file.read()
    
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the receiver (Device B)
        client_socket.connect((hostname, port))
        
        # Send the audio data
        client_socket.sendall(audio_data)
        print("Audio file sent successfully!")
        
        # Shutdown the sending side of the socket
        client_socket.shutdown(socket.SHUT_WR)
        
        # Receive the text from Device B
        received_data = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            received_data += data
        
        audio_text = received_data.decode()
        print("Received text from Device B:", audio_text)
        
    except ConnectionRefusedError:
        print("Connection refused. Please ensure the receiver is running and accessible.")
    except socket.timeout:
        print("Socket timeout. The receiver may have closed the connection unexpectedly.")
    except socket.error as e:
        print("Socket error occurred:", str(e))
    except Exception as e:
        print("An error occurred:", str(e))
        
    finally:
        # Close the socket
        client_socket.close()

# Example usage
audio_file = '/Users/family/Downloads/male.wav'
hostname = '192.168.0.157'
port = 12345

send_audio_file(audio_file, hostname, port)
