# Created by vidit.singh at 15-06-2022

import json

# Processing json
person = '{"id":1,"first_name":"Frasco","last_name":"Necolds","email":"fnecolds0@vk.com","gender":"Male","ip_address":"243.67.63.34"}'

json_dict = json.loads(person)

print(json_dict)
print(json_dict['first_name'])

persons = '''{"id":1,"first_name":"Frasco","last_name":"Necolds","email":"fnecolds0@vk.com","gender":"Male","ip_address":"243.67.63.34"}
{"id":2,"first_name":"Dulce","last_name":"Santos","email":"dsantos1@mashable.com","gender":"Female","ip_address":"60.30.246.227"}
{"id":3,"first_name":"Prissie","last_name":"Tebbett","email":"ptebbett2@infoseek.co.jp","gender":"Genderfluid","ip_address":"22.21.162.56"}
{"id":4,"first_name":"Schuyler","last_name":"Coppledike","email":"scoppledike3@gnu.org","gender":"Agender","ip_address":"120.35.186.161"}
{"id":5,"first_name":"Leopold","last_name":"Jarred","email":"ljarred4@wp.com","gender":"Agender","ip_address":"30.119.34.4"}
{"id":6,"first_name":"Joanna","last_name":"Teager","email":"jteager5@apache.org","gender":"Bigender","ip_address":"245.221.176.34"}
{"id":7,"first_name":"Lion","last_name":"Beere","email":"lbeere6@bloomberg.com","gender":"Polygender","ip_address":"105.54.139.46"}
{"id":8,"first_name":"Marabel","last_name":"Wornum","email":"mwornum7@posterous.com","gender":"Polygender","ip_address":"247.229.14.25"}
{"id":9,"first_name":"Helenka","last_name":"Mullender","email":"hmullender8@cloudflare.com","gender":"Non-binary","ip_address":"133.216.118.88"}
{"id":10,"first_name":"Christine","last_name":"Swane","email":"cswane9@shop-pro.jp","gender":"Polygender","ip_address":"86.16.210.164"}'''

# first convert json string into list of json strings

persons_list = persons.splitlines()

# converting json to list of dicts using list comprehension.
persons_list_obj = [json.loads(p) for p in persons_list]
print(persons_list_obj[3]['first_name'])

# converting list of string into list of dicts using map() of python
person_dict = list(map(lambda per: json.loads(per), persons_list))

print(person_dict[0])

# to fetch only names from person_dict
name_list = list(map(lambda p: p['first_name'], person_dict))

print(name_list)

#  filtering data from json dicts
print(list(filter(lambda p: p['gender'] == 'Female', person_dict)))

per = '''{
    "results": [
        {
            "id": 1,
            "first_name": "Frasco",
            "last_name": "Necolds",
            "email": "fnecolds0@vk.com",
            "gender": "Male",
            "ip_address": "243.67.63.34"
        },
        {
            "id": 2,
            "first_name": "Dulce",
            "last_name": "Santos",
            "email": "dsantos1@mashable.com",
            "gender": "Female",
            "ip_address": "60.30.246.227"
        },
        {
            "id": 3,
            "first_name": "Prissie",
            "last_name": "Tebbett",
            "email": "ptebbett2@infoseek.co.jp",
            "gender": "Genderfluid",
            "ip_address": "22.21.162.56"
        },
        {
            "id": 4,
            "first_name": "Schuyler",
            "last_name": "Coppledike",
            "email": "scoppledike3@gnu.org",
            "gender": "Agender",
            "ip_address": "120.35.186.161"
        },
        {
            "id": 5,
            "first_name": "Leopold",
            "last_name": "Jarred",
            "email": "ljarred4@wp.com",
            "gender": "Agender",
            "ip_address": "30.119.34.4"
        },
        {
            "id": 6,
            "first_name": "Joanna",
            "last_name": "Teager",
            "email": "jteager5@apache.org",
            "gender": "Bigender",
            "ip_address": "245.221.176.34"
        },
        {
            "id": 7,
            "first_name": "Lion",
            "last_name": "Beere",
            "email": "lbeere6@bloomberg.com",
            "gender": "Polygender",
            "ip_address": "105.54.139.46"
        },
        {
            "id": 8,
            "first_name": "Marabel",
            "last_name": "Wornum",
            "email": "mwornum7@posterous.com",
            "gender": "Polygender",
            "ip_address": "247.229.14.25"
        },
        {
            "id": 9,
            "first_name": "Helenka",
            "last_name": "Mullender",
            "email": "hmullender8@cloudflare.com",
            "gender": "Non-binary",
            "ip_address": "133.216.118.88"
        },
        {
            "id": 10,
            "first_name": "Christine",
            "last_name": "Swane",
            "email": "cswane9@shop-pro.jp",
            "gender": "Polygender",
            "ip_address": "86.16.210.164"
        }
    ]
}'''

p_data = json.loads(per)

print(p_data['results'][0])