import requests
import json

URL = "https://sussyworkshop.pythonanywhere.com/"

def _SimpleGET(endpoint):
    url = URL + endpoint
    response = requests.request("GET", url)
    return json.loads(response.text)

# Get quote from bbc
def Quote():
    result = _SimpleGET("/quote")
    return [result["author"], result["quote"]]

# Get a random fake IP address
def ip():
    result = _SimpleGET("/ip")
    return result["ip"]
