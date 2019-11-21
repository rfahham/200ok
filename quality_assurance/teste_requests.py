# !/usr/bin/env python
# -- coding: utf-8 --

import requests
import urllib3

url = ''
urllib3.disable_warnings()
r = requests.get(url, verify=False)
print url
print r.status_code