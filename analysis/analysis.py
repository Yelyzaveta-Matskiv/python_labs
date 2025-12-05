import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_file)

    avg_price = np.mean(df["price_per_unit"])
    median_qty = np.median(df["quantity"])
    std_price = np.std(df["price_per_unit"])

    df["total_price"] = df["quantity"] * df["price_per_unit"]

    supplier_totals = df.groupby("supplier")["total_price"].sum()
    top_supplier = supplier_totals.idxmax()

    category_totals = df.groupby("category")["quantity"].sum()

    low_supply = df[df["quantity"] < 100]
    low_supply.to_csv("low_supply.csv", index=False)

    print(df.sort_values("total_price", ascending=False).head(3))

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("=== Report ===\n")
        f.write(f"Average price: {avg_price:.2f}\n")
        f.write(f"Median quantity: {median_qty}\n")
        f.write(f"Std price: {std_price:.2f}\n")
        f.write(f"Top supplier: {top_supplier}\n")
        f.write("Low supply file: low_supply.csv\n")

    category_totals.plot(kind="bar")
    plt.title("Quantity by Category")
    plt.tight_layout()
    plt.savefig("category_distribution.png")

if __name__ == "__main__":
    main()