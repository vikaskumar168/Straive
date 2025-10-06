# # import os
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# #
# # # Create outputs directories if they don't exist
# # os.makedirs('outputs/figures', exist_ok=True)
# # os.makedirs('../data/processed', exist_ok=True)
# #
# # # Paths to raw .dat files
# # ratings_path = '../data/raw/ratings.dat'
# # movies_path = '../data/raw/movies.dat'
# # users_path = '../data/raw/users.dat'  # optional, for user info
# #
# # # Load ratings (MovieLens 1M format: userID::movieID::rating::timestamp)
# # ratings = pd.read_csv(ratings_path, sep='::', engine='python',
# #                       names=['user_id', 'movie_id', 'rating', 'timestamp'])
# # print(f"Ratings shape: {ratings.shape}")
# # print(ratings.head())
# #
# # # Load movies (movieID::title::genres)
# # movies = pd.read_csv(movies_path, sep='::', engine='python',
# #                      names=['movie_id', 'title', 'genres'], encoding='ISO-8859-1')
# # print(f"Movies shape: {movies.shape}")
# # print(movies.head())
# #
# # # Optional: load users if needed (userID::gender::age::occupation::zip)
# # users = pd.read_csv(users_path, sep='::', engine='python',
# #                     names=['user_id', 'gender', 'age', 'occupation', 'zip_code'], encoding='ISO-8859-1')
# # print(f"Users shape: {users.shape}")
# # print(users.head())
# #
# # # Check missing values
# # print("Missing values in ratings:\n", ratings.isnull().sum())
# # print("Missing values in movies:\n", movies.isnull().sum())
# # print("Missing values in users:\n", users.isnull().sum())
# #
# # # Rating distribution
# # # print("Plotting rating distribution...")
# # # plt.figure(figsize=(8,5))
# # # sns.countplot(ratings['rating'])
# # # plt.title("Rating distribution")
# # # plt.show()
# # # print("Rating distribution plot done.")
# # #
# # # # Number of ratings per movie
# # # print("Plotting number of ratings per movie...")
# # # plt.figure(figsize=(8,5))
# # # movie_counts = ratings['movie_id'].value_counts()
# # # plt.hist(movie_counts, bins=50)
# # # plt.title("Number of ratings per movie")
# # # plt.xlabel("Number of ratings")
# # # plt.ylabel("Number of movies")
# # # plt.savefig('outputs/figures/ratings_per_movie.png')
# # # plt.close()
# # # print("Number of ratings per movie plot saved.")
# # #
# # # # Number of ratings per user
# # # print("Plotting number of ratings per user...")
# # # plt.figure(figsize=(8,5))
# # # user_counts = ratings['user_id'].value_counts()
# # # plt.hist(user_counts, bins=50)
# # # plt.title("Number of ratings per user")
# # # plt.xlabel("Number of ratings")
# # # plt.ylabel("Number of users")
# # # plt.savefig('outputs/figures/ratings_per_user.png')
# # # plt.close()
# # # print("Number of ratings per user plot saved.")
# # #
# # # # Explore genres (split pipe-separated genres)
# # # if 'genres' in movies.columns:
# # #     print("Plotting genre counts...")
# # #     genre_counts = movies['genres'].str.split('|').explode().value_counts()
# # #     plt.figure(figsize=(12,6))
# # #     sns.barplot(x=genre_counts.index, y=genre_counts.values)
# # #     plt.title("Genre counts")
# # #     plt.xticks(rotation=45)
# # #     plt.savefig('outputs/figures/genre_counts.png')
# # #     plt.close()
# # #     print("Genre counts plot saved.")
# #
# # # Remove duplicates if any
# # print("Dropping duplicates if any...")
# # ratings.drop_duplicates(inplace=True)
# # movies.drop_duplicates(inplace=True)
# # users.drop_duplicates(inplace=True)
# # print("Duplicates removed.")
# #
# # # Save cleaned csv files to processed folder
# # print("Saving cleaned CSV files...")
# # ratings.to_csv('../data/processed/ratings_clean.csv', index=False)
# # movies.to_csv('../data/processed/movies_clean.csv', index=False)
# # users.to_csv('../data/processed/users_clean.csv', index=False)
# # print("Cleaned CSV files saved.")
#
#
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # Create outputs directories if they don't exist
# os.makedirs('outputs/figures', exist_ok=True)
# os.makedirs('../data/processed', exist_ok=True)
#
# # Paths to raw .dat files
# ratings_path = '../data/raw/ratings.dat'
# movies_path = '../data/raw/movies.dat'
# users_path = '../data/raw/users.dat'  # optional, for user info
#
# # Load ratings (MovieLens 1M format: userID::movieID::rating::timestamp)
# ratings = pd.read_csv(ratings_path, sep='::', engine='python',
#                       names=['user_id', 'movie_id', 'rating', 'timestamp'])
# print(f"Ratings shape: {ratings.shape}")
# print(ratings.head())
#
# # Load movies (movieID::title::genres)
# movies = pd.read_csv(movies_path, sep='::', engine='python',
#                      names=['movie_id', 'title', 'genres'], encoding='ISO-8859-1')
# print(f"Movies shape: {movies.shape}")
# print(movies.head())
#
# # Optional: load users if needed (userID::gender::age::occupation::zip)
# users = pd.read_csv(users_path, sep='::', engine='python',
#                     names=['user_id', 'gender', 'age', 'occupation', 'zip_code'], encoding='ISO-8859-1')
# print(f"Users shape: {users.shape}")
# print(users.head())
#
# # Check missing values
# print("Missing values in ratings:\n", ratings.isnull().sum())
# print("Missing values in movies:\n", movies.isnull().sum())
# print("Missing values in users:\n", users.isnull().sum())
#
# # Rating distribution
# print("Plotting rating distribution...")
# plt.figure(figsize=(8,5))
# sns.countplot(ratings['rating'])
# plt.title("Rating distribution")
# plt.show()
# print("Rating distribution plot done.")
#
# # Number of ratings per movie
# print("Plotting number of ratings per movie...")
# plt.figure(figsize=(8,5))
# movie_counts = ratings['movie_id'].value_counts()
# plt.hist(movie_counts, bins=50)
# plt.title("Number of ratings per movie")
# plt.xlabel("Number of ratings")
# plt.ylabel("Number of movies")
# plt.savefig('outputs/figures/ratings_per_movie.png')
# plt.close()
# print("Number of ratings per movie plot saved.")
#
# # Number of ratings per user
# print("Plotting number of ratings per user...")
# plt.figure(figsize=(8,5))
# user_counts = ratings['user_id'].value_counts()
# plt.hist(user_counts, bins=50)
# plt.title("Number of ratings per user")
# plt.xlabel("Number of ratings")
# plt.ylabel("Number of users")
# plt.savefig('outputs/figures/ratings_per_user.png')
# plt.close()
# print("Number of ratings per user plot saved.")
#
# # Explore genres (split pipe-separated genres)
# if 'genres' in movies.columns:
#     print("Plotting genre counts...")
#     genre_counts = movies['genres'].str.split('|').explode().value_counts()
#     plt.figure(figsize=(12,6))
#     sns.barplot(x=genre_counts.index, y=genre_counts.values)
#     plt.title("Genre counts")
#     plt.xticks(rotation=45)
#     plt.savefig('outputs/figures/genre_counts.png')
#     plt.close()
#     print("Genre counts plot saved.")
#
# # Remove duplicates if any
# print("Dropping duplicates if any...")
# ratings.drop_duplicates(inplace=True)
# movies.drop_duplicates(inplace=True)
# users.drop_duplicates(inplace=True)
# print("Duplicates removed.")
#
# # Save cleaned csv files to processed folder
# print("Saving cleaned CSV files...")
# ratings.to_csv('../data/processed/ratings_clean.csv', index=False)
# movies.to_csv('../data/processed/movies_clean.csv', index=False)
# users.to_csv('../data/processed/users_clean.csv', index=False)
# print("Cleaned CSV files saved.")
#
# # Note: If plots still don’t display and you're running from a terminal or script,
# # it’s normal that plt.show() might not open a window, especially on servers or headless systems.
# # In such cases, rely on saved plot images instead.
#


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create outputs directories if they don't exist
os.makedirs('outputs/figures', exist_ok=True)
os.makedirs('../data/processed', exist_ok=True)

