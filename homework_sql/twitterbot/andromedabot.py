
# coding: utf-8

# In[5]:

api_key = "POfOwij2GkfMu5xvHpDwIIAhy"
api_secret = "JT1d2ILd4SnuSMvdI2A4yMeufMiEwFvwiPuTRLGfyHk8IH0uEh"


# In[2]:

get_ipython().system('pip3 install twython')


# In[7]:

twitter = twython.Twython(api_key, api_secret)
auth = twitter.get_authentication_tokens()
print("Log into Twitter as the user you want to authorize and visit this URL:")
print("\t" + auth['auth_url'])


# In[8]:


pin = "0494636"

twitter = twython.Twython(api_key, api_secret, auth['oauth_token'], auth['oauth_token_secret'])
tokens = twitter.get_authorized_tokens(pin)

new_access_token = tokens['oauth_token']
new_token_secret = tokens['oauth_token_secret']
print("your access token:", new_access_token)
print("your token secret:", new_token_secret)


# In[9]:

twitter = twython.Twython(api_key, api_secret, new_access_token, new_token_secret)


# In[10]:

twitter.update_status(status="hi there, I am testing my cute little Twitter Bot, how's it going :-)")


# In[48]:

# setting up the Planet Database on Postgres
import pg8000

lakes = []

conn = pg8000.connect(user='postgres', password='password', database='andromedabot')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE solarsystem (
   name varchar(80),
   radius varchar(80),
   art_distance varchar(80),
   distance varchar(80),
   flattening varchar(80),
   tilt varchar(80),
   tilt_x varchar(80),
   tilt_y varchar(80),
   tilt_z varchar(80),
   rotperiod varchar(80),
   eccentricity varchar(80),
   orbitperiod varchar(80),
   texture varchar(80),
   color varchar(80)

)
""")
conn.commit()


# In[51]:

conn.rollback()


# In[49]:

cursor.execute("COPY solarsystem(name,radius,art_distance,distance,flattening,tilt,tilt_x,tilt_y,tilt_z,rotperiod,eccentricity,orbitperiod,texture,color) FROM '/Users/Radhika/Downloads/planets.csv' DELIMITER ',' CSV")
conn.commit()


# In[52]:

import pg8000

solar_sys = []

conn = pg8000.connect(user='postgres', password='password', database='andromedabot')
cursor = conn.cursor()
cursor.execute("SELECT name, radius, distance, tilt, rotperiod, orbitperiod FROM solarsystem")
for row in cursor.fetchall():
    solar = {'name': row[0], 'radius':row[1], 'distance': row[2], 'tilt': row[3], 'rotperiod': row[4], 'orbitperiod': row[5]}
    solar_sys.append(solar)
len(solar)


# In[53]:

sentences = {
    'radius': 'The radius of Planet {} is {} kilometers.',
    'distance': 'The distance of Planet {} from Sun is {} kilometers.',
    'tilt': 'The tilt angle to orbit plane of Planet {} is {} degrees.',
    'rotperiod': 'The rotation period of Planet {} is {} days.',
    'orbitperiod': 'The orbital period of Planet {} is {} days.'
    
}


# In[70]:

import random
def random_planet_sentence(solar_sys, sentences):
    planet = random.choice(solar_sys)
    possible_keys = [k for k, v in planet.items() if k != 'name']
    col = random.choice(possible_keys)
    sentence_template = sentences[col]
    output = sentence_template.format(planet['name'], planet[col])
    return output
    
for i in range(10):
    print(random_planet_sentence(solar_sys, sentences))


# In[115]:

flare = ["Wow!", "Cool, huh?", "Now you know.", "See!", "Neat-o!!"]
output = random_planet_sentence(solar_sys, sentences) + " " + random.choice(flare)
twitter.update_status(status=output)


# In[ ]:




# In[ ]:



