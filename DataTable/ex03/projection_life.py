import pandas as pd
from load_csv import load 
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from sys import stderr

class CSVReadError(Exception):
    """ Raise when read failure of CSV """

    def __init__(self, error_msg="Error reading CSV"):
        """ CSVReadError initialization """
        self.error_msg = error_msg
        super().__init__(self.error_msg)


def extract_income() -> list:
    df = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    if not isinstance(df, pd.DataFrame):
        raise CSVReadError
    

def extract_life_expectancy() -> list:
    df = load('life_expectancy_years.csv')
    if not isinstance(df, pd.DataFrame):
        raise CSVReadError
    pass


def main():
    """ Displays projection life expectancy in relation to PIB for each country """
    df_gdp = load('population_total.csv')
    df_life = load('population_total.csv')
    if not isinstance(df_gdp, pd.DataFrame) or not isinstance(df_life, pd.DataFrame):
        print(f'aff_pop.py :: Could not load dataframe, exiting...', file=stderr)
        return 1
    try:
        df.set_index('country', inplace=True)
        print(df["1900"])
    except KeyboardInterrupt:
        print("Exiting...")
        return 0
    except (KeyError, TypeError) as e:
        print(f'{type(e).__name__} :: {e}')
        return 1


if __name__ == "__main__":
    main()