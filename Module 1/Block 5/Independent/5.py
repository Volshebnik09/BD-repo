import pandas as pd

data = pd.read_csv('movies_metadata.csv')

def has_history_genre(genres):
    try:
        genres_list = eval(genres)
        return any(genre['name'] == 'History' for genre in genres_list)
    except:
        return False

filtered_movies = data[data['genres'].apply(has_history_genre)]

print(filtered_movies[['title', 'genres']])