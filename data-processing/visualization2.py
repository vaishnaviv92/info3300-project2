import csv
import json

data = []
aggregated_data = {} # {taylor swift: {'artist(s)_name': taylor swift, 'in_spotify_playlists': 123, 'in_apple_playlists':23 , 
# 'in_deezer_playlists':11, 'bpm':96, 'danceability_%': 70, 'energy_%':80 }}
keys_to_index = {'artist(s)_name': 1, 'in_spotify_playlists':6, 'in_apple_playlists':9 , 
'in_deezer_playlists':11, 'bpm':14, 'danceability_%': 17, 'energy_%':19 }
with open('../datasets-raw/spotify-2023.csv') as f:
  reader = csv.reader(f)
  for r in reader:
    song = { k: r[keys_to_index[k]] for k in keys_to_index}
    data.append(song)

for d in data:
  artists = d['artist(s)_name'].split(',')
  for artist in artists:
    if artist in aggregated_data.keys():
      aggregated_data[artist].append(d)
    else:
      aggregated_data[artist] = [d]
# print(aggregated_data)

top_artists = {}
n = 0
for artist in aggregated_data.keys():
  if n != 0:
    print(artist)
    n_songs = len(aggregated_data[artist])
    aggregate = {'artist(s)_name': artist, 'in_spotify_playlists': 0, 'in_apple_playlists':0 , 
'in_deezer_playlists': 0, 'bpm': 0, 'danceability_%': 0, 'energy_%': 0 }
    for s in aggregated_data[artist]:
      aggregate['in_spotify_playlists'] += int(s['in_spotify_playlists'].replace(',', ''))
      aggregate['in_apple_playlists'] += int(s['in_apple_playlists'].replace(',', ''))
      aggregate['in_deezer_playlists'] += int(s['in_deezer_playlists'].replace(',', ''))
      aggregate['bpm'] += int(s['bpm'])
      aggregate['danceability_%'] += int(s['danceability_%'])
      aggregate['energy_%'] += int(s['energy_%'])
    aggregate['in_spotify_playlists'] /= n_songs
    aggregate['in_apple_playlists'] /= n_songs
    aggregate['in_deezer_playlists'] /= n_songs
    aggregate['bpm'] /= n_songs
    aggregate['danceability_%'] /= n_songs
    aggregate['energy_%'] /= n_songs 
    top_artists[artist] = aggregate['in_spotify_playlists'] + aggregate['in_apple_playlists'] + aggregate['in_deezer_playlists']
    aggregated_data[artist] = aggregate
  n+=1

ordered = {k: v for k, v in sorted(top_artists.items(), key=lambda item: item[1], reverse=True)}
print(top_artists['Taylor Swift'])
print(top_artists[' Zendaya'])
# top_ten = []
# x = 0
# for a in ordered.keys():
#   if x < 10:
#     print(a)
#     x+=1

      



  

# with open("../json-data/spotify-2023.json", "w") as final:
#     json.dump(data, final)


    

