from scrape_images import scrape_images

def main():
    pokemon_name = input("Enter the name of the Pokémon to scrape images for: ").lower()
    num_images = int(input("Enter the number of images to scrape: "))
    scrape_images(pokemon_name, num_images)

if __name__ == "__main__":
    main()