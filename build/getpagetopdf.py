# a simple script to get a screenshot of a webpage and save it to a pdf file
# The pdfkit module is a third-party library that is not part of the Python standard library.
# You can install the pdfkit module using pip, the Python package manager.
# pip install pdfkit

import os
import sys
import time
import tempfile
from selenium import webdriver
import img2pdf

def generate_webpage_pdf(url, filename):
    # Create the folder if it doesn't exist
    if not os.path.exists('webpdf'):
        os.makedirs('webpdf')

    # Specify the full path to the webpdf folder as the destination for the PDF file
    filepath = os.path.join('webpdf', filename)

    # Start a headless Chrome browser
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # Load the webpage
    driver.get(url)

    # Wait for the webpage to fully load
    time.sleep(10)

    # Save a screenshot of the webpage to a temporary file
    with tempfile.NamedTemporaryFile(mode='w+b', suffix='.png', delete=False) as f:
        driver.save_screenshot(f.name)
        f.seek(0)
        # Convert the screenshot to a PDF file
        pdf_bytes = img2pdf.convert(f.name)

    # Save the PDF file to the specified filepath
    with open(filepath, 'wb') as f:
        f.write(pdf_bytes)
    

    # Close the browser
    driver.quit()

# Get the URL and filename from the command-line arguments
if len(sys.argv) == 3:
    url = sys.argv[1]
    filename = sys.argv[2]
elif len(sys.argv) == 2:
    url = sys.argv[1]
    filename = input("Enter the filename for the PDF: ")
else:
    url = input("Enter the URL of the webpage: ")
    filename = input("Enter the filename for the PDF: ")

generate_webpage_pdf(url, filename)
