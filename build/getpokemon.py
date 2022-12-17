# a script to get information about a Pokemon from the PokeAPI

import requests
import json

# Prompt the user for the Pokemon ID
pokemon_id = input("Enter the Pokemon ID: ")

# Construct the endpoint URL with the Pokemon ID
endpoint = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

# Send a GET request to the endpoint
response = requests.get(endpoint)

# Parse the response as JSON
data = response.json()

# Print the name, ID, type, and artwork URL of the Pokemon
print("Name:", data['name'])
print("ID:", data['id'])
print("Type:", data['types'][0]['type']['name'])
print("Artwork URL:", data['sprites']['front_default'])
