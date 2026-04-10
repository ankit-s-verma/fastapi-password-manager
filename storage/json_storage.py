# import json

# # Accessing the existing data
# def load_data():
#     try:
#         with open('data.json', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}
    
# # Saving the new data    
# def save_data(data):
#     with open('data.json', 'w') as file:
#         json.dump(data, file, indent=4)

from cryptography.fernet import Fernet
print(Fernet.generate_key())