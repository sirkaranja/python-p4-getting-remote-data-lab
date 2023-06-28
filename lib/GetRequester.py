
from urllib import response
import requests
import json

from lib.testing.get_requester_test import CONVERTED_DATA




class GetRequester:
    url= 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
    CONVERTED_DATA = [{ 'name': 'Daniel', 'occupation' : 'LG Fridge Salesman' }, { 'name': 'Joe', 'occupation': 'WiFi Fixer' }, { 'name': 'Avi', 'occupation': 'DJ' }, { 'name': 'Howard', 'occupation': 'Mountain Legend' }]


    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        assert response.get_response_body()=JSON_STRING

    def load_json(self):
        # responce_body= self.get_response_body
        assert response.load_json()== CONVERTED_DATA
        # data=json.loads(responce_body)
        # return data
       
        