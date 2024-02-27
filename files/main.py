import json

# with open("myfile.json", "r") as f:
#     dict1 = json.load(f)
#
# print(list(filter(lambda x: x[1]['age'] > 29, dict1.items()))) #tuple pairs of key and value
#
# print(list(filter(lambda x: dict1[x]['age'] > 29, dict1))) #the keys of the dictionary are going into the lambda function when I call it by itself.



import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level= logging.DEBUG,
    datefmt= '%Y-%m-%d %H:%M:%S'
)

logging.debug("debug message")
logging.info("info message")
logging.error("error message")


import sys

for i, arg in enumerate(sys.argv):
    if i==0:
        print("Script name:{}".format(sys.argv[0]))
    else:
        print("{}. arguments is:{}".format(i, arg))


my_dict= {1:"a", 2:"b", 3:"c", 4:"a"}
my_dict1= my_dict.copy()
for key, value in my_dict.items():
    if value=="a":
        my_dict1.__delitem__(key)
my_dict = my_dict1
print(my_dict)