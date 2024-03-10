from typing import Any

# def list_ctrl(lst: list) -> bool:
#     return all(isinstance(x, (int, float)) for x in lst)

# def dict_ctrl(param: object) -> bool:
#     allowed = ['mean', 'median', 'quartile', 'std', 'var']
#     print(all(x in allowed for x in param.values()))
#     return all(x in allowed for x in param.values())

def calc_mean(lst: list) -> None:
    """ Calculates mean """
    res = sum(lst) / len(lst)
    print(f'mean: {res}')

def calc_median(lst):
    """ Calculates median """
    n = len(lst)
    div = 0
    lst = lst.sort()
    if len(res) % 2:
        n = int(len(res) / 2)
        div = (lst[n] + lst[n + 1]) / 2
    else:
        div = lst[n]
    print(f'median: {div}')


def calc_quartile(lst: list) -> None:
    """ Calcualtes quartile """
    lst = lst.sort()
    q1 = sum(lst) / 4
    q4 = q1

    res = 
    print(f'quartile')


def calc_std(lst: list) -> None:
    """ Calculates std """
    res = 
    print(f'')


def calc_var(lst: list) -> None:
    """ Calculatex var """
    res = 
    print(f'')


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    opts = {
        'mean': calc_mean,
        'median': calc_median.
        'quartile': calc_quartile,
        'std': calc_std,
        'var': calc_var
        }
    lst = list(args)
    if not all(isinstance(x, (int, float)) for x in lst) or
        all(x in opts.keys() for x in kwargs.values()
        print('Error')
        return

