import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from create_folder import create_folder
from download_image import download_image

def scrape_images(pokemon_name, num_images):
    folder_path = create_folder(pokemon_name)

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    service = Service('C:/Users/Your/Path/To/chromedriver-win64/chromedriver.exe')  # Edit this to match your path to Chromedriver.
    driver = webdriver.Chrome(service = service, options = chrome_options)
    driver.get(f"https://www.google.com/search?tbm=isch&q={pokemon_name}")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img.YQ4gaf')))

    image_count = 0
    scroll_attempts = 0
    max_scroll_attempts = 10
    while image_count < num_images and scroll_attempts < max_scroll_attempts:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)
        images = driver.find_elements(By.CSS_SELECTOR, 'img.YQ4gaf')
        image_count = len(images)
        print(f"Found {image_count} images after {scroll_attempts + 1} scrolls.")
        scroll_attempts += 1

    if image_count == 0:
        print("No images found.")
        driver.quit()
        return

    print(f"Total images found: {image_count}")

    downloaded_images = 0
    for index, img in enumerate(images):
        if downloaded_images >= num_images:
            break
        try:
            img_url = img.get_attribute('src')
            print(f"Image {index} URL: {img_url}")
            if img_url and img_url.startswith('http'):
                image_name = f"{pokemon_name}-{downloaded_images:03}.jpg"
                if download_image(img_url, folder_path, image_name):
                    downloaded_images += 1
                    print(f"Downloaded image {downloaded_images}/{num_images}")
                else:
                    print(f"Failed to download image from {img_url}")
            else:
                print(f"No valid URL found for image {index}")
        except Exception as e:
            print(f"Error downloading image {index}: {e}")