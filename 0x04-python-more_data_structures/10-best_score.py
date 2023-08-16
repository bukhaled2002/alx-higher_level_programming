#!/usr/bin/python3
#!/usr/bin/python3
def best_score(a_dictionary: dict):
    if a_dictionary == None:
        return None
    key = list(a_dictionary.keys())
    if len(key) < 1:
        return None
    print(key)
    large=0
    value = ''
    for i in key:
        if a_dictionary[i] >= large:
            value = i
            large = a_dictionary[i]
        else: continue
    return value
