print ("")
print ("++++++---++++++++++++---++++++++++++---++++++++++++---++++++++++++-")
print (" ___            ___          __                       ____________ ")
print ("|   \          /   |         | |                     |____    ____|")
print ("| |\ \        / /| |   ___   | |         ___              |  |     ")
print ("| | \ \      / / | |  / __ \ | |_____   / __ \     _      |  |     ")
print ("| |  \ \    / /  | | | |  | ||  __   | | |  | |   |_|     |  |     ")
print ("| |   \ \  / /   | | | |__| || |__|  | | |__| |           |  |     ")
print ("|_|    \_\/_/    |_|  \ ___/ |_______|  \____/            |__|     ")
print ("                                                                   ")
print ("++++++---++++++++++++---++++++++++++---++++++++++++---++++++++++++-")
print ("")

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

api_id =                          #enter here api_id 
api_hash = '' #Enter here api_hash id
phone = ''          #enter here phone number with country code
client = TelegramClient(phone, api_id, api_hash)

print("api_id: ")
ap-id = input()
print("api_hash: ")
ap-hash =input()

async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello !!!!')
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter verification code: '))


chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

print('From Which Group Yow Want To Scrap A Members:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Please! Enter a Number: ")
target_group=groups[int(g_index)]

print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Saving In file...')
with open("Scrapped.csv","w",encoding='UTF-8') as f:#Enter your file name.
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
print('Members scraped successfully.......')
print(':)')
