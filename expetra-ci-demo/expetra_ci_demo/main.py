import pandas as pd

def summarize_budget(df):
    return df.groupby("category")["amount"].sum()

def run_from_csv(path="data.csv"):
    df = pd.read_csv(path)
    summary = summarize_budget(df)
    print(summary.to_string())

if __name__ == "__main__":
    run_from_csv()