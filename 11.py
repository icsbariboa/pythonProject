import requests
response = requests.get("https://api.github.com/users/avielb/repos")
repositories = response.json()

for repo in repositories:
    if "DEVOPS" in repo["name"].upper():
        print(repo["name"].upper())
# if response.status_code == 200:
#     print("github is up and running")
# else:
#     print("github is down " + str(response.status_code))
