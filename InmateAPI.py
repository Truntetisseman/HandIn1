#%%%
import requests
import json
#from PIL import Image

save = True
url = "http://www.JailBase.com/api/1/search/"
params = {'source_id' : 'ca-sfso', 'last_name' : 'Smith'}
response = requests.get(url , params = params)

if response.status_code == 200: #The API returns the Ok() http status code when everything is okay
    if len(response.json()["records"]) > 0:
        records = response.json()["records"]
        sortedRecords = sorted(records, key=lambda k: k['book_date'], reverse=True)
        print(sortedRecords)
    else : 
        print("No records found")
else:
    print("Http status code : ", response.status_code)

date = str(response.json()["records"][0]["book_date"])
date = date.replace("-", "/")
print(date)
#%%%

url = "https://www.metaweather.com/api/location/2487956/" + date
print(url)
response = requests.get(url)
weather = response.json()
print(weather)


#%%%

#Saving as json file
if save :
    with open('records.json', 'w') as outfile:
        json.dump(records, outfile)
    with open('weather.json', 'w') as outfile:
        json.dump(weather, outfile)
else :
    exit()


