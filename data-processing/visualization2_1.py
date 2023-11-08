import csv
import json

data = []
aggregated_data = {} # {taylor swift: {'artist(s)_name': taylor swift, 'in_spotify_playlists': 123, 'in_apple_playlists':23 , 
# 'in_deezer_playlists':11, 'bpm':96, 'danceability_%': 70, 'energy_%':80 }}
keys_to_index = {'artist(s)_name': 1, 'streams':8, 'bpm':14, 'danceability_%': 17, 'energy_%':19 }
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

streams = {}
n = 0
for artist in aggregated_data.keys():
  if n != 0:
    n_songs = len(aggregated_data[artist])
    aggregate = {'artist(s)_name': artist, 'streams': 0, 'bpm': 0, 'danceability_%': 0, 'energy_%': 0 }
    for s in aggregated_data[artist]:
      aggregate['streams'] += int(s['streams'].replace(',', ''))
      aggregate['bpm'] += int(s['bpm'])
      aggregate['danceability_%'] += int(s['danceability_%'])
      aggregate['energy_%'] += int(s['energy_%'])
    aggregate['bpm'] /= n_songs
    aggregate['danceability_%'] /= n_songs
    aggregate['energy_%'] /= n_songs 
    aggregated_data[artist] = aggregate
    streams[artist] = aggregate['streams']
  n+=1

descending = dict(sorted(streams.items(), key = lambda x: x[1], reverse = True))
top_streamed = {}
n = 0
for i in descending.keys():
  if (n < 10):
    top_streamed[i] = aggregated_data[i]
    n+=1

with open("../json-data/spotify-2023.json", "w") as final:
    json.dump(top_streamed, final, indent = 2)


    

