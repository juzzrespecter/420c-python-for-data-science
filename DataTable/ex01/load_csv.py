from pandas import read_csv, DataFrame
from sys import stderr


def load(path: str) -> DataFrame:
    """
    Loads csv into dataframe

    - path: path to csv.
    """
    try:
        df = read_csv(path)
        print(f'Loading dataset of dimensions: {df.shape}')
        return df
    except IOError as e:
        print(f'Error trying to read file: {e}', file=stderr)
    except ValueError as e:
        print(f'{type(e).__name__}: {e}', file=stderr)
    return None