# Paths to your raw data files
titles_basics_path = '../data/raw/title.basics.tsv'
titles_crew_path = '../data/raw/title.crew.tsv'
titles_ratings_path = '../data/raw/title.ratings.tsv'
ratings_path = '../data/raw/u.data'
users_path = '../data/raw/u.user'

# Load movie basic info
print("Loading title.basics.tsv...")
movies_basics = pd.read_csv(titles_basics_path, sep='\t', na_values='\\N')
print(f"Movies basics shape: {movies_basics.shape}")

# Load crew info
print("Loading title.crew.tsv...")
movies_crew = pd.read_csv(titles_crew_path, sep='\t', na_values='\\N')
print(f"Movies crew shape: {movies_crew.shape}")

# Load ratings info
print("Loading title.ratings.tsv...")
movies_ratings = pd.read_csv(titles_ratings_path, sep='\t', na_values='\\N')
print(f"Movies ratings shape: {movies_ratings.shape}")

# Merge movies data on 'tconst'
print("Merging movie datasets...")
movies = movies_basics.merge(movies_crew, on='tconst', how='left').merge(movies_ratings, on='tconst', how='left')

# Select relevant columns and rename for clarity
movies = movies[['tconst', 'primaryTitle', 'titleType', 'startYear', 'runtimeMinutes', 'genres', 'directors', 'averageRating', 'numVotes']]
movies.rename(columns={
    'tconst': 'movie_id',
    'primaryTitle': 'title',
    'startYear': 'year',
    'runtimeMinutes': 'duration',
    'averageRating': 'avg_rating',
    'numVotes': 'num_votes'
}, inplace=True)

