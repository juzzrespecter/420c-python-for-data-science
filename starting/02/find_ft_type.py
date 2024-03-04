def all_thing_is_obj(object: any) -> int:
    type_obj = type(object)
    typename = type_obj.__name__
    if typename not in ['list', 'tuple', 'set', 'dict', 'str']:
        print('Type not found')
    else:
        if (typename == 'str'):
            typename = f'{object} is in the kitchen'
        print(f'{typename.capitalize()} : {type_obj}')
    return 42