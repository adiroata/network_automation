import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from napalm import get_network_driver
from getpass import getpass

# Pasi activare API:
# 1. Accesam: https://console.cloud.google.com/
# 2. Cream un nou proiect
# 3. Activam Google Drive API & Google Sheets API
# 4. Generam un fisier de autentificare pentru Google Drive API
# 5. Facem share la un Worksheet catre adresa de email din JSON-ul de autentificare
# 
# Procedura completa este documentata pe https://www.kias.ro/2020/02/google-sheets-api.html
#
# Documentatie gspread:  https://gspread.readthedocs.io/en/latest/index.html
# Documentatie NAPALM: https://napalm.readthedocs.io/en/latest/#
#
# Autor: https://www.adiroata.eu

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

# Specificam fisierul JSON prin care vom prezenta Token-ul de Autentificare catre API
creds = ServiceAccountCredentials.from_json_keyfile_name("gdrive-creds.json", scope)

# Deschidem fisierul la care ne-a fost acordat accesul
client = gspread.authorize(creds)
sheet = client.open("python_sheets_API_get").sheet1

# Facem clear la vechile intrari si generam capul de tabel
sheet.clear()
headerRow=['Router', 'Interfata', 'Adresa IP', 'Descriere']
sheet.insert_row(headerRow, 1)

# Introducem parola de autentificare pe CPE
parola = getpass()

# Configuram NAPALM pentru conectarea pe CPE 
routere=['10.255.255.10', '10.255.255.11']
for router in routere:
    driver = get_network_driver('ios')
    device = driver(router, 'admin', parola)
    device.open()

# Colecteaza informatia de pe CPE
    dict_ip=device.get_interfaces_ip()
    dict_if=device.get_interfaces()
    dict_facts=device.get_facts()

# Pentru T-Shoot:
#print(json.dumps(dict_ip, indent=4))
#print(json.dumps(dict_if, indent=4))
#print(dict_facts['fqdn'])

#Listeaza toate cheile dictionarului 'dict_ip'
    lista_key_ip=dict_ip.keys()

# Help 
# Se poate obtine acelasi output cu: lista_key_ip=list(dict_ip)

# Pentru fiecare cheie salveaza valoarea intr-o variabila
# Fiecare valoare este un dictionar mai mic  
    n=1
    for iface_key in lista_key_ip:
        n += 1
        dict_ip_mici=dict_ip[iface_key]
        new_dict_ip=dict_ip_mici['ipv4']
        ip_key=list(new_dict_ip)
        adresaip=ip_key[0]
        masca=dict_ip_mici['ipv4'][str(adresaip)]['prefix_length']
        adresaip_cidr=(str(adresaip) + '/' + str(masca))
        descriere=dict_if[str(iface_key)]['description']
        hostname=dict_facts['fqdn']

        insertRow = [hostname, iface_key, adresaip_cidr, descriere]
        sheet.insert_row(insertRow, n)

# Done.
