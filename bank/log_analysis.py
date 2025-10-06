import time
import pandas as pd

LOG_FILE = "logs/app.csv"
PROCESSED_LINES = 0

def analyze_logs():
    global PROCESSED_LINES
    try:
        df = pd.read_csv(LOG_FILE, skiprows=range(1, PROCESSED_LINES + 1))
        PROCESSED_LINES += len(df)

        total_logs = PROCESSED_LINES
        info_count = df[df["Level"] == "INFO"].shape[0]
        warning_count = df[df["Level"] == "WARNING"].shape[0]
        error_count = df[df["Level"] == "ERROR"].shape[0]

        login_attempts = df["Message"].str.contains("Login attempt", case=False).sum()
        failed_logins = df["Message"].str.contains("Invalid login credentials", case=False).sum()
        get_requests = df["Message"].str.contains("GET", case=False).sum()
        post_requests = df["Message"].str.contains("POST", case=False).sum()
        put_requests = df["Message"].str.contains("PUT", case=False).sum()
        delete_requests = df["Message"].str.contains("DELETE", case=False).sum()

        print("\nLog Summary:")
        print(f"Total log entries: {total_logs}")
        print(f"INFO: {info_count}, WARNING: {warning_count}, ERROR: {error_count}")
        print(f"Login attempts: {login_attempts}, Failed logins: {failed_logins}")
        print(f"Total Get Requests: {get_requests}")
        print(f"Total Post Requests: {post_requests}")
        print(f"Total Put Requests: {put_requests}")
        print(f"Total Delete Requests: {delete_requests}")

    except Exception as e:
        print(f"Error reading log file: {e}")

if __name__ == "__main__":
    print("🔍 Starting real-time log analysis...")
    analyze_logs()
