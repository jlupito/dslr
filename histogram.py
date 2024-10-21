from describe import extract_numeric
from load_csv import load
import argparse

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

