import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Load Big Mac dataset from Excel file.
    """
    df = pd.read_excel(path)
    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)
    return df