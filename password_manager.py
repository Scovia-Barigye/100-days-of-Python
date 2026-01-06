#this is a password maneger program . our aim was to create a simple password manager that can store and retrieve passwords for different accounts
from cryptography.fernet import Fernet
import os

# Only call write_key() if key.key does not exist
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Check if key.key exists, if not, generate it
if not os.path.exists("key.key"):
    write_key()

# Load the key and initialize Fernet
key = load_key()
fer = Fernet(key)  # <-- Fernet instance for encryption/decryption

def view():
    # Decrypt the password using fer.decrypt() before printing
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, enc_pwd = data.split("|")
            # Decrypt the password (stored as bytes string)
            try:
                decrypted_pwd = fer.decrypt(enc_pwd.encode()).decode()
            except Exception as e:
                decrypted_pwd = "<decryption failed>"
            print("Account:", user, "| Password:", decrypted_pwd)

def add():
    name = input('Account Name: ')
    pwd = input("password: ")
    # Encrypt the password using fer.encrypt() before writing
    enc_pwd = fer.encrypt(pwd.encode()).decode()  # Store as string
    with open('password.txt', 'a') as f:
        f.write(name + "|" + enc_pwd + "\n")

while True:
    mode = input("do you want to add a new password or view existing ones (view, add)? or q to quit")
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        print("quitting...")
        quit()
    else:
        print("invalid input")


