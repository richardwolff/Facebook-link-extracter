from fbchat import Client
from fbchat.models import *
import pandas as pd
import pygsheets

## Facebook login: Client(username, password)
client = Client( , )

## insert path to local gsheetpermit json
localpath=' ' 

namedict={}

## insert names of people in group 
names = []

for name in names:
  namedict[client.searchForUsers(name)[0].uid] = name

## insert thread_id here. Fetches last 10000 messages — adjust as necessary
messages=client.fetchThreadMessages(thread_id=' ',,limit=10000)

lines=[]
cols=['Name','Title','Link','Source']

d=dict.fromkeys(cols)
df1=pd.DataFrame(columns=cols)

for message in messages:
    
    try:
        m=message.attachments[0]
        info=[namedict[message.author],m.title,m.original_url,m.source]
        for i in range(len(cols)):
            d[cols[i]]=info[i]
        df1=df1.append(d,ignore_index=True)
    
    except:
        pass

c=pygsheets.authorize(service_file=localpath)

## insert name of gsheet to create and write to
sh=c.create(' ')

## insert email associated with gsheets
sh.share(" ",role='writer')

wks.set_dataframe(df1,(1,1))
