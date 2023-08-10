import requests
try:
    my_file = requests.get("dskfjakldsfjkladsjfklasdjflkasdjlfkj")
except requests.exceptions.MissingSchema as e:
    print("invalid schema")
