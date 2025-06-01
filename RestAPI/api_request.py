import requests
import pandas as pd
baseurl = 'https://rickandmortyapi.com/api/'

enpoint = 'character'

# response_get = requests.get(baseurl + enpoint)

# print(response_get.json())

def main_request(baseurl, enpoint):
    response = requests.get(baseurl + enpoint)
    return response.json()

def main_request_page(baseurl, enpoint, page):
    response = requests.get(baseurl + enpoint + '?page=%s'%page)
    return response.json()


def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    characters_list = []
    for item in response['results']:
        character = {
            'id': item['id'], 
            'name': item['name'], 
            'no_ep': len(item['episode'])
        }
        characters_list.append(character)  
    return characters_list



data = main_request(baseurl=baseurl, enpoint=enpoint)
print(get_pages(data))
parse_json(data)


all_data_list = []
for page in range(1, get_pages(data) + 1):
    all_data_list.extend(parse_json(main_request_page(baseurl=baseurl, enpoint=enpoint, page=page)))


data_frame = pd.DataFrame(all_data_list)

data_frame.to_csv('character_list.csv', index=False)

