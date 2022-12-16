# a simple script to get a screenshot of a webpage and save it to a pdf file
# The pdfkit module is a third-party library that is not part of the Python standard library.
# You can install the pdfkit module using pip, the Python package manager.
# pip install pdfkit

import webbrowser
import pdfkit

url = 'https://www.google.com'
filename = 'google.pdf'


# Load the webpage in the default web browser
webbrowser.open(url)

# Wait for the webpage to load
input("Press Enter when the webpage is fully loaded...")

# Save a print of the webpage to a PDF file
pdfkit.from_url(url, filename, configuration=pdfkit.configuration(wkhtmltopdf='wkhtmltox/bin/wkhtmltopdf.exe'))


