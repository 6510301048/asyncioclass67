from flask import Flask, render_template
import asyncio
import httpx
import time
import random
from pypokemon.pokemon import Pokemon


app = Flask(__name__)

async def get_pokemon(client, url):
    print(f"{time.ctime()} - get {url}")
    resp =await client.get(url)
    pokemon = resp.json()

    return pokemon

async def get_pokemons():
        rand_list=[]
        pokemon_data = []
        async with httpx.AsyncClient() as client:
            for i in range(5):
                rand_list.append(random.randint(1,151))
            for number in rand_list:
                pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
                pokemon_json = await get_pokemon(client, pokemon_url)
                pokemon_object = Pokemon(pokemon_json)
                pokemon_data.append(pokemon_object)
            return pokemon_data

@app.route('/')
async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")
    return render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)


if __name__ == '__main__':
    app.run(debug=True, port=50001)