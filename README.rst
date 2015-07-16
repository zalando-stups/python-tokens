=============
Python Tokens
=============

A Python library that keeps OAuth 2.0 service access tokens in memory for your usage.

Installation
============

.. code-block:: bash

    $ sudo pip3 install --upgrade stups-tokens

Usage
=====

.. code-block:: python

    import requests
    import time
    import tokens

    # will use OAUTH2_ACCESS_TOKEN_URL environment variable by default
    # will try to read application credentials from CREDENTIALS_DIR
    tokens.configure(url='https://example.com/access_tokens')
    tokens.manage('example', ['read', 'write'])
    tokens.start()

    tok = tokens.get('example')

    requests.get('https://example.org/', headers={'Authorization': 'Bearer {}'.format(tok)})

    time.sleep(3600) # make the token expire

    tok = tokens.get('example') # will refresh the expired token
    requests.get('https://example.org/', headers={'Authorization': 'Bearer {}'.format(tok)})
