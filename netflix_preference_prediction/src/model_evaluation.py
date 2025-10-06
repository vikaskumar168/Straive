import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import joblib


def evaluate_model(model_path, df, feature_cols, target_col):
    # Load model
    print(f"Loading model from: {model_path}")
    model = joblib.load(model_path)

    # Derive model name from filename
    model_name = os.path.splitext(os.path.basename(model_path))[0]

    # Ensure outputs directories exist
    os.makedirs("outputs/reports", exist_ok=True)
    os.makedirs("outputs/figures", exist_ok=True)

    # Prepare data
    print(f"Preparing data for evaluation with features: {feature_cols} and target: {target_col}")
    X = df[feature_cols]
    y_true = df[target_col]

    # Generate predictions
    print("Generating predictions...")
    y_pred = model.predict(X)
    y_proba = model.predict_proba(X)[:, 1]

    # Evaluation results
    print(f"\n--- Evaluation Results for model: {model_name} ---")
    report = classification_report(y_true, y_pred)
    print("Classification Report:")
    print(report)

    roc_auc = roc_auc_score(y_true, y_proba)
    print(f"ROC AUC Score: {roc_auc:.4f}")

    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(cm)
    print("--- End of Evaluation ---\n")

    # Save classification report
    report_path = f"outputs/reports/{model_name}_classification_report.txt"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Classification report saved to {report_path}")

    # Save confusion matrix as heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"{model_name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    fig_path = f"outputs/figures/{model_name}_confusion_matrix.png"
    plt.savefig(fig_path)
    plt.close()
    print(f"Confusion matrix heatmap saved to {fig_path}")
