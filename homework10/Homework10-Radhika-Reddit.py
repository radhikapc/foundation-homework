
# coding: utf-8

# In[107]:

import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get("https://www.reddit.com/", headers=headers)
doc = BeautifulSoup(response.text, 'html.parser')


# In[108]:

import pandas as pd


# In[109]:

#doc


# #### The title of the post

# In[110]:

def title(my_dict):
    title = doc.find_all("p", { 'class': 'title'})
    for i in title:
        return (i.text.strip())
title(doc)


# #### The number of votes it has (the number between the up and down arrows)

# In[111]:

def votes(my_dict):
    voted = doc.find_all("div", { 'class': 'score unvoted'})
    for i in voted:
        #print(i.text)
        if i.text == "•":
            return 0
        else:
            return (i.text.strip())
votes(doc)


# In[6]:

#### The number of comments it has


# In[112]:

def comments(my_dict):
    comm = doc.find_all("li", { 'class': 'first'})
    for i in comm:
        if i.text == "comment":
            return "no comments"
        else:
            return (i.text.strip())     
comments(doc)


# In[13]:

#comm = doc.find_all("li", { 'class': 'first'})
#for i in comm:
        #if i.text == "comment":
            #print(0)
        #else:
            #print(i.text)


# #### What subreddit it is from (e.g. /r/AskReddit, /r/todayilearned)

# In[15]:

#sub = doc.find_all ("p", {'class': 'tagline'})
#for i in sub:
    #subred = doc.find_all("a", {'class': 'subreddit hover may-blank'})
    #for i in subred:
        #print(i.text)


# In[113]:

def subreddit(my_dict):
    sub = doc.find_all ("p", {'class': 'tagline'})
    for i in sub:
        subred = doc.find_all("a", {'class': 'subreddit hover may-blank'})
        for i in subred:
            return (i.text.strip())
subreddit(doc)


# #### When it was posted (get a TIMESTAMP, e.g. 2016-06-22T12:33:58+00:00, not "4 hours ago")

# In[114]:

def timestamp(my_dict):
    sub = doc.find_all ("p", {'class': 'tagline'})
    for i in sub:
        time_tag = i.find('time')['datetime']
        return time_tag
timestamp(doc)    


# In[26]:

#sub = doc.find_all ("p", {'class': 'tagline'})
#for i in sub:
   # time_tag = i.find('time')['datetime']
    #print(time_tag)


# #### The URL to the post itself

# In[115]:

def url(my_dict):
    url_all = doc.find_all ("p", {'class': 'title'})
    for i in url_all:
        url_tag = i.find('a')['href']
        return url_tag
url(doc)


# In[28]:

#url = doc.find_all ("p", {'class': 'title'})
#for i in url:
    #url_tag = i.find('a')['href']
    #print(url_tag)


# #### The URL of the thumbnail image associated with the post

# In[116]:

def image(my_dict):
    image = doc.find_all("a", {'class': 'thumbnail may-blank '})
    for i in image:
        x = i.find('img')['src']
        return x
image(doc)  


# In[77]:

#image = doc.find_all("a", {'class': 'thumbnail may-blank '})
#for i in image:
    #x = i.find('img')['src']
    #print(x)
    


# ### Creating a CSV

# In[117]:

all_redit = []
# Grab their headlines and bylines
this_story['TITLE']= title(doc)
this_story['Votes'] = votes(doc) 
this_story['Comments']= comments(doc) 
this_story['Subredit'] = subreddit(doc)
this_story['Timestamp'] = timestamp(doc) 
this_story['URL'] = url(doc) 
this_story['URL of Thumbnail'] = image(doc)
all_redit.append(this_story)


# In[118]:

#all_redit


# In[119]:

redit_df = pd.DataFrame(all_redit)
redit_df.head()


# In[120]:

redit_df.to_csv("redit-data.csv")


# In[121]:

import time


# In[122]:

datestring = time.strftime("%Y-%m-%d-%H-%M")
datestring


# In[123]:

now = time.strftime("%B %d, %Y")
now


# In[129]:

filename = "redit-data-" + datestring + ".csv"
my_file = redit_df.to_csv(filename, index=False)


# In[130]:

key = 'key-f5edb244ca7303dc63f079a4cdb97f73'
sandbox = 'sandbox3b984a674a954bcf8c5f2dca397bc3c1.mailgun.org'
recipient = 'radhika.dwaraka@gmail.com'


# In[131]:

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), files=[("attachment", open("my_file"))], data={
    'from': 'hello@example.com',
    'to': recipient,
    'subject': "Reddit This Morning:" + now,
    'text': 'Reddit Updates from My Server'
})
print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))


# In[ ]:



