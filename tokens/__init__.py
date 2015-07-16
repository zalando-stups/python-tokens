import json
import os
import requests


CONFIG = {'url': os.environ.get('OAUTH_ACCESS_TOKEN_URL'),
          'dir': os.environ.get('CREDENTIALS_DIR')}

TOKENS = {}


def configure(**kwargs):
    CONFIG.update(kwargs)


def manage(token_name, scopes):
    TOKENS[token_name] = {'scopes': scopes}


def start():
    # TODO: start background thread to manage tokens
    pass


def get(token_name):
    token = TOKENS[token_name]
    access_token = token.get('access_token')
    if not access_token:
        path = CONFIG['dir']
        with open(os.path.join(path, 'user.json')) as fd:
            user_data = json.load(fd)
        with open(os.path.join(path, 'clien.json')) as fd:
            client_data = json.load(fd)
        body = {
                'grant_type': 'password',
                'username': user_data.get('application_username'),
                'password': user_data.get('application_password'),
                'scope': ' '.join(token['scopes'])
                }

        r = requests.post(CONFIG['url'], data=json.dumps(body),
                          auth=(client_data.get('client_id'), client_data.get('client_secret')),
                          headers={'Content-Type': 'application/json'})
        data = r.json()
        token['data'] = data
        token['access_token'] = data.get('access_token')


    return access_token

