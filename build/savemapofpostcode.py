import folium
import requests
import os

# Function to get the latitude and longitude of a postcode
def get_lat_long_from_postcode(postcode):
    # Send a request to the postcodes.io API to retrieve the latitude and longitude of the postcode
    postcodes_url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(postcodes_url)

    print(response.status_code)
    # Check the status code to ensure the request was successful
    if response.status_code == 200:
        # Retrieve the latitude and longitude from the response
        data = response.json()
        latitude = data["result"]["latitude"]
        longitude = data["result"]["longitude"]

        # Return the latitude and longitude as a tuple
        return (latitude, longitude)
    else:
        # If the request was not successful, return None
        return None

# Get the postcode from the user
postcode = input('Enter a postcode: ')

# Get the latitude and longitude of the postcode
lat_long = get_lat_long_from_postcode(postcode)

# Check if the function returned a valid latitude and longitude
if lat_long is not None:
    # takes a postcode and returns a map of that are and saves it to a file
    
    # If the function returned a valid latitude and longitude, create a folium map object centered on that location
    map = folium.Map(location=lat_long, zoom_start=12)
    print('Map created')
    # Display the map
    map

    # Create the "map" folder if it doesn't exist
    if not os.path.exists('map'):
        os.makedirs('map')

    # Save the map to an HTML file
    map.save('map/map.html')

    # Open the HTML file in the default web browser
    import webbrowser
    webbrowser.open('map/map.html')

    
else:
    # If the function returned None, print an error message
    print('Invalid postcode')
