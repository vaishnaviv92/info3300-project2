import pandas as pd

df = pd.read_json("../json-data/vis1-data.json")

result = df.groupby('year')[['bpm', 'nrgy', 'dnce']].mean().reset_index()

output_json = '../json-data/vis2-grouped-data.json'
result.to_json(output_json, orient='records')

print("Data saved to", output_json)