import pandas as pd

data = pd.read_csv('movies_metadata.csv')

data = data.dropna(subset=['runtime'])

sorted_movies = data.sort_values(by='runtime')

print(sorted_movies[['title', 'runtime']])