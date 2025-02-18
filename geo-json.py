import requests
import json
from requests.structures import CaseInsensitiveDict

def geoObject(id, jsonDump):
	if len(jsonDump['features'])>0:
		result = '{"resultID":"' + str(id) + '","query":"' + jsonDump['query']['text'] + '", "lat":"' + str(jsonDump['features'][0]['properties']['lat']) + '", "lon":"' + str(jsonDump['features'][0]['properties']['lon']) + '"}'
	else:
		result = '{"resultID":"' + str(id) + '","query":"' + jsonDump['query']['text'] + '", "lat":"na", "lon":"na"}'
	return result

API_KEY = ""
	
data_file = open('geokodolashoz.json','r', encoding='utf-8')
data = json.load(data_file)
data_file.close()
i=0
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
f=open("result_json.json","w", encoding='utf-8')
f.write('[')
for address in data:
	print(address['CIM'])
	i=i+1

	url = "https://api.geoapify.com/v1/geocode/search?text=" + address['CIM'] + "&filter=countrycode:hu&apiKey=" + API_KEY
	print(url)
	

	resp = requests.get(url, headers=headers)

	print(resp.status_code)
	geoResult = geoObject(address['ID'], resp.json())
	print(geoResult)

	f.write(geoResult)
	if i<len(data):
		f.write(',')
f.write(']')
f.close()


	