def get_none():
    return None


def flatten_dict(dict):
    new_list = []
    for i in dict:
        if type(dict[i]) == type(dict):
            for x in dict[i]:
                new_list.append(dict[i][x])

        else:
            new_list.append(dict[i])
    return new_list


# print(flatten_dict({'a': 42, 'b': 3.14}))
print(flatten_dict({"a": {"inner_a": 42, "inner_b": 350}, "b": 3.14}))
# print(flatten_dict({'a': [{'inner_inner_a': 42}]}))
