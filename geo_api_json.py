import urllib.parse
import requests

main_api = "http://paleobiodb.org/data1.2/taxa/single.json?"
name = "Dascillidae"


url = main_api + urllib.parse.urlencode({"name":name})

json_data = requests.get(url).json()
print(json_data)