import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def main():
    try:
        df = load("data.csv")
        if df is None:
            return
        if (df < 0).any().any():
            raise ValueError("Mileage and Price inputs cannot be negative.")
        

    except KeyboardInterrupt:
        print(" Keyboard interrupt detected.")
        return

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()