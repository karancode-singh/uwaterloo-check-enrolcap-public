import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from telethon import TelegramClient, events, sync

url = 'https://classes.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl'

headers = CaseInsensitiveDict()
headers["Accept"] = "*/*"
headers["User-Agent"] = "PostmanRuntime/7.28.0"
payload = {'level':'grad','sess':'1221','subject':'ECE','cournum':'657A'}

## Telegram details for sending notification ##
channel = ''
api_id = ''
api_hash = ''
phone = ''
username = ''
############

client = TelegramClient(username, api_id, api_hash)
client.start()

############
resp = requests.post(url, headers=headers, data=payload)
if resp.status_code != 200:
    print('ERROR')
    client.send_message(channel, 'ERROR')
else:
    parsed_html = BeautifulSoup(str(resp.content),"lxml")
    no = parsed_html.body.findAll('tr')[4].findAll('td')[7].text
    if(int(no) < 132): ## replace 132 with max general enrolment allowed
        print('**',no,'**')
        client.send_message(channel, no+" https://quest.pecs.uwaterloo.ca/psp/SS/ACADEMIC/SA/?cmd=login&languageCd=ENG")
    else:
        print(no)