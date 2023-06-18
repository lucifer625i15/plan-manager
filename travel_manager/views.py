import requests
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

from .models import Location

def live_location(request):
    latest_location = Location.objects.latest('timestamp')  # Assuming you have a timestamp field in Location model
    context = {'latest_location': latest_location}
    return render(request, 'live_location.html', context)

def find_hotels(request):
    # Define the coordinates that represent the path
    # Replace these coordinates with your own path coordinates
    path_coordinates = [
        (latitude1, longitude1),
        (latitude2, longitude2),
        # Add more coordinates as needed
    ]
    
    # Prepare the Overpass API query
    query = f'[out:json];(node["tourism"="hotel"]({",".join([f"{lat},{lon}" for lat, lon in path_coordinates])}););out;'

    # Send the API request to Overpass API
    response = requests.get(f'https://api.opentripmap.com/0.1/en/amenity/by_bbox?bbox={min(lon for lat, lon in path_coordinates)},{min(lat for lat, lon in path_coordinates)},{max(lon for lat, lon in path_coordinates)},{max(lat for lat, lon in path_coordinates)}&kinds=hotels&format=json')

    if response.status_code == 200:
        # Parse the API response and extract hotel information
        hotels = []
        data = response.json()
        for feature in data['features']:
            properties = feature['properties']
            name = properties['name']
            address = properties['address']
            rating = properties['rate']
            hotels.append({
                'name': name,
                'address': address,
                'rating': rating
            })

        # Pass the hotel data to the template
        context = {'hotels': hotels}
        return render(request, 'hotel_list.html', context)
    else:
        # Handle API request error
        error_message = f"Error occurred while retrieving hotels: {response.status_code}"
        return render(request, 'error.html', {'error_message': error_message})
