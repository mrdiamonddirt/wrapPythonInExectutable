# a script to see if a website has a form and return information about it

import requests
from bs4 import BeautifulSoup

url = input('Enter a url: ')
# Send an HTTP request to the website
response = requests.get(f"https://{url}".format(url=url))

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the form elements on the page
    forms = soup.find_all("form")

    # Print the details of each form
    for form in forms:
        print("Form action:", form["action"])
        method = form.get("method")  # Get the value of the method attribute, if it is set
        if method:
            print("Form method:", method)
        else:
            print("Form method: not set")
        print("Form inputs:")
        for input in form.find_all("input"):
            input_type = input.get("type")  # Get the value of the type attribute, if it is set
            input_name = input.get("name")  # Get the value of the name attribute, if it is set
            input_value = input.get("value")  # Get the value of the value attribute, if it is set
            if input_type and input_name and input_value:
                print(" -", input_name, input_type, ":", input_value)
            else:
                print(" - input missing attributes")
else:
    print("Failed to retrieve webpage")
