# from storage.json_storage import load_data, save_data
from storage.db import get_connection
import sqlite3
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("SECRET_KEY")
if not KEY:
    raise ValueError("SECRET_KEY not set in environment")

cipher = Fernet(KEY.encode())


def encrypt_pwd(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_pwd(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def get_credentials():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT website, username, password FROM credentials")
    rows = cursor.fetchall()

    conn.close()

    data = {}

    for website, username, password in rows:
        if website not in data:
            data[website] = []

        try:
            decrypted_pasword = decrypt_pwd(password)
        except Exception:
            decrypted_pasword = "[DECRYPTION FAILED]"

        data[website].append({
            "username":username,
            "password":decrypted_pasword
        })

    return data
    # JSON data loading
    # return load_data()

# Saving the data and supporting multiple account for a website
def save_credentials(website, username, password):
    website = website.lower()
    username = username.lower()

    conn = get_connection()
    cursor = conn.cursor()

    encrypted_password = encrypt_pwd(password)

    try:
        cursor.execute("""INSERT INTO credentials (website, username, password) VALUES (?, ?, ?)""", (website, username, encrypted_password))
    except sqlite3.IntegrityError:
        raise ValueError("Account already exists!")


    conn.commit()
    conn.close()


    # JSON DATASET
    # data = load_data()

    # new_data = {
    #     'username' : username,
    #     'password' : password
    # }

    # if website in data:
    #     for account in data[website]:
    #         if account['username'] == username:
    #             raise ValueError("account already exists")
            
    #     data[website].append(new_data)
    # else:
    #     data[website] = [new_data]

    # save_data(data)

# Updating the password for an existing account
def update_credentials(website, username, new_password):
    website = website.strip().lower()
    username = username.strip().lower()

    conn = get_connection()
    cursor = conn.cursor()

    encrypted_password = encrypt_pwd(new_password)

    cursor.execute("""UPDATE credentials SET password = ? WHERE website = ? AND username = ?""", (encrypted_password, website, username))
    
    if cursor.rowcount == 0:
        raise ValueError("Credential not found")
    
    conn.commit()
    conn.close()

    # JSON data updation
    # for website, username, new_password in rows:
    #     if website not in data:
    #         data[website] = []

    #     data[website].append({
    #         "username":username,
    #         "password":new_password
    #     })    

    # data = load_data()

    # if website in data:
    #     for acc in data[website]:
    #         if acc['username'] == username:
    #             acc['password'] = new_password        
    #     save_data(data)
    #     return
        
    #     raise ValueError("Username not found")
    # else:
    #     raise ValueError("Website not found")
    
def delete_credentials(website, username):
    website = website.strip().lower()
    username = username.strip().lower()

    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM credentials WHERE website = ? AND username = ?""", (website, username))
    
    if cursor.rowcount == 0:
        raise ValueError("Credential not found")

    conn.commit()
    conn.close()

    # JSON data deletion
    # data = load_data()

    # if website in data:
    #     data[website] = [
    #         acc for acc in data[website]
    #         if acc['username'] != username
    #     ]

    #     if not data[website]:
    #         del data[website]

    #     save_data(data)
    #     return
    
    # raise ValueError("Website not found")

def search_credentials(website):
    website = website.strip().lower()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT website, username, password FROM credentials WHERE website = ?""", (website,))

    rows = cursor.fetchall()

    conn.close()

    data = {}

    for website, username, password in rows:
        try:
            decrypted_password = decrypt_pwd(password)
        except Exception:
            decrypted_password = "[DECRYPTION FAILED]"    

        if website not in data:
            data[website] = []
        
        data[website].append({
            "username" : username,
            "password" : decrypted_password
        })
    return data
