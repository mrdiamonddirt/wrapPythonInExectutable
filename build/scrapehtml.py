# simple scraper using requests
# The requests module is a third-party library that is not part of the Python standard library. 
# You can install the requests module using pip, the Python package manager.
# pip install requests


import requests

def scrape_html(url):
    """Scrape the HTML data from the given URL and return it as a string."""
    response = requests.get(url)
    return response.text

def save_html(html, filename):
    """Save the HTML data to a file with the given filename."""
    with open(filename, 'w') as f:
        f.write(html)

# Scrape the HTML data from a URL
url = 'http://www.google.com'
html = scrape_html(url)

# Save the HTML data to a file
save_html(html, 'google.html')
