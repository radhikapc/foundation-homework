#Make a non-IPython Notebook that automates browsing for top tracks
#Prompts for an artist you put it in, displays the results, asks which one you want (numbered)
#you enter a number It displays their top tracks, then their MOST popular album
#and their least popular album. if they only have one album it says that they only have one album.

enter_artist= input("Enter an artist: ")
print("You selected", enter_artist)

import requests
response = requests.get('https://api.spotify.com/v1/search?query='+enter_artist+'&type=artist')
data = response.json()
data
#below code prints out all the artists and IDs whose name has the string that you entered.
id_dict = {}
num_artists = data['artists']['items']
for i in num_artists:
    #print(i['id'], i['name'])
    id_dict.update({i['name']: i['id']})
#print(id_dict)

# Names and IDs are printed out to the user.
num_artists = data['artists']['items']
test_dict = {}
count = 0
for artist in num_artists:
    if enter_artist in artist['name']:
        count = count+1
        #artist_id = artist['id']
        #print(artist_id, artist['name'])
        test_dict.update({count: artist['name']})
print("These are the artists listed:", test_dict)

# displays the selection to the user
enter_num= input("From the above list, enter the number corresponding to the artist you are searching for: ")
artist_chose = test_dict[int(enter_num)]
artist_chose_id = id_dict[artist_chose]
print("You selected", enter_num, "corresponding to", artist_chose,"with ID", artist_chose_id)

# top tracks of the artist the user selected.
id_response = requests.get('https://api.spotify.com/v1/artists/'+artist_chose_id+'/top-tracks?country=US')
id_data = id_response.json()
id_loop = id_data['tracks']
#print(id_loop)
print("The top tracks of", artist_chose, "are:")
for i in id_loop:
    print("-",i['name'])


#code for selecting albums

response = requests.get('https://api.spotify.com/v1/artists/'+artist_chose_id+'/albums?')
data = response.json()

album_dict = {}
x= data['items']
#print(x)
for item in x:
    album_dict.update({item['name']: item['id']})

#print(album_dict)

#finding most popular album and least popular

most_pop = {}
x= data['items']
#print(x)
for item in x:
    #['external_urls', 'album_type', 'name', 'href', 'uri', 'images', 'type', 'available_markets', 'id'
    # print(item['name'])
    album_id = item['id']
    album_name = item['name']
    response = requests.get("https://api.spotify.com/v1/albums/"+album_id+"?")
    alb_data = response.json()
    alb_pop = alb_data['popularity']
    #print("Popularity of", album_name, "is", alb_pop)
    most_pop.update({album_name: alb_pop})
#print(most_pop)
#print(type(most_pop))
#print(len(most_pop))

# printing out the most and least to the user
if (len(most_pop)) == 1:
    print(artist_chose, "has only one album to his credit!")
print("The most popular Album of", artist_chose, "is", max(most_pop, key=lambda i: most_pop[i]))
print("The least popular Album of", artist_chose, "is", min(most_pop, key=lambda i: most_pop[i]))
