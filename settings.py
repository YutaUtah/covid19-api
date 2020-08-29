import configparser

conf = configparser.ConfigParser()
conf.read('settings.ini')

api_key = conf['api']['API_KEY']
project_token = conf['api']['PROJECT_TOKEN']
run_token = conf['api']['RUN_TOKEN']

print(run_token)