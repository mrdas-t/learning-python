import requests

username = "mrdas-t"
response = requests.get(f"https://api.github.com/users/{username}")
data = response.json()

print(f"Username: {data['login']}")
print(f"Account created: {data['created_at']}")
print(f"Public repos: {data['public_repos']}")
print(f"Followers: {data['followers']}")