import requests

url = "https://icanhazdadjoke.com/j/R7UfaahVfFd"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

joke = response.json()

print(f"\n{joke['joke']}\n")