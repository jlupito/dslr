import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.load_csv import load
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype
import numpy as np
from matplotlib.patches import Patch
import argparse


def get_numeric_col(df):
    numeric =[]
    for col in df.columns[1:]:
        if not df[col].dropna().empty and is_numeric_dtype(df[col]):
            numeric.append(col)
    return numeric

def get_data_by_house(houses, col, df):
    data_by_house = {}
    for house in houses:
        house_data = df[df['Hogwarts House'] == house][col].dropna().to_numpy()
        data_by_house[house] = house_data
    return data_by_house

def main():

    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument('path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    try:
        df = load(args.path)
        if df is None:
            return
        if not df['Hogwarts House'].dropna().empty:
            houses = df['Hogwarts House'].unique()
        else:
            raise ValueError("Houses have not been attributed yet.")
        
        numeric_col = get_numeric_col(df)
        fig, axes = plt.subplots(5, 3, figsize=(10, 5 * 5))
        bar_colors = ['#00008B', '#006400', '#8B0000', '#B8860B']    

        for ax, col in zip(axes.flat, numeric_col):
            bar_values = get_data_by_house(houses, col, df)

            for house, color in zip(houses, bar_colors):
                ax.hist(bar_values[house], bins=20, alpha=0.5, label=house, color=color)         
            ax.set_title(col, fontsize=10)
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels(ax.get_xticks(), fontsize=6)
            ax.set_yticks(ax.get_yticks())
            ax.set_yticklabels(ax.get_yticks(), fontsize=6)
        
        for ax in axes.flat[len(numeric_col):]:
            fig.delaxes(ax)
        legend_handles = [Patch(color=color, label=house) for color, house in zip(bar_colors, houses)]
        fig.legend(handles=legend_handles, loc='lower right', fontsize=10, bbox_to_anchor=(0.9, 0.10))
        fig.suptitle('Score distribution by House for each subject', fontsize=12, fontweight='bold', y=0.96)

        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        plt.show()

    except KeyboardInterrupt:
        print(" Keyboard interrupt detected.")
        return

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()

