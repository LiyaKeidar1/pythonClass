import json

# Open the orders.json file
with open("orders.json") as file:
    # Load its content and make a new dictionary
    data = json.load(file)

    # Delete the "client" key-value pair from each order
    for order in data["orders"]:
        del order["client"]

# Open (or create) an orders_new.json file
# and store the new version of the data.
with open("orders_new.json", 'w') as file:
    json.dump(data, file, indent= 4)

