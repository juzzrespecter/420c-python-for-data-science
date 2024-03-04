def NULL_not_found(object: any) -> int:
    types = {"NoneType": "Nothing", "float": "Cheese", "int": "Zero", "str": "Empty", "bool": "Fake"}
    obj_type = type(object)
    typename = obj_type.__name__
    if object or (object != object):
        print(f"Type not Found")
        return 1
    else:
        print(f"{types[typename]}: {object} {obj_type}")
    return 0