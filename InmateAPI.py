import requests

url = "http://www.JailBase.com/api/1/search/"
params = {'source_id' : 'az-mcso', 'last_name' : 'jensen'}
#params = {'last_name' : 'jensen'} #To text status code else statement
response = requests.get(url , params = params)
if response.status_code == 200:
    print(response.json()["current_page"]) #Prints all the json objects on the page
    #print(len(response.json()["records"])) #Prints the amount of records on page
else:
    print("Http status code : ", response.status_code)

