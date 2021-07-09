import urllib.parse
import requests

main_api = "https://api.nasa.gov/planetary/apod?"
start_date = "2021-01-01"
end_date = "2021-05-31"
api_key = "wgckoSMSI20knZdg0DCVLXcwOecXOV9YzWZlI5XG"

url = main_api + urllib.parse.urlencode({"api_key":api_key, "start_date":start_date, "end_date":end_date})


json_data = requests.get(url).json()
print(json_data)