# Convert numeric columns (handle missing)
movies['year'] = pd.to_numeric(movies['year'], errors='coerce')
movies['duration'] = pd.to_numeric(movies['duration'], errors='coerce')
movies['avg_rating'] = pd.to_numeric(movies['avg_rating'], errors='coerce')
movies['num_votes'] = pd.to_numeric(movies['num_votes'], errors='coerce')

print(f"Movies final shape: {movies.shape}")
print(movies.head())

# Load ratings data (u.data)
print("Loading ratings data (u.data)...")
ratings = pd.read_csv(ratings_path, sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
print(f"Ratings shape: {ratings.shape}")
print(ratings.head())

# Load users data (u.user)
print("Loading users data (u.user)...")
users = pd.read_csv(users_path, sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
print(f"Users shape: {users.shape}")
print(users.head())

# Check for missing values
print("Missing values in movies:\n", movies.isnull().sum())
print("Missing values in ratings:\n", ratings.isnull().sum())
print("Missing values in users:\n", users.isnull().sum())

# Remove duplicates if any
print("Dropping duplicates if any...")
movies.drop_duplicates(inplace=True)
ratings.drop_duplicates(inplace=True)
users.drop_duplicates(inplace=True)

# Save cleaned CSV files to processed folder with new names
print("Saving cleaned CSV files with new names...")
movies.to_csv('../data/processed/newmovies.csv', index=False)
ratings.to_csv('../data/processed/newratings.csv', index=False)
users.to_csv('../data/processed/newusers.csv', index=False)
print("Cleaned CSV files saved as newmovies.csv, newratings.csv, newusers.csv")

# Optional: plot rating distribution
print("Plotting rating distribution...")
plt.figure(figsize=(8,5))
sns.countplot(ratings['rating'])
plt.title("Rating distribution")
plt.savefig('outputs/figures/rating_distribution.png')
plt.close()
print("Rating distribution plot saved.")

# Optional: plot genre counts
if 'genres' in movies.columns:
    print("Plotting genre counts...")
    genre_counts = movies['genres'].dropna().str.split(',').explode().value_counts()
    plt.figure(figsize=(12,6))
    sns.barplot(x=genre_counts.index, y=genre_counts.values)
    plt.title("Genre counts")
    plt.xticks(rotation=45)
    plt.savefig('outputs/figures/genre_counts.png')
    plt.close()
    print("Genre counts plot saved.")
