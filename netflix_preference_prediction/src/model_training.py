# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.neural_network import MLPClassifier
# from xgboost import XGBClassifier
# import joblib
# # from feature_engineering import engineer_features
#
# def split_data(df, test_size=0.2, val_size=0.1, random_state=42):
#     print("Splitting data into train, validation, and test sets...")
#     # First split off test
#     train_val, test = train_test_split(df, test_size=test_size, random_state=random_state, stratify=df['like_dislike'])
#     # Then split train & val
#     relative_val = val_size / (1 - test_size)
#     train, val = train_test_split(train_val, test_size=relative_val, random_state=random_state,
#                                   stratify=train_val['like_dislike'])
#     print(f"Train set size: {train.shape[0]} rows")
#     print(f"Validation set size: {val.shape[0]} rows")
#     print(f"Test set size: {test.shape[0]} rows")
#     return train, val, test
#
#
# def train_models(train_df, val_df, feature_cols, target_col, models_output_dir="models/"):
#     print("Starting model training...")
#
#     # Prepare data
#     X_train = train_df[feature_cols]
#     y_train = train_df[target_col]
#     X_val = val_df[feature_cols]
#     y_val = val_df[target_col]
#
#     # Model 1: Random Forest
#     print("Training Random Forest classifier...")
#     rf = RandomForestClassifier(random_state=42)
#     rf_param = {'n_estimators': [100, 200], 'max_depth': [5, 10]}
#     rf_grid = GridSearchCV(rf, rf_param, cv=3, scoring='f1')
#     rf_grid.fit(X_train, y_train)
#     print("Random Forest best params:", rf_grid.best_params_)
#     joblib.dump(rf_grid.best_estimator_, models_output_dir + "rf_model.pkl")
#     print(f"Random Forest model saved to {models_output_dir}rf_model.pkl")
#
#     # Model 2: XGBoost
#     print("Training XGBoost classifier...")
#     xgb = XGBClassifier(eval_metric="logloss", random_state=42)
#     xgb_param = {'n_estimators': [100, 200], 'max_depth': [3, 6]}
#     xgb_grid = GridSearchCV(xgb, xgb_param, cv=3, scoring='f1')
#     xgb_grid.fit(X_train, y_train)
#     print("XGBoost best params:", xgb_grid.best_params_)
#     joblib.dump(xgb_grid.best_estimator_, models_output_dir + "xgb_model.pkl")
#     print(f"XGBoost model saved to {models_output_dir}xgb_model.pkl")
#
#     # Model 3: Logistic Regression
#     print("Training Logistic Regression classifier...")
#     lr = LogisticRegression(max_iter=1000, random_state=42)
#     lr_param = {'C': [0.1, 1, 10], 'penalty': ['l2']}
#     lr_grid = GridSearchCV(lr, lr_param, cv=3, scoring='f1')
#     lr_grid.fit(X_train, y_train)
#     print("Logistic Regression best params:", lr_grid.best_params_)
#     joblib.dump(lr_grid.best_estimator_, models_output_dir + "lr_model.pkl")
#     print(f"Logistic Regression model saved to {models_output_dir}lr_model.pkl")
#
#     # Model 4: Neural Network (MLP)
#     print("Training Neural Network classifier...")
#     mlp = MLPClassifier(max_iter=500, random_state=42)
#     mlp_param = {'hidden_layer_sizes': [(50,), (100,)], 'activation': ['relu', 'tanh']}
#     mlp_grid = GridSearchCV(mlp, mlp_param, cv=3, scoring='f1')
#     mlp_grid.fit(X_train, y_train)
#     print("Neural Network best params:", mlp_grid.best_params_)
#     joblib.dump(mlp_grid.best_estimator_, models_output_dir + "mlp_model.pkl")
#     print(f"Neural Network model saved to {models_output_dir}mlp_model.pkl")
#
#     print("Model training completed.\n")


import time
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
import joblib


