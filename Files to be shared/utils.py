import json
from random import *
import string

# Password Generation function
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()"

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    generated_password = "".join(password_list)

    return generated_password

# Accessing the existing data
def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
# Saving the new data    
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Getting the entire data for the credential list logic
def get_credentials():
    return load_data()

# Saving the data and supporting multiple account for a website
def save_credentials(website, username, password):
    website = website.lower()
    username = username.lower()

    data = load_data()

    new_data = {
        'username' : username,
        'password' : password
    }

    if website in data:
        for account in data[website]:
            if account['username'] == username:
                raise ValueError("account already exists")
            
        data[website].append(new_data)
    else:
        data[website] = [new_data]

    save_data(data)

# Updating the password for an existing account
def update_credentials(website, username, new_password):
    website = website.strip().lower()
    username = username.strip().lower()

    data = load_data()

    if website in data:
        for acc in data[website]:
            if acc['username'] == username:
                acc['password'] = new_password        
        save_data(data)
        return
        
        raise ValueError("Username not found")
    else:
        raise ValueError("Website not found")
    
def delete_credentials(website, username):
    data = load_data()

    if website in data:
        data[website] = [
            acc for acc in data[website]
            if acc['username'] != username
        ]

        if not data[website]:
            del data[website]

        save_data(data)
        return
    
    raise ValueError("Website not found")