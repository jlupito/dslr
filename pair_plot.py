from utils.load_csv import load
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype
import seaborn as sns
import numpy as np
import argparse


def main():

    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument('path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    try:
        df = load(args.path)
        if df is None:
            return
        if df['Hogwarts House'].dropna().empty:
            raise ValueError("Houses have not been attributed yet.")

        df.drop('Index', axis=1, inplace=True)
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if 'Hogwarts House' in df.columns:
            numeric_cols.append('Hogwarts House')
        colors = {'Gryffindor': '#8B0000', 'Hufflepuff': '#B8860B', 'Ravenclaw': '#00008B', 'Slytherin': '#006400'}
        pair_plot = sns.pairplot(df[numeric_cols], hue='Hogwarts House', palette=colors)
        
        for ax in pair_plot.axes.flatten():
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.set_xlabel(ax.get_xlabel(), fontsize=6)
            ax.set_ylabel(ax.get_ylabel(), fontsize=6)

        pair_plot._legend.set_title('House')
        for text in pair_plot._legend.get_texts():
            text.set_fontsize(6)
        pair_plot._legend.get_title().set_fontsize(8)
        
        plt.suptitle('Pair plot features by House', fontsize=10, fontweight='bold')
        plt.show()

    except KeyboardInterrupt:
        print(" Keyboard interrupt detected.")
        return

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()