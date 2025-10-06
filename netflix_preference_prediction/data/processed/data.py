import pandas as pd
import numpy as np
import random

# Sample pools for random selection
directors = ["John Lasseter", "Joe Johnston", "Howard Deutch", "John Landis", "Chris Columbus", "Steven Spielberg", "James Cameron", "Quentin Tarantino"]
actors = ["Tom Hanks", "Tim Allen", "Robin Williams", "Kirsten Dunst", "Mel Gibson", "Goldie Hawn", "Dan Aykroyd", "John Belushi", "Macaulay Culkin", "Joe Pesci"]
languages = ["English", "Hindi", "Spanish", "French", "German", "Japanese"]
countries = ["USA", "India", "UK", "France", "Germany", "Canada"]

# Generate synthetic data
num_movies = 3952
data = {
    "movie_id": list(range(1, num_movies + 1)),
    "imdb_rating": np.round(np.random.uniform(4.0, 9.5, num_movies), 1),
    "imdb_votes": np.random.randint(1000, 1000000, num_movies),
    "director": [random.choice(directors) for _ in range(num_movies)],
    "main_cast": [f"{random.choice(actors)}|{random.choice(actors)}" for _ in range(num_movies)],
    "runtime": np.random.randint(80, 180, num_movies),
    "language": [random.choice(languages) for _ in range(num_movies)],
    "country": [random.choice(countries) for _ in range(num_movies)],
}

df = pd.DataFrame(data)
df.to_csv("synthetic_movies.csv", index=False)
