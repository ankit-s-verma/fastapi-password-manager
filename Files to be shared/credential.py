from storage.json_storage import load_data, save_data
from storage.db import get_connection

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

        data[website].append({
            "username":username,
            "password":password
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

    cursor.execute("""
        INSERT INTO credentials (website, username, password) VALUES (?, ?, ?)""", (website, username, password))

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

    cursor.execute("""
        UPDATE credentials SET password = ? WHERE website = ? AND username = ?""", (new_password, website, username))
    
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

    cursor.execute("""
                   DELETE FROM credentials WHERE website = ? AND username = ?""", (website, username))
    
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