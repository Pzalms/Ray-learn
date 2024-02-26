# File name: model_client.py
import requests

english_text = "HI Ebuka !"

response = requests.post("http://127.0.0.1:8000/", json=english_text)
french_text = response.text

print(french_text)