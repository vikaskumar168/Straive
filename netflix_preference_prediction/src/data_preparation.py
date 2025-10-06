import os
from src.utils import load_csv, save_csv, ensure_dir
import pandas as pd
from sklearn.impute import SimpleImputer

def prepare_data(raw_ratings_path, raw_movies_path, external_meta_path=None, output_path="data/processed/"):
    print("Step 1: Ensuring outputs directory exists...")
    ensure_dir(output_path)

    print(f"Step 2: Loading raw ratings data from {raw_ratings_path}...")
    ratings = load_csv(raw_ratings_path)
    print(f"Loaded ratings: {ratings.shape[0]} rows, {ratings.shape[1]} columns.")

    print(f"Step 3: Loading raw movies data from {raw_movies_path}...")
    movies = load_csv(raw_movies_path)
    print(f"Loaded movies: {movies.shape[0]} rows, {movies.shape[1]} columns.")

    if external_meta_path:
        print(f"Step 4: Loading external metadata from {external_meta_path}...")
        external = load_csv(external_meta_path)
        print(f"Loaded external metadata: {external.shape[0]} rows, {external.shape[1]} columns.")
        print("Merging external metadata with movies data...")
        movies = movies.merge(external, how="left", on="movie_id")
        print(f"Movies after merge: {movies.shape[0]} rows, {movies.shape[1]} columns.")

    print("Step 5: Handling missing values in numeric columns...")
    num_cols = movies.select_dtypes(include='number').columns.tolist()
    print(f"Numeric columns to impute: {num_cols}")
    imputer = SimpleImputer(strategy="median")
    movies[num_cols] = imputer.fit_transform(movies[num_cols])
    print("Missing numeric values imputed with median.")

    print("Step 6: Filling missing categorical/string fields...")
    cat_cols = movies.select_dtypes(include='object').columns.tolist()
    print(f"Categorical columns to fill: {cat_cols}")
    for c in cat_cols:
        missing_before = movies[c].isna().sum()
        movies[c] = movies[c].fillna("Unknown")
        missing_after = movies[c].isna().sum()
        print(f"Filled '{c}': missing before={missing_before}, missing after={missing_after}")

    print("Step 7: Merging ratings and movies data...")
    df = ratings.merge(movies, how="left", on="movie_id")
    print(f"Merged dataset shape: {df.shape}")

    output_file = os.path.join(output_path, "full_merged.csv")
    print(f"Step 8: Saving processed data to {output_file}...")
    save_csv(df, output_file)
    print("Data preparation complete.")

    return df
