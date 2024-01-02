# Write a function called save_json. This function takes a
# dictionary below as an argument and saves it on a file in JSON
# format.
# Write another function called read_json that opens the file
# that you just saved and reads its content.
# names = {'name': 'Carol','sex': 'female','age': 55}
import json
def save_json():
    names = {'name': 'Carol','sex': 'female','age': 55}
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(names, f, ensure_ascii=False, indent=4)


def read_json():
    with open('data.json', 'r') as json_data:
        json_file = json.load(json_data)
        print(json_file)
        #return json_data.read()