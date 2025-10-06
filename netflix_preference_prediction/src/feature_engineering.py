import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.decomposition import TruncatedSVD

def engineer_features(df, output_path="data/processed/"):
    print("Starting feature engineering...")

    # 1. Encode genre
    print("Encoding genres...")
    mlb = MultiLabelBinarizer()
    genre_matrix = mlb.fit_transform(df['genres'].str.split('|'))
    genre_df = pd.DataFrame(genre_matrix, columns=[f"genre_{g}" for g in mlb.classes_])
    df = pd.concat([df.reset_index(drop=True), genre_df.reset_index(drop=True)], axis=1)
    print(f"Genres encoded: {genre_df.shape[1]} new columns added")

    # 2. Normalize numeric features
    print("Scaling numeric features...")
    num_feats = ['imdb_rating', 'rating']
    existing_num_feats = [col for col in num_feats if col in df.columns]
    print(f"Numeric features to scale: {existing_num_feats}")
    if existing_num_feats:
        scaler = StandardScaler()
        df[existing_num_feats] = scaler.fit_transform(df[existing_num_feats])
        print("Numeric features scaled.")
    else:
        print("No numeric features found to scale.")

    # 3. Create user-level aggregated features
    print("Creating user-level aggregated features...")
    user_grp = df.groupby('user_id')
    df_user = user_grp['rating'].agg(['mean', 'count']).rename(
        columns={'mean': 'user_avg_rating', 'count': 'user_rating_count'})
    df = df.merge(df_user, how='left', on='user_id')
    print("User-level features added.")

    # 4. Movie-level aggregated features
    print("Creating movie-level aggregated features...")
    movie_grp = df.groupby('movie_id')
    df_movie = movie_grp['rating'].agg(['mean', 'count']).rename(
        columns={'mean': 'movie_avg_rating', 'count': 'movie_rating_count'})
    df = df.merge(df_movie, how='left', on='movie_id')
    print("Movie-level features added.")

    # 5. Favorite genre per user
    print("Calculating user's favorite genre...")
    genre_cols = [col for col in df.columns if col.startswith('genre_')]
    user_genre_matrix = df[['user_id'] + genre_cols]
    user_genre_sum = user_genre_matrix.groupby('user_id').sum()
    user_fav_genre = user_genre_sum.idxmax(axis=1).rename("user_fav_genre")
    df = df.merge(user_fav_genre, on='user_id', how='left')
    df = pd.get_dummies(df, columns=['user_fav_genre'], prefix='fav_genre')
    print("User favorite genre feature added.")

    # # 6. Time-of-day features (if timestamp exists)
    # if 'timestamp' in df.columns:
    #     print("Extracting time-of-day features...")
    #     df['hour'] = pd.to_datetime(df['timestamp'], unit='s').dt.hour
    #     df['time_of_day'] = pd.cut(df['hour'], bins=[0, 6, 12, 18, 24],
    #                                labels=['Night', 'Morning', 'Afternoon', 'Evening'], right=False)
    #     df = pd.get_dummies(df, columns=['time_of_day'], prefix='watch_time')
    #     print("Time-of-day features added.")

    # 7. User × Genre interaction features
    print("Creating user-genre interaction features...")
    for genre in genre_cols:
        df[f"user_genre_pref_{genre}"] = df[genre] * df['user_avg_rating']
    print("User-genre interaction features added.")

    # 8. Dimensionality reduction (optional)
    print("Applying dimensionality reduction to genre features...")
    svd = TruncatedSVD(n_components=5, random_state=42)
    genre_reduced = svd.fit_transform(df[genre_cols])
    genre_reduced_df = pd.DataFrame(genre_reduced, columns=[f"genre_svd_{i}" for i in range(5)])
    df = pd.concat([df.drop(columns=genre_cols), genre_reduced_df], axis=1)
    print("Genre dimensionality reduced.")

    # Save final feature file
    print(f"Saving features file to {output_path}features_all.csv")
    df.to_csv(output_path + "features_all.csv", index=False)
    print("Feature engineering completed and file saved.")
    return df
