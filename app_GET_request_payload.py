import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/"

# Adding a payload
payload = {"id": [1, 2, 3], "userId":1}

# A get request to the API
response = requests.get(url, params=payload)

# Print the response
response_json = response.json()

for i in response_json:
    print(i, "\n")