def split_data(df, test_size=0.2, val_size=0.1, random_state=42):
    print("Splitting data into train, validation, and test sets...")
    # First split off test
    train_val, test = train_test_split(df, test_size=test_size, random_state=random_state, stratify=df['like_dislike'])
    # Then split train & val
    relative_val = val_size / (1 - test_size)
    train, val = train_test_split(train_val, test_size=relative_val, random_state=random_state,
                                  stratify=train_val['like_dislike'])
    print(f"Train set size: {train.shape[0]} rows")
    print(f"Validation set size: {val.shape[0]} rows")
    print(f"Test set size: {test.shape[0]} rows")
    return train, val, test


def train_models(train_df, val_df, feature_cols, target_col, models_output_dir="models/"):
    print("Starting model training...")

    # Prepare data
    X_train = train_df[feature_cols]
    y_train = train_df[target_col]
    X_val = val_df[feature_cols]
    y_val = val_df[target_col]

    # Model 1: Random Forest
    # print("Training Random Forest classifier...")
    # start_time = time.time()
    # rf = RandomForestClassifier(random_state=42)
    # rf_param = {'n_estimators': [100, 200], 'max_depth': [5, 10]}
    # # rf_grid = GridSearchCV(rf, rf_param, cv=3, scoring='f1')
    # # rf_grid.fit(X_train, y_train)
    # rf_rand = RandomizedSearchCV(
    #     rf,
    #     rf_param,
    #     cv=3,
    #     scoring='f1',
    #     n_iter=2,
    #     random_state=42,
    #     n_jobs=-1
    # )
    # rf_rand.fit(X_train, y_train)
    # elapsed = time.time() - start_time
    # print(f"Random Forest best params: {rf_rand.best_params_}")
    # print(f"Random Forest training time: {elapsed:.2f} seconds")
    # joblib.dump(rf_rand.best_estimator_, models_output_dir + "rf_model.pkl")
    # print(f"Random Forest model saved to {models_output_dir}rf_model.pkl")

    # Model 2: XGBoost
    print("Training XGBoost classifier...")
    start_time = time.time()
    xgb = XGBClassifier(eval_metric="logloss", random_state=42)
    xgb_param = {'n_estimators': [100, 200], 'max_depth': [3, 6]}
    xgb_grid = GridSearchCV(xgb, xgb_param, cv=3, scoring='f1')
    xgb_grid.fit(X_train, y_train)
    elapsed = time.time() - start_time
    print(f"XGBoost best params: {xgb_grid.best_params_}")
    print(f"XGBoost training time: {elapsed:.2f} seconds")
    joblib.dump(xgb_grid.best_estimator_, models_output_dir + "xgb_model.pkl")
    print(f"XGBoost model saved to {models_output_dir}xgb_model.pkl")

    # Model 3: Logistic Regression
    print("Training Logistic Regression classifier...")
    start_time = time.time()
    lr = LogisticRegression(max_iter=4500, random_state=42)
    lr_param = {'C': [0.1, 1, 10], 'penalty': ['l2']}
    lr_grid = GridSearchCV(lr, lr_param, cv=3, scoring='f1')
    lr_grid.fit(X_train, y_train)
    elapsed = time.time() - start_time
    print(f"Logistic Regression best params: {lr_grid.best_params_}")
    print(f"Logistic Regression training time: {elapsed:.2f} seconds")
    joblib.dump(lr_grid.best_estimator_, models_output_dir + "lr_model.pkl")
    print(f"Logistic Regression model saved to {models_output_dir}lr_model.pkl")

    # Model 4: Neural Network (MLP)
    print("Training Neural Network classifier...")
    start_time = time.time()
    mlp = MLPClassifier(max_iter=500, random_state=42)
    mlp_param = {'hidden_layer_sizes': [(50,), (100,)], 'activation': ['relu', 'tanh']}
    mlp_grid = GridSearchCV(mlp, mlp_param, cv=1, scoring='f1')
    mlp_grid.fit(X_train, y_train)
    elapsed = time.time() - start_time
    print(f"Neural Network best params: {mlp_grid.best_params_}")
    print(f"Neural Network training time: {elapsed:.2f} seconds")
    joblib.dump(mlp_grid.best_estimator_, models_output_dir + "mlp_model.pkl")
    print(f"Neural Network model saved to {models_output_dir}mlp_model.pkl")

    print("Model training completed.\n")

    # import time
    # import pandas as pd
    # from sklearn.linear_model import LogisticRegression
    # from sklearn.model_selection import RandomizedSearchCV
    # from sklearn.ensemble import RandomForestClassifier
    # from sklearn.neural_network import MLPClassifier
    # from xgboost import XGBClassifier
    # import joblib
    #
    # def train_models(train_df, val_df, feature_cols, target_col, models_output_dir="models/"):
    #     print("Starting model training...")
    #
    #     X_train = train_df[feature_cols]
    #     y_train = train_df[target_col]
    #
    #     # Model 1: Random Forest
    #     print("Training Random Forest classifier...")
    #     start_time = time.time()
    #     rf = RandomForestClassifier(random_state=42)
    #     rf_param = {
    #         'n_estimators': [100, 200, 300],
    #         'max_depth': [5, 10, 15],
    #         'min_samples_split': [2, 5],
    #         'min_samples_leaf': [1, 2]
    #     }
    #     rf_rand = RandomizedSearchCV(rf, rf_param, cv=3, scoring='f1', n_iter=10, random_state=42, n_jobs=-1)
    #     rf_rand.fit(X_train, y_train)
    #     elapsed = time.time() - start_time
    #     print(f"Random Forest best params: {rf_rand.best_params_}")
    #     print(f"Random Forest training time: {elapsed:.2f} seconds")
    #     joblib.dump(rf_rand.best_estimator_, models_output_dir + "rf_model.pkl")
    #
    #     # Model 2: XGBoost
    #     print("Training XGBoost classifier...")
    #     start_time = time.time()
    #     xgb = XGBClassifier(eval_metric="logloss", random_state=42)
    #     xgb_param = {
    #         'n_estimators': [100, 200, 300],
    #         'max_depth': [3, 6, 9],
    #         'learning_rate': [0.01, 0.1, 0.3]
    #     }
    #     xgb_rand = RandomizedSearchCV(xgb, xgb_param, cv=3, scoring='f1', n_iter=10, random_state=42, n_jobs=-1)
    #     xgb_rand.fit(X_train, y_train)
    #     elapsed = time.time() - start_time
    #     print(f"XGBoost best params: {xgb_rand.best_params_}")
    #     print(f"XGBoost training time: {elapsed:.2f} seconds")
    #     joblib.dump(xgb_rand.best_estimator_, models_output_dir + "xgb_model.pkl")
    #
    #     # Model 3: Logistic Regression
    #     print("Training Logistic Regression classifier...")
    #     start_time = time.time()
    #     lr = LogisticRegression(max_iter=1000, random_state=42)
    #     lr_param = {
    #         'C': [0.01, 0.1, 1, 10],
    #         'penalty': ['l2'],
    #         'solver': ['lbfgs', 'saga']
    #     }
    #     lr_rand = RandomizedSearchCV(lr, lr_param, cv=3, scoring='f1', n_iter=6, random_state=42, n_jobs=-1)
    #     lr_rand.fit(X_train, y_train)
    #     elapsed = time.time() - start_time
    #     print(f"Logistic Regression best params: {lr_rand.best_params_}")
    #     print(f"Logistic Regression training time: {elapsed:.2f} seconds")
    #     joblib.dump(lr_rand.best_estimator_, models_output_dir + "lr_model.pkl")
    #
    #     # Model 4: Neural Network (MLP)
    #     print("Training Neural Network classifier...")
    #     start_time = time.time()
    #     mlp = MLPClassifier(max_iter=500, random_state=42)
    #     mlp_param = {
    #         'hidden_layer_sizes': [(50,), (100,), (100, 50)],
    #         'activation': ['relu', 'tanh'],
    #         'alpha': [0.0001, 0.001, 0.01]
    #     }
    #     mlp_rand = RandomizedSearchCV(mlp, mlp_param, cv=3, scoring='f1', n_iter=10, random_state=42, n_jobs=-1)
    #     mlp_rand.fit(X_train, y_train)
    #     elapsed = time.time() - start_time
    #     print(f"Neural Network best params: {mlp_rand.best_params_}")
    #     print(f"Neural Network training time: {elapsed:.2f} seconds")
    #     joblib.dump(mlp_rand.best_estimator_, models_output_dir + "mlp_model.pkl")
    #
    #     print("Model training completed.\n")


