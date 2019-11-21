# !/usr/bin/env python
# -- coding: utf-8 --

import requests
import urllib3
import certifi

r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})
print(r.status_code, r.reason)
print(r.text[:300] + '...')
