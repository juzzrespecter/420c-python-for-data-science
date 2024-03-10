import pandas as pd
import numpy as np
from load_csv import load
import matplotlib.pyplot as plt
from sys import stderr


def main():
    """
    Displays graphic with life expectancy of a country.
    """
    df = load('life_expectancy_years.csv')
    if not isinstance(df, pd.DataFrame):
        print('aff_life.py :: Could not load dataframe, exiting...',
              file=stderr)
        return 1
    try:
        _, x = df.shape
        df.set_index('country', inplace=True)
        x_values = df.columns
        plt.xticks(np.arange(0, x, 40), np.arange(1800, 2081, 40))
        y_values = df.loc['Spain']
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title("Spain Life expectancy Projections")
        plt.plot(x_values, y_values)
        plt.show()
    except KeyboardInterrupt:
        print("Exiting...")
        return 0
    except KeyError as e:
        print(f'{type(e).__name__} :: {e}')
        return 1


if __name__ == "__main__":
    main()
