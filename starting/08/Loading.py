def ft_tqdm(lst: range) -> None:
    """ A progress bar """

    n = len(lst)
    for i in lst:
        print(f"{porcentaje:padding}|█ |{i}/{n}")
    pass

