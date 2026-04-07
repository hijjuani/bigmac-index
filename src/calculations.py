import pandas as pd

def compute_bigmac_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute theoretical exchange rate and price gap (brecha).
    """

    df = df.copy()

    # Tipo de cambio implícito según Big Mac
    df["BigMac_Implied_FX"] = df["Price_ARS"] / df["Price_USA"]

    # Brecha porcentual respecto al dólar blue
    df["FX_Gap_Percent"] = (
        (df["Dolar_Blue"] / df["BigMac_Implied_FX"]) - 1
    ) * 100

    return df