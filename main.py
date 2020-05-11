import requests
import json

API_KEY = "teqVRTa6T0fr"
PROJECT_TOKEN = "tC-w4ZE2duZT"
RUN_TOKEN = "tF39FsT3mtTP"



class Data:
    '''
    instantiate api_key and project_token
    '''
    def __init__(self, api_key, project_token):

        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }

        # every time you instantiate the object, you get the data as well from get_data function
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run//data',
                                params=self.params)
        self.data = json.loads(response.text)

    def export_json(self):
        json_data = self.data

        with open('covid_details.json', 'w') as json_file:
            json.dump(json_data, json_file)


    def get_total_cases(self):
        data = self.data['total']

        for content in data:
            if content['name'] == 'Coronavirus Cases:':
                return content['value']

    def get_total_deaths(self):
        data = self.data['total']

        for content in data:
            if content['name'] == 'Deaths:':
                return content['value']

        return '0'

    def get_country_data(self, country):
        data = self.data['country']

        for content in data:
            if content['name'] == country:
                return content

        return '0'

data = Data(API_KEY, PROJECT_TOKEN)

