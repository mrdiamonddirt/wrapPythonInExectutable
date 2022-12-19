# Description: This script prompts the user to enter a postcode, year and month, 
# then retrieves the number of crimes that occurred in that area during that month.

import requests

# Prompt the user to enter a postcode and year/month
while True:
    postcode = input("Enter a postcode: ")
    year = input("Enter the year (YYYY): ")
    month = input("Enter the month (MM): ")
    
    # Validate the postcode input
    postcodes_url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(postcodes_url)
    if response.status_code != 200:
        print("Error: Invalid postcode")
        continue
    
    # Validate the year input
    if not year.isdigit() or len(year) != 4:
        print("Error: Invalid year")
        continue
    
    # Validate the month input
    if not month.isdigit() or int(month) < 1 or int(month) > 12:
        print("Error: Invalid month")
        continue
    
    # If all input is valid, break out of the loop
    break

# Retrieve the latitude and longitude from the postcodes.io API response
data = response.json()
latitude = data["result"]["latitude"]
longitude = data["result"]["longitude"]

# Send a request to the UK police API to retrieve crime data for the given coordinates and date
police_url = f"https://data.police.uk/api/crimes-street/all-crime?lat={latitude}&lng={longitude}&date={year}-{month}"
response = requests.get(police_url)

# Check the status code to ensure the request was successful
if response.status_code != 200:
    print("Error: Could not retrieve crime data")
else:
    # Retrieve the number of crimes from the response
    data = response.json()
    num_crimes = len(data)
    
    # Print the number of crimes
    print(f"Number of crimes in {month}/{year}: {num_crimes}")
