#!/usr/bin/env python

# https://www.kias.ro/2020/02/meraki-dashboard-api.html

import requests

files = [

]
headers = {
  'Accept': '*/*',
  'Content-Type': 'application/x-www-form-urlencoded',
  'X-Cisco-Meraki-API-Key': '{{Meraki_API_key}}',
  'User-Agent': 'PostmanRuntime/7.22.0',
  'Cache-Control': 'no-cache',
  'Postman-Token': '{{Token}}',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Length': '273',
  'Connection': 'keep-alive'
}

choice = raw_input('Configure ? (yes/no)\n')

networks = ['{{networkId}}', '{{networkId}}']

if choice == 'yes':
    for i in networks:
        preurl = "https://api.meraki.com/api/v0/networks/"+str(i)+"/ssids/"
        for n in range (10, 15):
            url = preurl+str(n)
            payload = {'number': n,
            'name': 'Python SSID '+str(n),
            'authMode': 'psk',
            'psk': 'pythoniscool',
            'encryptionMode': 'wpa',
            'wpaEncryptionMode': 'WPA2 only',
            'ipAssignmentMode': 'NAT mode',
            'enabled': 'true'}
            response = requests.request("PUT", url, headers=headers, data = payload, files = files)

            print(response.text.encode('utf8'))

elif choice == 'no':
    for i in networks:
        preurl = "https://api.meraki.com/api/v0/networks/"+str(i)+"/ssids/"
        for n in range (10, 15):
            url = preurl+str(n)
            payload = {'number': n,
            'name': 'Unconfigured SSID '+str(n),
            'authMode': 'open',
            'ipAssignmentMode': 'NAT mode',
            'enabled': 'false'}
            response = requests.request("PUT", url, headers=headers, data = payload, files = files)

            print(response.text.encode('utf8'))

else:
    print 'Invalid option.'
