import pygsheets
from fbchat import Client
from fbchat.models import *
import pandas as pd
from pandas.util.testing import assert_frame_equal
import numpy as np
import time

## Facebook login: Client(username, password)
client = Client( , )

## insert path to local gsheetpermit json
localpath=' ' 

namedict={}

## insert names of people in group 
names = []

for name in names:
  namedict[client.searchForUsers(name)[0].uid] = name

## insert thread_id here
messages=client.fetchThreadMessages(thread_id=' ')

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

## insert name of gsheet to write to
sh=c.open(' ')

## insert email associated with gsheets
sh.share(" ",role='writer')

wks=sh[0]
df2=wks.get_as_df()
filter=df2!=""
dfNew=df2[filter]
df2=dfNew.dropna(how='all')
newlinks=list(np.setdiff1d(list(df1['Link']),list(df2['Link'])))
dfnew=[df1[df1.Link==newslinks[i]] for i in range(len(newlinks))]

try:
	dff=pd.concat(dfnew)
	wks.insert_rows(row=1,number=len(dff))
	wks.set_dataframe(dff,(1,1))
	wks.frozen_rows=1

except:
	pass
