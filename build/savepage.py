# Description: Extracts HTML, CSS, and JavaScript elements from a webpage and saves them to files

import os
import requests
from bs4 import BeautifulSoup


# Make a request to the webpage
input_url = input('Enter a url: ')
url = f'https://{input_url}'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the HTML, CSS, and JavaScript elements
html = soup.prettify()
css = soup.find_all('style')
javascript = soup.find_all('script')

# Create a folder for the extracted elements
folder_name = url.split('/')[-1]
os.makedirs(folder_name, exist_ok=True)

# Save the extracted elements to files
with open(f'{folder_name}/index.html', 'w') as f:
    f.write(html)

for i, style in enumerate(css):
    with open(f'{folder_name}/style{i}.css', 'w') as f:
        f.write(style.text)

for i, script in enumerate(javascript):
    with open(f'{folder_name}/script{i}.js', 'w') as f:
        f.write(script.text)
