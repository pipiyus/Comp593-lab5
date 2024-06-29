'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
from urllib import response
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    headers = {"Accept": "text/plain"}

    print("Getting pokemon info...", end="")
    resp = requests.get(POKE_API_URL, headers=headers)

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if response.status_code == requests.codes.ok:
        print(" Success!")
    return resp.text

    # TODO: If the GET request failed, print the error reason and return None

    return

if __name__ == '__main__':
    main()