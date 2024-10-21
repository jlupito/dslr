import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
from pandas.api.types import is_numeric_dtype
from utils_stats import calculate
import argparse


def update_feature(df, column):
    info = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
    data = column.dropna().tolist()
    calculation = [calculate.count(data), calculate.mean(data), calculate.std(data),
                calculate.min(data), calculate.quart(data)[0], calculate.median(data),
                calculate.quart(data)[1], calculate.max(data)]

    for i in range(len(info)):
        df.at[info[i], column.name] = calculation[i]
    # print(df)
    return df

def create_dataset(features):
    info = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
    data = np.zeros((len(info), len(features)))
    df = pd.DataFrame(data, index = info, columns = features)
    # print(df)
    return df

def extract_numeric(df):
        features = []
        for col in df.columns[1:]:
            if not df[col].dropna().empty and is_numeric_dtype(df[col]):
                features.append(col)
        result_df = create_dataset(features)

        for col in df.columns[1:]:
            if not df[col].dropna().empty and is_numeric_dtype(df[col]):
                result_df = update_feature(result_df, df[col])
        
        return result_df

def main():

    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument('path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    try:
        df = load(args.path)
        if df is None:
            return
        
        numeric_df = extract_numeric(df)
    
        print(numeric_df)

    except KeyboardInterrupt:
        print(" Keyboard interrupt detected.")
        return

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()