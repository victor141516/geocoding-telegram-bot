import requests

GOOGLE_PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"


def get_coordinates(api_key, search_term):
    params = {
        "key": api_key,
        "input": search_term,
        "inputtype": "textquery",
        "fields": "formatted_address,name,geometry"
    }

    req = requests.get(GOOGLE_PLACES_API_URL, params=params)
    res = req.json()

    return [
        {
            "lat": r["geometry"]["location"]["lat"],
            "lng": r["geometry"]["location"]["lng"],
            "formatted": r["formatted_address"],
            "name": r["name"]
        }
        for r in res.get("candidates", [])
    ]


get_coordinates('AIzaSyBlXa42g68EQPwVha_7NqvcMzXiqZBvH9g', 'plenilunio')
