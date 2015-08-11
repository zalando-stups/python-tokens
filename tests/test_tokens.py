import time
import tokens

def test_get():
    tokens.TOKENS = {'test': {'access_token': 'mytok123',
                              'expires_at': time.time() + 3600}}
    tokens.get('test')

