import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt
import numpy as np
from sys import stderr


def formatter_func(value: float, pos) -> str:
    """ Aux. function formater for yaxis """
    return f'{value / 1e6:.1f}M'


def translate(value: str) -> float:
    """ Translates trsing formatted value into float. """
    change = {"k": 1000., "M": 1000000.0, "B": 1000000000.0}
    if value[-1] not in "kMB":
        return value
    return float(value[:-1]) * change[value[-1]]


def set_axes(df: pd.DataFrame) -> None:
    """ Set all plot info. """
    _, x = df.shape
    plt.xticks(np.arange(0, x - 50, 40), np.arange(1800, 2041, 40))
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.gca().yaxis.set_major_formatter(formatter_func)
    plt.title("Population Projections")


def plot_country(df: pd.DataFrame, name: str) -> None:
    """ Plot a country into ptl. """
    _, x = df.shape
    x_values = df.columns[:-50]
    y_values = list(map(translate, df.loc[name][:-50]))
    plt.plot(x_values, y_values, label=name)


def main():
    """
    Displays graphic comparison between Spain and another country.
    """
    df = load('population_total.csv')
    if not isinstance(df, pd.DataFrame):
        print('aff_pop.py :: Could not load dataframe, exiting...',
              file=stderr)
        return 1
    try:
        df.set_index('country', inplace=True)
        set_axes(df)
        plot_country(df, 'Spain')
        plot_country(df, 'France')
        plt.legend(loc='lower right')
        plt.show()
    except KeyboardInterrupt:
        print("Exiting...")
        return 0
    except KeyError as e:
        print(f'{type(e).__name__} :: {e}')
        return 1


if __name__ == "__main__":
    main()
