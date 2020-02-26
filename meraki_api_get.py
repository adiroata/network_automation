#!/usr/bin/env python

# https://www.kias.ro/2020/02/meraki-dashboard-api.html

import requests
import json

url = "https://api.meraki.com/api/v0/networks/{{networkId}}/clients"

payload = {}
headers = {
  'Accept': '*/*',
  'X-Cisco-Meraki-API-Key': '{{Meraki_API_key}}',
  'User-Agent': 'PostmanRuntime/7.22.0',
  'Cache-Control': 'no-cache',
  'Postman-Token': '{{Token}}',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://api.meraki.com/api/v0/networks/{{networkId}}/clients',
  'Connection': 'keep-alive'
}

response = requests.request("GET", url, headers=headers, data = payload)
jsonfile = json.loads(response.text.encode('utf8'))

#print(jsonfile)

for dictionary in jsonfile:
    keys = ['description','manufacturer','mac','ip','lastSeen','ssid','status']
    print('')
    for key in keys:
        output = dictionary.get(key)
        print str(key),':',str(output)
print('')

