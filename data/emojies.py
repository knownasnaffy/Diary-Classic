import json

with open('./data/db.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    emojies = data["emojies"]