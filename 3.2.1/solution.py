# не добавляйте кода вне функции
def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2*key in d:
        d[key*2] += [value]
    else:
        d.setdefault(key*2,[]).append(value)
# не добавляйте кода вне функции