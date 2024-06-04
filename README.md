# Image Scraper

Used to collect images for my image classifier. Collects images from Google image search results.

## Requirements

Install Chromedriver from the official Chromedriver website, matching your version of Chrome (Chrome MUST be installed).

## How To Run

1. Clone the repo
2. Install the dependencies `pip install -r requirements.txt`
3. Create a folder "images" at the root of this repo
4. Change line 19 to the appropriate filepath leading to your installed Chromedriver executable in `scrape_images.py`
5. Run the main file, enter the search term you want

## Functionality

Creates a folder in the images folder matching the user input search term, and scrapes images in JPG format. Adds it to the folder with filename-###.jpg.

Example, image I search for is "apple"
Creates a folder "apple", and adds images as apple-000.jpg, apple-001.jpg, and so on.