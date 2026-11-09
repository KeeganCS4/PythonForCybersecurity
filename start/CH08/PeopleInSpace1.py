import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

astronauts = response.json()

# print number of people
print(f"There are {astronauts['number']} Astronauts in space.\n")

# print first person
# print(f"{astronauts['people'][0]['name']}")

# print out and number each person
count = 0
people = astronauts['people']
for person in people:
    print(f"{count + 1}: {person['name']} is on the {person['craft']}")
    count += 1