# Description: Downloads all images from a webpage and saves them to a directory

import requests
import os
from bs4 import BeautifulSoup

def get_images(url):
    # Make a request to the specified URL
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return []

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags in the HTML
    images = soup.find_all('img')

    # Return a list of image URLs
    image_urls = []
    for image in images:
        src = image['src']
        if src.startswith('http'):
            # Absolute URL
            image_urls.append(src)
        else:
            # Relative URL
            image_urls.append(f'{url}{src}')
    return image_urls


def save_images(image_urls, directory):
    # Create the specified directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Iterate over the list of image URLs
    for url in image_urls:
        # Get the file name of the image
        file_name = url.split('/')[-1]

        # Download the image and save it to the specified directory
        try:
            response = requests.get(url)
            open(f'{directory}/{file_name}', 'wb').write(response.content)
        except requests.exceptions.RequestException as e:
            print(f'Error downloading {url}: {e}')


# Example usage:

url = 'https://www.google.com/'
image_urls = get_images(url)
save_images(image_urls, 'images')
