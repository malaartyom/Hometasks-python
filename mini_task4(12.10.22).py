def reversed_dict(d):
    items = list(d.items())
    values = list(set(d.values()))
    almost_dictionary = []
    d1 = dict()
    for i in values:
        a = [i]
        for key, value in items:
            if i == value:
                a.append(key)
        almost_dictionary.append(a)
    for i in almost_dictionary:
        d1[i[0]] = tuple(i[1:]) if len(i[1:]) > 1 else i[1]
    return d1


d = {"Ivanov": 97832, "Petrov": 97832, "Sidorov": 56738, "Popov": 56738, "Malyarenko": 56738, "Rude": 434343}
d1 = {(1,2): 97832, "Petrov": 55521, (2,3): 97832}
d2 = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Sidorov": 97832}
print(reversed_dict(d))
print(reversed_dict(d1))
print(reversed_dict(d2))

