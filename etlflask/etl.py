import pandas as pd
import sqlite3

class ETLError(Exception):
    pass

def calculate_loan(row):
    if row['account_type'].lower() == 'savings':
        return row['balance']*2
    elif row['account_type'].lower() == 'current':
        return row['balance']*1.5
    else:
        return 0

def run_etl(csv_file, db_file="bank.db"):
    try:
        df = pd.read_csv(csv_file)
        mandatory_columns = {'account_number','name', 'balance', 'account_type'}
        if not mandatory_columns.issubset(df.columns):
            raise ETLError("Missing required columns in CSV!")
        if df.empty:
            raise ETLError("CSV file is empty!")

        df['balance'] = df['balance'].apply(lambda x: float(x) if x >= 0 else 0)

        if 'account_id' in df.columns:
            df = df.drop(columns=['account_id'])

        conn = sqlite3.connect(db_file)
        df.to_sql("accounts", conn, if_exists="replace", index=False)


        # df = pd.read_sql("SELECT * FROM accounts WHERE balance >= 5000",conn)
        df = pd.read_sql("SELECT * FROM accounts", conn)
        df_filtered = df[df['balance'] >= 5000]
        print("account with balance more that 5000")
        print(df_filtered)

        df = pd.read_sql("SELECT * FROM accounts",conn)
        print("Interest amount for all customers")
        df["interest_amount"] = df.apply(lambda interest: interest['balance']*.04 if interest['account_type'].lower() == 'savings' else 0, axis=1)
        print(df)


        df["eligible_loan"] = df.apply(calculate_loan,axis=1)
        print("Loan amount for all customers")
        print(df)
        conn.close()

        print("ETL Completed Successfully!")
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found.")
    except ETLError as e:
        print(f"ETL Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    run_etl("bank_data.csv")