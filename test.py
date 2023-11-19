origin = '''

1: pato asado
    2: gato raro
            3: perro salchicha


'''

#origin = origin.rstrip()
origin = origin.split('\n')
list_origin = []

# quits the enters
for i, v in enumerate(origin):
    if v != '':
        list_origin.append(v)

# quits the spaces
for i, v in enumerate(list_origin):
    list_origin[i] = v.strip()


print(list_origin)
