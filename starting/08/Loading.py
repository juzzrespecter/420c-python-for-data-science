def get_percentage(n: int, i: int) -> int:
    """ Get current percentage """
    return int(((i + 1) / n) * 100)


def get_progress(percentage: int) -> str:
    """ Gets current progress completion for bar """

    return "█" * percentage


def ft_tqdm(lst: range) -> None:
    """ A progress bar """

    n = len(lst)
    fmt = "\r{:3}%|{:100}| {}/{}"
    print(fmt.format(0, "", 0, n), end="")
    yield 0
    for i in lst:
        p = get_percentage(n, i)
        progress = get_progress(p)
        print(fmt.format(p, progress, i + 1, n), end="")
        yield i
    print()
