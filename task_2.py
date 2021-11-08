def thesaurus(*name):
    dict_data = {}
    for args in name:
        key = args[0]
        if key not in dict_data:
            dict_data[key] = []
        dict_data[key].append(args)
    return dict_data


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
