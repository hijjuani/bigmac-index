from data_loader import load_data
from calculations import compute_bigmac_metrics
from visualization import plot_bigmac_analysis


def main():
    df = load_data("data/BigMac.xlsx")
    df = compute_bigmac_metrics(df)
    plot_bigmac_analysis(df)


if __name__ == "__main__":
    main()