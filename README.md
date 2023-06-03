# Ransomware

The ransomware will utilize encryption techniques and a client-server architecture to enable data exchange between the attacker and the victim.

## Overview
The main goal of this project is to create a malware that performs the following tasks:

Generate a random 128-bit key (16 characters) using ASCII characters.
Locate all .txt files on the victim's computer and encrypt their contents.
Send the generated key back to the server.
Infect other systems by sending the compiled malware to a list of email addresses.

## To run the ransomware, follow these steps:

Open two separate terminals or command prompt windows.

In the first terminal, navigate to the project directory and execute the server.py file using the following command:

Copy code
python server.py
In the second terminal, navigate to the project directory and execute the client.py file using the following command:

Copy code
python client.py
The client program will initiate the encryption process on the victim's computer. You will see a prompt indicating that the encryption is in progress.

Once the encryption is completed, the prompt will wait for a decryption key input. Enter the word "code" (without quotes) as the decryption key and press Enter.

The ransomware will decrypt all the encrypted files using the provided decryption key.

Please note that running this ransomware on your computer can result in the encryption of your files. It is strongly advised to only run it in a controlled virtual machine environment or on systems where you have appropriate permissions and backups in place.
