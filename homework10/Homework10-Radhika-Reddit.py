
# coding: utf-8

# In[4]:

import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get("https://www.reddit.com/", headers=headers)
doc = BeautifulSoup(response.text, 'html.parser')


# In[5]:

import pandas as pd


# In[6]:

#doc


# #### The title of the post

# In[7]:

def title(my_dict):
    title = doc.find_all("p", { 'class': 'title'})
    for i in title:
        return (i.text.strip())
title(doc)


# #### The number of votes it has (the number between the up and down arrows)

# In[8]:

def votes(my_dict):
    voted = doc.find_all("div", { 'class': 'score unvoted'})
    for i in voted:
        #print(i.text)
        if i.text == "•":
            return 0
        else:
            return (i.text.strip())
votes(doc)


# In[9]:

#### The number of comments it has


# In[10]:

def comments(my_dict):
    comm = doc.find_all("li", { 'class': 'first'})
    for i in comm:
        if i.text == "comment":
            return "no comments"
        else:
            return (i.text.strip())     
comments(doc)


# In[11]:

#comm = doc.find_all("li", { 'class': 'first'})
#for i in comm:
        #if i.text == "comment":
            #print(0)
        #else:
            #print(i.text)


# #### What subreddit it is from (e.g. /r/AskReddit, /r/todayilearned)

# In[12]:

#sub = doc.find_all ("p", {'class': 'tagline'})
#for i in sub:
    #subred = doc.find_all("a", {'class': 'subreddit hover may-blank'})
    #for i in subred:
        #print(i.text)


# In[13]:

def subreddit(my_dict):
    sub = doc.find_all ("p", {'class': 'tagline'})
    for i in sub:
        subred = doc.find_all("a", {'class': 'subreddit hover may-blank'})
        for i in subred:
            return (i.text.strip())
subreddit(doc)


# #### When it was posted (get a TIMESTAMP, e.g. 2016-06-22T12:33:58+00:00, not "4 hours ago")

# In[14]:

def timestamp(my_dict):
    sub = doc.find_all ("p", {'class': 'tagline'})
    for i in sub:
        time_tag = i.find('time')['datetime']
        return time_tag
timestamp(doc)    


# In[15]:

#sub = doc.find_all ("p", {'class': 'tagline'})
#for i in sub:
   # time_tag = i.find('time')['datetime']
    #print(time_tag)


# #### The URL to the post itself

# In[16]:

def url(my_dict):
    url_all = doc.find_all ("p", {'class': 'title'})
    for i in url_all:
        url_tag = i.find('a')['href']
        return url_tag
url(doc)


# In[17]:

#url = doc.find_all ("p", {'class': 'title'})
#for i in url:
    #url_tag = i.find('a')['href']
    #print(url_tag)


# #### The URL of the thumbnail image associated with the post

# In[18]:

def image(my_dict):
    image = doc.find_all("a", {'class': 'thumbnail may-blank '})
    for i in image:
        x = i.find('img')['src']
        return x
image(doc)  


# In[19]:

#image = doc.find_all("a", {'class': 'thumbnail may-blank '})
#for i in image:
    #x = i.find('img')['src']
    #print(x)
    


# ### Creating a CSV

# In[22]:

all_redit = []
this_story = {}
# Grab their headlines and bylines
this_story['TITLE']= title(doc)
this_story['Votes'] = votes(doc) 
this_story['Comments']= comments(doc) 
this_story['Subredit'] = subreddit(doc)
this_story['Timestamp'] = timestamp(doc) 
this_story['URL'] = url(doc) 
this_story['URL of Thumbnail'] = image(doc)
all_redit.append(this_story)


# In[24]:

#all_redit


# In[ ]:

redit_df = pd.DataFrame(all_redit)
redit_df.head()


# In[ ]:

redit_df.to_csv("redit-data.csv")


# In[ ]:

import time


# In[ ]:

datestring = time.strftime("%Y-%m-%d-%H-%M")
datestring


# In[ ]:

now = time.strftime("%B %d, %Y")
now


# In[ ]:

filename = "redit-data-" + datestring + ".csv"
my_file = redit_df.to_csv(filename, index=False)


# In[ ]:

key = 'key-f5edb244ca7303dc63f079a4cdb97f73'
sandbox = 'sandbox3b984a674a954bcf8c5f2dca397bc3c1.mailgun.org'
recipient = 'radhika.dwaraka@gmail.com'


# In[27]:

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), files=[("attachment", open("my_file"))], data={
    'from': 'radhika.dwaraka@gmail.com',
    'to': recipient,
    'subject': "Reddit This Morning:" + now,
    'text': 'Reddit Updates from My Server',
})
print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))


# In[ ]:



