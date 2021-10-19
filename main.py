import pandas as pd
import requests
import urllib.parse
import json
import matplotlib.pyplot as plt

data = pd.read_excel('Data_Set.xlsx')
s = pd.DataFrame(data, columns= ['Address, Type'])

address_list = []
type_list = []

iUPUI_address = s.cell(2,2).value
address_list.append(iUPUI_address)
The_Speak_Easy_address = s.cell(3,2).value
address_list.append(The_Speak_Easy_address)
The_Speak_Easy_address = s.cell(4,2).value
address_list.append(The_Speak_Easy_address)
The_Speak_Easy_address = s.cell(5,2).value
address_list.append(The_Speak_Easy_address)
The_Speak_Easy_address = s.cell(6,2).value
address_list.append(The_Speak_Easy_address)
The_Speak_Easy_address = s.cell(7,2).value
address_list.append(The_Speak_Easy_address)

iUPUI_type = s.cell(2,3).value
type_list.append(iUPUI_type)
The_Speak_Easy_type = s.cell(3,3).value
type_list.append(The_Speak_Easy_type)
zWORKS_type = s.cell(4,3).value
type_list.append(zWORKS_type)
Launch_Fishers_type = s.cell(5,3).value
type_list.append(Launch_Fishers_type)
Industrious_Mass_Ave_type = s.cell(6,3).value
type_list.append(Industrious_Mass_Ave_type)
Launch_Indy_type = s.cell(7,3).value
type_list.append(Launch_Indy_type)

for addresses in address_list:
    address = addresses
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

    response = requests.get(url).json()
    location = response[0]["lat"] + response[0]["lon"]
    
    final_data = []

    radius='1500'
    types='restaurant'
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&types=%s&key=api key" % (location,radius,types)
    counter = 0

    while True:

        response = requests.request("POST", url)
        response = json.loads(response.text)
        results = response['results']

        for result in results:
            final_data.append(result)
            counter += 1

        if 'next_page_token' not in response:
            break
        else:
            next_page_token = response['next_page_token']

        next_page_token = '&pagetoken=%s' % str(next_page_token)
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&types=%s&key=api key%s" % (location,radius,types,next_page_token)

    print(final_data)

    radius='1000'
    types='housing'
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&types=%s&key=api key" % (location,radius,types)
    counter1 = 0

    while True:

        response = requests.request("POST", url)
        response = json.loads(response.text)
        results = response['results']

        for result in results:
            final_data.append(result)
            counter1 += 1

        if 'next_page_token' not in response:
            break
        else:
            next_page_token = response['next_page_token']

        next_page_token = '&pagetoken=%s' % str(next_page_token)
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&types=%s&key=api key%s" % (location,radius,types,next_page_token)

    print(final_data)

    radius='2500'
    types='conference'
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&types=%s&key=api key" % (location,radius,types)
    counter2 = 0

    while True:

        response = requests.request("POST", url)
        response = json.loads(response.text)
        results = response['results']

        for result in results:
            final_data.append(result)
            counter2 += 1

        if 'next_page_token' not in response:
            break
        else:
            next_page_token = response['next_page_token']

        next_page_token = '&pagetoken=%s' % str(next_page_token)
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&types=%s&key=api key%s" % (location,radius,types,next_page_token)

    print(final_data)

    radius='3000'
    types='event'
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&types=%s&key=api key" % (location,radius,types)
    counter3 = 0

    while True:

        response = requests.request("POST", url)
        response = json.loads(response.text)
        results = response['results']

        for result in results:
            final_data.append(result)
            counter3 += 1

        if 'next_page_token' not in response:
            break
        else:
            next_page_token = response['next_page_token']

        next_page_token = '&pagetoken=%s' % str(next_page_token)
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&types=%s&key=api key%s" % (location,radius,types,next_page_token)

    print(final_data)

plt.plot([1, 2, 3, 4], [counter, counter1, counter2, counter3], 'ro')
plt.show()

