import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def process_file(path):
    async with aiofiles.open(path, mode='r') as f:
        contents = await f.read()

    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]

    output_path = Path(pokemonmove_directory) / f'{name}_moves.txt'
    
    async with aiofiles.open(output_path, mode='w') as f:
        await f.write('\n'.join(moves))

async def main():
    # Create a Path object and glob for JSON files.
    pathlist = Path(pokemonapi_directory).glob('*.json')

    # Iterate through all JSON files in the directory.
    tasks = [process_file(path) for path in pathlist]
    await asyncio.gather(*tasks)

asyncio.run(main())
