import requests
from PIL import Image
from io import BytesIO
import os

def download_image(url, folder_path, image_name):
    try:
        response = requests.get(url)
        print(f"Requesting image from {url}")
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            if image.format in ['JPEG', 'JPG', 'PNG']:
                image = image.convert('RGB')
                image.save(os.path.join(folder_path, image_name), 'JPEG')
                print(f"Saved image as {os.path.join(folder_path, image_name)}")
                return True
            else:
                print(f"Unsupported image format: {image.format}")
        else:
            print(f"Failed to download image, HTTP status code: {response.status_code}")
        return False
    except Exception as e:
        print(f"Could not download {url} - {e}")
        return False