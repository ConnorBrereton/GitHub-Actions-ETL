import os
import requests
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Set API keys and contract name
API_KEY=os.getenv('API_KEY')
CONTRACT=os.getenv('CONTRACT_NAME')

response = requests.get(f'https://api.jcdecaux.com/vls/v1/stations?contract={CONTRACT}&apiKey={API_KEY}')
with open('data.json', 'w') as f:
    f.write(response.text)