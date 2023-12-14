origin = '''
COMIDA

Comida 1
1: pato asado

Comida 2    
2: gato raro
            3: perro salchicha

COCHES
Coches 1
1: gato
2: avesturz

PATO
Pato 1
1: cuac
Pato 2
2: yessssss


Pato 3
1: es
2: el
3: epico, un pato
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


#print(list_origin)
chapter = 0
actual_chapter_list = []
actual_chapter = 0

# get the list with all the chapters len
for i, value in enumerate(list_origin):
    if value == value.upper():
        if i != actual_chapter:
            actual_chapter_list.append(i-1)
        
        actual_chapter_list.append(value)
        actual_chapter_list.append(i+1)
        actual_chapter = i
        
    if i == (len(list_origin) -1):
        actual_chapter_list.append(i)

        
#print(actual_chapter_list)

# transforms the list to a dictionary
dict_origin = {}
only_title_list = []
for i in range(0, len(actual_chapter_list), 3):
    dict_origin[actual_chapter_list[i]] = [actual_chapter_list[i+1], actual_chapter_list[i+2]]
    only_title_list.append(actual_chapter_list[i])
#print(only_title_list)



