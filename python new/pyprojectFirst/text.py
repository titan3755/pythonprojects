import cryptography
from cryptography.fernet import Fernet
from tkinter import *

file = open('key.key', 'rb')
key = file.read()
file.close()

encrypted = ''

root = Tk()
root.title('Encryption')
root.geometry('1280x720')
root.resizable(False, False)
root.config(bg='white')

def on_click():
    msg = entry_box.get()
    encoded = msg.encode()

    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    true_msg_encrypted = encrypted.decode()
    output_box.insert(0, true_msg_encrypted)

def on_decrypt_click():
    msg = entry_box.get()
    encoded = msg.encode()

    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    true_msg_decrypted = decrypted.decode()
    output_box.insert(0, true_msg_decrypted)

main_title = Label(root)
entry_title = Label(root)
entry_box = Entry(root)
output_title = Label(root)
output_box = Entry(root)
encrypt_button = Button(root)
decrypt_button = Button(root)

main_title.config(text='Encrypt and Decrypt text', fg='darkred', bg='lightgray', font=('Helvetica', 28, 'italic'), padx=3000, pady=10, border=8)
entry_title.config(text='Entry Text', fg='black', bg='white', padx=12, pady=10, border=8, font=('Helvetica', 18, 'bold'))
entry_box.config(bg='lightgreen', fg='black', font=('Roboto', 16, 'italic'), width=30)
output_title.config(text='Encrypted Text', fg='black', bg='white', padx=20, pady=10, border=8, font=('Helvetica', 18, 'bold'), height=2)
output_box.config(bg='lightgreen', fg='black', font=('Roboto', 16, 'italic'), width=45)
encrypt_button.config(text='Encrypt', font=('Helvetica', 16, 'bold'), padx=12, pady=10, border=8, bg='darkorange', command=on_click)
decrypt_button.config(text='Decrypt', font=('Helvetica', 16, 'bold'), padx=12, pady=10, border=8, bg='darkorange', command=on_decrypt_click)

main_title.pack(anchor=CENTER)
entry_title.place(x=10, y=200)
entry_box.place(x=260, y=215)
output_title.place(x=10, y=300)
output_box.place(x=366, y=337)
encrypt_button.place(x=450, y=600)
decrypt_button.place(x=650, y=600)

root.mainloop()