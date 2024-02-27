import json
country_json = '{"Country Name": "USA", "States": " "}'
dict1 = {"Name": "Keidar"}
json.dump(dict1, open("myfile.json", "w"), indent=6)
