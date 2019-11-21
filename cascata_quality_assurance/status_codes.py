# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib3
import certifi

urllib3.disable_warnings()

r = requests.get('https://globo.com', verify=False)
# print r.status_code


if (r.status_code == 200):
    print("Status Code 200 ")
if (r.status_code == 401):
    print("Status Code 401 ")
if (r.status_code == 404):
    print("Status Code 404 ")
if (r.status_code == 500):
    print("Status Code 500 ")

