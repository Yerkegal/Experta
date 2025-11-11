import pandas as pd
from expetra_ci_demo.main import summarize_budget

def test_summarize_budget():
    df = pd.DataFrame({
        "category": ["Rent", "Food", "Food", "NFTs"],
        "amount":   [150000, 80000, 20000, 50000]
    })
    out = summarize_budget(df)
    assert out["Food"] == 100000
    assert out["Rent"] == 150000
    assert out["NFTs"] == 50000