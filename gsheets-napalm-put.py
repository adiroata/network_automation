import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import telnetlib
from getpass import getpass
import gzip


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
sheet = client.open("python_sheets_API_put").sheet1

# Introducem parola de autentificare pe CPE
parola = getpass()

# Configuram NAPALM pentru conectarea pe CPE
# Lista rutere
routere=['10.255.255.10', '10.255.255.11']
# Lista index randuri
rows_index=[2, 3]

# Configuram CPE
for router, n in zip(routere, rows_index):
    cell = sheet.cell(n,3).value
    print('Se acceseaza: ' + router)
    tn=telnetlib.Telnet(router)
    tn.read_until('Username: ')
    tn.write('admin\n')
    if parola:
        tn.read_until('Password: ')
        tn.write(parola + '\n')

    tn.write('conf t\n')
    tn.write('interface Loop1337\n')
    tn.write('ip address ' + str(cell) + ' 255.255.255.255\n')
    tn.write('end\n')
    tn.write('copy run start\n')
    tn.write('\n')
    tn.write('\n')
    tn.write('exit\n')

    readoutput=tn.read_until('exit', 5)
    print(readoutput)

# Done.
