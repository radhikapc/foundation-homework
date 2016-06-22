
# coding: utf-8

# ### APIs/Data Structures
# 
# #### Forecasts Part One: Getting data
# 
# Using the Dark Sky Forecast API at https://developer.forecast.io/, generate a sentence that describes the weather that day.
# 
# Right now it is TEMPERATURE degrees out and SUMMARY. Today will be TEMP_FEELING with a high of HIGH_TEMP and a low of LOW_TEMP. RAIN_WARNING.

# In[1]:

import requests


# In[5]:

import dateutil.parser
import datetime


# In[2]:

response = requests.get('https://api.forecast.io/forecast/4da699cf85f9706ce50848a7e59591b7/40.712784,-74.005941')
data = response.json()


# In[54]:

#data


# In[55]:

#data.keys()


# In[56]:

#data_list = data['daily']['data']

#for i in data_list:
    #print(i)


# In[57]:

#data['currently']['temperature']


# In[43]:

def temp(my_dict):
    temperature = my_dict['currently']['temperature']
    temper = str(temperature)
    return temper

temp(data)


# In[18]:

def summ(my_dict):
    summary = my_dict['currently']['summary']
    l = summary.lower()
    return l

summ(data)


# In[44]:

def high_temp(my_dict):
    TempMax = data['daily']['data']
    for i in TempMax:
        h_temp = str(i['temperatureMax'])
        return h_temp
high_temp(data)


# In[20]:

def temp_feel(my_dict):
    TemMax = data['daily']['data']
    for i in TemMax:
        hi_temp = i['temperatureMax']
        if hi_temp > 80:
            return "high"
        if hi_temp > 70:
            return "moderate"
        if hi_temp > 50:
            return "warm"
        if hi_temp > 30:
            return "cool"
        if hi_temp < 30:
            return "cold"
temp_feel(data)


# In[45]:

def low_temp(my_dict):
    TempMin = data['daily']['data']
    for i in TempMin:
        l_temp = str(i['temperatureMin'])
        return l_temp
low_temp(data)


# In[52]:

def rain_warning(my_dict):
    data_list = data['daily']['data']

    for i in data_list:
        rain_prob = float(i['precipIntensity'])
        #print(type(rain_prob))
        if rain_prob > 0.002:
            return "Very light rain!"
        if rain_prob > 0.017:
            return "Light rain, you may bring your umbrella"
        if rain_prob > 0.1:
            return "Moderate rain, you need an umbrella!"
        if rain_prob > 0.4:
            return "Heavy rain, don't miss your umbrella"
rain_warning(data)


# In[53]:

def eq_to_sentence(my_dict):
    return "Right now it is " + temp(my_dict) + " degrees out and " + summ(my_dict) + ". Today will be " + temp_feel(my_dict) + " with a high temperature of " + high_temp(my_dict) + " and a low temperature of " + low_temp(my_dict) + "." + rain_warning(my_dict)
eq_to_sentence(data)


# In[58]:

import requests


# In[59]:

key = 'key-'
sandbox = 'sandbox3b984a674a954bcf8c5f2dca397bc3c1.mailgun.org'
recipient = 'radhika.dwaraka@gmail.com'


# In[68]:

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'hello@example.com',
    'to': recipient,
    'subject': 'Hello',
    'text': 'Hello from My Server'
})
print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))


# In[69]:

request_url = 'https://api.mailgun.net/v2/{0}/events'.format(sandbox)
request = requests.get(request_url, auth=('api', key), params={'limit': 5})

print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))


# In[ ]:



