import pandas as pd

def summarize_budget(df):
    return df.groupby("category")["amount"].sum()

def run_from_csv(path="data.csv"):
    df = pd.read_csv(path)
    print(summarize_budget(df).to_string())

if __name__ == "__main__":
    run_from_csv()
