import requests
# A deliberate typo is made in the endpoint "postz" instead of "posts"
url = "https://jsonplaceholder.typicode.com/postz"

# Attempt to GET data from provided endpoint
try:
    response = requests.get(url)
    response.raise_for_status()
# If the request fails (404) then print the error.
except requests.exceptions.HTTPError as error:
  print(error)

"""
404 Client Error: Not Found for url: https://jsonplaceholder.typicode.com/postz
"""




