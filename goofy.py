import requests
import json

URL = "https://sussyworkshop.pythonanywhere.com/"

def _SimpleGET(endpoint) ->dict:
    url = URL + endpoint
    response = requests.request("GET", url, headers={"method":"command"})
    responseDict = json.loads(response.text)
    if responseDict["error"] != "none":
        raise Exception(responseDict["error"])
    else:
        return responseDict

# Get quote from bbc
def Quote():
    result = _SimpleGET("/quote")
    return [result["author"], result["quote"]]

# Get a random fake IP address
def ip():
    result = _SimpleGET("/ip")
    return result["ip"]

# Get a random password
def password(characters: int = 12):
    result = _SimpleGET(f"/password?length={int(characters)}")
    return result["password"]
