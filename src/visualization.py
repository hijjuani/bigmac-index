import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_bigmac_analysis(df):

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Precio Big Mac en USD
    ax1.plot(df["Date"], df["Price_USD"], label="Argentina (USD)")
    ax1.plot(df["Date"], df["Price_USA"], label="USA (USD)")
    ax1.set_ylabel("Price (USD)")
    ax1.set_xlabel("Date")
    ax1.set_title("Big Mac Index – Argentina vs USA")

    # Segundo eje: brecha cambiaria
    ax2 = ax1.twinx()
    ax2.plot(
        df["Date"],
        df["FX_Gap_Percent"],
        linestyle="--",
        label="FX Gap (%)"
    )
    ax2.set_ylabel("FX Gap (%)")

    # Formato fechas
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    # Leyenda combinada
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2)

    plt.tight_layout()
    plt.show()