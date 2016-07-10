
# coding: utf-8

# In[1]:

api_key = ""
api_secret = ""
access_token = ""
token_secret = ""


# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')
import dateutil.parser


# In[3]:

get_ipython().system('pip3 install twython')


# In[4]:

import twython

twitter = twython.Twython(api_key, api_secret, access_token, token_secret)


# In[5]:

status = twitter.get_application_rate_limit_status(resources = ['statuses'])


# In[6]:

#check how many API call is remaining the current window
status = twitter.get_application_rate_limit_status(resources = ['statuses'])
home_status = status['resources']['statuses']['/statuses/home_timeline']
home_status


# In[3]:




# In[ ]:




# In[7]:

response = twitter.search(q="DoSelect",result_type="recent", count=20)


# In[8]:

response


# In[8]:

first = (response['statuses'][0])
first.keys()


# In[9]:

first['text']


# In[10]:

first['user']['screen_name']


# In[11]:

for item in response['statuses']:
    print(item['user']['screen_name'], "-", item['text'])


# In[12]:

response = twitter.search(q="DoSelect",result_type="recent", geo_code="12.935230, 77.694599,1000mi",count=500)


# In[27]:

response


# In[20]:

len(response['statuses'])


# In[13]:

for item in response['statuses']:
    print("https://twitter.com/" + item['user']['screen_name'])


# In[14]:

retweets= twitter.retweeted_of_me(screen_name="DoSelectHQ")
retweets


# In[15]:

mention = twitter.get_mentions_timeline(screen_name="DoSelectHQ")
mention


# In[16]:

response = twitter.search(q="hiring",result_type="recent", geo_code="12.935230, 77.694599,1000mi",count=500)


# In[17]:

for item in response['statuses']:
    print("https://twitter.com/" + item['user']['screen_name'])
    #print()


# In[18]:

response = twitter.get_user_timeline(screen_name="DoSelectHQ", count=300,include_rts=False,exclude_replies=True)


# In[19]:

for item in response:
    print(item['text'])


# In[ ]:

cursor = twitter.cursor(twitter.get_user_timeline, q='"DoSelect" -filter:retweets', count=100)
all_text = list()
for tweet in cursor:
    all_text.append(tweet['text'])
    if len(all_text) > 500:
        break


# In[ ]:

cursor = twitter.cursor(twitter.search, q='"DoSelect" -filter:retweets', count=100)
all_text = list()
for tweet in cursor:
    all_text.append(tweet['text'])
    if len(all_text) > 500:
        break


# In[58]:

from collections import Counter
c = Counter()


# In[ ]:

for item in all_text:
    c.update(item.split())
c.most_common(25)


# In[29]:

first['entities']


# In[30]:

for item in first['entities']['urls']:
    print(item['expanded_url'])


# In[33]:

all_urls = list()
for tweet in cursor:
    print(tweet['entities'])
    for item in tweet['entities']['urls']:
        all_urls.append(item['expanded_url'])

    if len(all_urls) > 100:
        break


# In[34]:

all_urls


# In[35]:

all_media_url = list()

for tweet in cursor:
    if 'media' in tweet['entities']:
        for item in tweet['entities']['media']:
            all_media_url.append(item['media_url'])

    if len(all_urls) > 1000:
        break


# In[36]:

fh = open("preview.html", "w")
for item in all_media_url:
    fh.write('<img src="{}" width="50">'.format(item))
fh.close()


# In[22]:

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import requests


# In[37]:

next_cursor = -1


# In[39]:

response = twitter.get_followers_list(screen_name="DoSelectHQ",count=200,cursor=next_cursor)


# In[41]:

response.keys()


# In[42]:

response['next_cursor']


# In[49]:

response['users'][0]


# In[46]:

list_i = response['users']
matrix = {}
my_list = []
for item in list_i:
    #print(item)

    try:
        #print(item['name'], "-", item['location'],"-", item['time_zone'])
        matrix = {'name': item['name'], 'timezone':item['time_zone']}

        my_list.append(matrix)
        #print(matrix)
        #print(my_list)
    except:
        pass
next_cursor = response["next_cursor"]
print(my_list)


# In[49]:

#for item in my_list:
df = pd.DataFrame.from_records(my_list)
df.head(20)


# In[56]:

df.groupby('timezone').count().plot(kind='bar', label='DoSelect Twitter Followers')


# In[ ]:
