# from src.data_preparation import prepare_data
# from src.feature_engineering import engineer_features
# from src.model_training import split_data, train_models
# from src.model_evaluation import evaluate_model
# import os
#
#
# def main():
#     print("Starting main pipeline...")
#
#     # Paths (adjust as needed)
#     raw_ratings = "data/processed/ratings_clean.csv"
#     raw_movies = "data/processed/movies_clean.csv"
#     external_meta = "data/external/imdb_meta.csv"  # optional
#
#     # Step 1: Prepare / clean data
#     print("Step 1: Preparing and cleaning data...")
#     df = prepare_data(raw_ratings, raw_movies, external_meta, output_path="data/processed/")
#     print(f"Data prepared: {df.shape[0]} rows, {df.shape[1]} columns")
#
#     # Step 2: Feature engineering
#     print("Step 2: Engineering features...")
#     df_feat = engineer_features(df, output_path="data/processed/")
#     print(f"Feature engineered data shape: {df_feat.shape}")
#
#     # Create binary target variable 'like_dislike'
#     print("Creating binary target 'like_dislike' from ratings...")
#     df_feat['like_dislike'] = (df_feat['rating'] >= 4).astype(int)
#     print(f"Target variable 'like_dislike' distribution:\n{df_feat['like_dislike'].value_counts()}")
#
#     # Step 3: Split data
#     print("Step 3: Splitting data into train, validation, and test sets...")
#     train, val, test = split_data(df_feat, test_size=0.2, val_size=0.1)
#     print(f"Train set shape: {train.shape}")
#     print(f"Validation set shape: {val.shape}")
#     print(f"Test set shape: {test.shape}")
#
#     # Choose feature columns & target
#     all_cols = df_feat.columns.tolist()
#     # Exclude non-feature columns
#     non_features = ['user_id', 'movie_id', 'like_dislike', 'rating', 'genres', 'timestamp']  # adapt if needed
#     feature_cols = [c for c in all_cols if c not in non_features]
#     target_col = 'like_dislike'
#
#     print(f"Using {len(feature_cols)} feature columns for model training")
#
#     # Step 4: Train models
#     print("Step 4: Training models...")
#     if not os.path.exists("models/"):
#         os.makedirs("models/")
#     train_models(train, val, feature_cols, target_col, models_output_dir="models/")
#     print("Model training complete.")
#
#     # Step 5: Evaluate on test set
#     print("\n--- Test set evaluation ---")
#     for model_fn in ["models/rf_model.pkl", "models/xgb_model.pkl"]:
#         print(f"Evaluating model: {model_fn}")
#         evaluate_model(model_fn, test, feature_cols, target_col)
#
#
# if __name__ == "__main__":
#     main()



import os
from src.data_preparation import prepare_data
from src.feature_engineering import engineer_features
from src.model_training import split_data, train_models
from src.model_evaluation import evaluate_model

def main():
    print("Starting main pipeline...")

    # Paths (adjust as needed)
    raw_ratings = "data/processed/ratings_clean.csv"
    raw_movies = "data/processed/movies_clean.csv"
    external_meta = "data/external/imdb_meta.csv"  # optional

    # Step 1: Prepare / clean data
    print("Step 1: Preparing and cleaning data...")
    df = prepare_data(raw_ratings, raw_movies, external_meta, output_path="data/processed/")
    print(f"Data prepared: {df.shape[0]} rows, {df.shape[1]} columns")

    # Step 2: Feature engineering
    print("Step 2: Engineering features...")
    df_feat = engineer_features(df, output_path="data/processed/")
    print(f"Feature engineered data shape: {df_feat.shape}")

    # Create binary target
    print("Creating binary target 'like_dislike' from ratings...")
    df_feat['like_dislike'] = (df_feat['rating'] >= 0.31).astype(int)
    print("Target variable 'like_dislike' distribution:")
    print(df_feat['like_dislike'].value_counts())

    # Step 3: Split data
    print("Step 3: Splitting data into train, validation, and test sets...")
    train, val, test = split_data(df_feat, test_size=0.2, val_size=0.1)
    print(f"Train set shape: {train.shape}")
    print(f"Validation set shape: {val.shape}")
    print(f"Test set shape: {test.shape}")

    # Choose feature columns & target
    all_cols = df_feat.columns.tolist()
    non_features = [
        'user_id', 'movie_id', 'like_dislike', 'rating', 'genres', 'timestamp',
        'title', 'director', 'main_cast', 'language', 'country'
    ]
    feature_cols = [c for c in all_cols if c not in non_features]
    print(f"Using {len(feature_cols)} feature columns for model training")

    target_col = 'like_dislike'

    # Step 4: Train models
    # print("Step 4: Training models...")
    # os.makedirs("models/", exist_ok=True)
    # train_models(train, val, feature_cols, target_col, models_output_dir="models/")

    # Step 5: Evaluate on test set
    print("\n--- Test set evaluation ---")
    os.makedirs("outputs/reports/", exist_ok=True)
    os.makedirs("outputs/figures/", exist_ok=True)

    model_paths = {
        "random_forest": "models/rf_model.pkl",
        "xgboost": "models/xgb_model.pkl",
        "logistic_regression":"models/lr_model.pkl",
        "Neural_network":"models/mlp_model.pkl"
    }

    for model_name, model_path in model_paths.items():
        evaluate_model(model_path, test, feature_cols, target_col)


if __name__ == "__main__":
    main()

