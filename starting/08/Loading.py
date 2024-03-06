def get_percentage(n: int, i: int) -> int:
    return int(((i + 1) / n) * 100)

def get_progress(percentage: int) -> str:
    return "█" * percentage

def ft_tqdm(lst: range) -> None:
    """ A progress bar """

    n = len(lst)
    for i in lst:
        p = get_percentage(n, i)
        progress = get_progress(p)
        print('\r', f"{p:<3}%|{progress:100}| {i}/{n}", end="")
        yield i
