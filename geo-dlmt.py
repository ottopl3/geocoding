import requests
import csv
from requests.structures import CaseInsensitiveDict

def dlmtObject(id, jsonDump):
	if len(jsonDump['features'])>0:
		result = str(id) + "\t" + jsonDump['query']['text'] + "\t" + str(jsonDump['features'][0]['properties']['lat']) + "\t" + str(jsonDump['features'][0]['properties']['lon'])
	else:
		result = str(id) + "\t" + jsonDump['query']['text'] + "\t" + "na" + "\t" + "na"
	return result
	
API_KEY = ""
	
with open("geokodolashoz.txt","r", encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')
    rows = [row for row in reader]

i=0
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
f=open("result_dlmt.txt","w", encoding='utf-8')
f.write("ID\tQuery\tlat\tlon\n")
for row in rows:
	id = row[0]
	address = row[1]
	print(address)
	i=i+1

	url = "https://api.geoapify.com/v1/geocode/search?text=" + address + "&filter=countrycode:hu&apiKey=" + API_KEY
	print(url)

	resp = requests.get(url, headers=headers)

	print(resp.status_code)
	geoResult = dlmtObject(id, resp.json())
	print(geoResult)
	
	f.write(geoResult + "\n")
f.close()
	