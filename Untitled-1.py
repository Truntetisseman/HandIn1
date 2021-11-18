#%%%
import requests
import json
#from PIL import Image

save = False
url = "http://www.JailBase.com/api/1/search/"
params = {'source_id' : 'az-mcso', 'last_name' : 'jensen'}
response = requests.get(url , params = params)

if response.status_code == 200: #The API returns the Ok() http status code when everything is okay
    if len(response.json()["records"]) > 0:
        records = response.json()["records"]
        print(type(records))
        sortedRecords = sorted(records, key=lambda k: k['book_date'], reverse=True)
        print(sortedRecords)
    else : 
        print("No records found")
else:
    print("Http status code : ", response.status_code)

#Saving as json file
if save :
    with open('records.json', 'w') as outfile:
        json.dump(records, outfile)
else :
    exit()







#%%%
# Reading image
#from PIL import Image # pip3 install Pillow

#url = 'https://imgstore.jailbase.com/small/arrested/az-mcso/2020-10-28/trevon-tajee-smith-t662412.pic1.jpg'
#im = Image.open(requests.get(url, stream=True).raw)
#im
