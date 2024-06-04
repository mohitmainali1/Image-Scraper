import os

def create_folder(pokemon_name):
    base_dir = os.path.join(os.getcwd(), 'images', pokemon_name)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    return base_dir