import pandas as pd

data = pd.read_csv('movies_metadata.csv')

filtered_movies = data[data['revenue'] > 100000000]

print(filtered_movies[['title', 'revenue']])