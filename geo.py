import requests

GOOGLE_MAPS_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"


def get_coordinates(api_key, search_term):
    params = {"key": api_key, "address": search_term}

    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    return [
        {
            "lat": r["geometry"]["location"]["lat"],
            "lng": r["geometry"]["location"]["lng"],
            "formatted": r["formatted_address"],
        }
        for r in res["results"]
    ]
