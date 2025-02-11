import pandas as pd

data = pd.read_csv('movies_metadata.csv')

data = data.dropna(subset=['vote_count'])

threshold = data['vote_count'].max() * 0.5

filtered_movies = data[data['vote_count'] > threshold]

print(filtered_movies[['title', 'vote_count']])