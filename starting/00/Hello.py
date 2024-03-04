ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

new_values = ["World!", "Spain!", "Madrid!", "42Madrid"]

# List substitution
if "tata!" in ft_list:
    ft_list[ft_list.index("tata!")] = new_values[0]

# Tuple substitution
if "toto!" in ft_tuple:
    ft_tuple = tuple([new_values[1] if n == "toto!" else n for n in list(ft_tuple)])

# Set substitution
if "tutu!" in ft_set:
    ft_set.remove("tutu!")
    ft_set.add(new_values[2])

# Dict substitution
if "titi!" in ft_dict.values():
    ft_dict["Hello"] = new_values[3]

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
