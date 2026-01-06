#this is a password maneger program . our aim was to create a simple password manager that can store and retrieve passwords for different accounts
from cryptography.fernet import Fernet

master_pwd = input("Enter master password: ")
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key","rb") as key_file:
        key = key_file.read()
    return key

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print("Account:", user, "| Password:", pwd)

def add():
    name = input('Account Name: ')
    pwd = input("password: ")
    with open('password.txt','a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
  mode = input ("do you want to add a new password or view existing ones (view, add)? or q to quit")
  if mode == "view":
    view()
  elif  mode == "add":
    add()
  elif mode == "q":
    print("quitting...")
    quit()
  else:
    print("invalid input")
    
    
