import json
import os
import pytest
import time
import tokens
from unittest.mock import MagicMock

def test_get():
    tokens.TOKENS = {'test': {'access_token': 'mytok123',
                              'expires_at': time.time() + 3600}}
    tokens.get('test')


def test_refresh(monkeypatch, tmpdir):
    tokens.configure(dir=str(tmpdir), url='')
    tokens.manage('mytok', ['myscope'])
    with pytest.raises(tokens.ConfigurationError):
        tokens.refresh('mytok')

    tokens.configure(dir=str(tmpdir), url='https://example.org')

    with open(os.path.join(str(tmpdir), 'user.json'), 'w') as fd:
        json.dump({'application_username': 'app', 'application_password': 'pass'}, fd)

    with open(os.path.join(str(tmpdir), 'client.json'), 'w') as fd:
        json.dump({'client_id': 'cid', 'client_secret': 'sec'}, fd)

    response = MagicMock()
    response.json.return_value = {'expires_in': 123123, 'access_token': '777'}
    monkeypatch.setattr('requests.post', lambda url, **kwargs: response)
    tok = tokens.get('mytok')
    assert tok == '777'
