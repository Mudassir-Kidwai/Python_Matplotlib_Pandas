"""Example of Python client calling Knowledge Graph Search API."""
import json
import urllib
"""key=AIzaSyAw0d9xQn-DCVrXsw2_wGqahDBM0WFkpvk"""
"""api_key = open('.api_key').read()"""
api_key = open('AIzaSyAw0d9xQn-DCVrXsw2_wGqahDBM0WFkpvk.api_key').read()
query = 'Taylor Swift'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': api_key,
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for element in response['itemListElement']:
  print(element['result']['name'] + ' (' + str(element['resultScore']) + ')')
