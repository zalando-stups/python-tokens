=============
Python Tokens
=============

A Python library that keeps OAuth 2.0 service access tokens in memory for your usage.

Usage
=====

.. code-block:: python

    import tokens

    # will use OAUTH2_ACCESS_TOKEN_URL environment variable by default
    tokens.configure(url='https://example.com/access_tokens')
    tokens.manage('example', ['read', 'write'])
    tokens.start()

    tok = tokens.get('example')

    requests.get('https://example.org/', headers={'Authorization': 'Bearer {}'.format(tok)})
