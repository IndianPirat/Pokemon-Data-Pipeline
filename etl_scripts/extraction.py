import requests

pokemon_data = []
def get_data():
    for poke_num in range(1, 2):
        try:
            BASE_URL = f"https://pokeapi.co/api/v2/pokemon/{poke_num}"
            response = requests.get(BASE_URL)
            response.raise_for_status()
            data = response.json()
            pokemon_data.append(data)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error!Statuscode:{e}")
        except ValueError as e:
            print("JSON decoding error!")
        except Exception as e:
            print(f"Error:{e}")

get_data()

