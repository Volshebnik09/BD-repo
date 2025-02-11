import pandas as pd

data = pd.read_csv('movies_metadata.csv')

filtered_movies = data[pd.to_datetime(data['release_date']) > '1995-09-01']

print(filtered_movies[['title', 'release_date']])