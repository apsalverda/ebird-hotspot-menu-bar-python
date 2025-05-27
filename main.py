import requests
import json
import keyring
import re
import getpass
from datetime import datetime

# REQUIREMENTS:
# Your ebird API key needs to be stored in your macOS keychain, in a password item called "ebird-api-key"
# You can obtain your personal API key at:
# https://ebird.org/api/keygen

# You can set your own location:
# 1. Navigate to the ebird webpage for your location
# 2. Retrieve the location code from the URL
#    For instance, the Brickyard Trail ebird webpage can be found at
#    https://ebird.org/hotspot/L4686222
# 3. Set EBIRD_LOCATION to the location code (e.g. "L4686222")
# 4. Set EBIRD_LOCATION_NAME to the name of your location

EBIRD_LOCATION = "L4686222"
EBIRD_LOCATION_NAME = "Brickyard Trail"

def get_ebird_observations(location_id, api_token):
    url = f"https://api.ebird.org/v2/data/obs/{location_id}/recent"
    headers = {
        "X-eBirdApiToken": api_token
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
    return None

def main():
    user_name = getpass.getuser()
    api_key = keyring.get_password(service_name = "ebird-api-key", username = user_name)
    if api_key is not None:
        observations = get_ebird_observations(EBIRD_LOCATION, api_key)
        today = datetime.now().strftime("%Y-%m-%d")
        birds_today = []
        birds_earlier = []
        for item in observations:
            bird = item["obsDt"] + " " + item["comName"]
            if item["obsDt"].startswith(today):
                # remove date from timestamp for today's observations
                bird = bird.removeprefix(str(today) + " ")
                birds_today.append(bird)
            else:
                # remove time of day from timestamp for earlier observations
                bird = re.sub(r'^\d{4}-(\d{2}-\d{2}) \d{2}:\d{2} ', r'\1 ', bird)
                birds_earlier.append(bird)
        print(f"{EBIRD_LOCATION_NAME} ({len(birds_today) + len(birds_earlier)} species)")
        print(f"[{len(birds_today)} TODAY]")
        for bird in birds_today:
            print(bird)
        print(f"[{len(birds_earlier)} EARLIER]")
        for bird in birds_earlier:
            print(bird)
    else:
        print("Unable to find \"ebird-api-key\" in keychain.")
        print("To resolve this issue:")
        print("1. Open app Keychain Access")
        print("2. Create password item \"ebird-api-key\"")
        print("3. Store your ebird API key in this item")
        print("Obtain your eBird API key at:")
        print("https://ebird.org/api/keygen")

if __name__ == "__main__":
    main()