import pandas as pd
music = pd.read_csv("featuresdf.csv")
dance_gen2 = (x for x in music.danceability if x > 0.8)
loud_gen2 = (x for x in music.loudness if x < -5.0)
results = [(a,d) for a,d in zip(dance_gen2, loud_gen2)]
print(results)