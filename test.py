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

final_dict = {}
for i in dict_origin:
    final_dict[i] = []
#print(final_dict)


chapter = 1
chapter_in_list = 0
last_book = None

#from the chapter dict adds the list
for j, value in dict_origin.items():
    if j == last_book:
        chapter_in_list += 1

    for i in range(value[0], value[1]):
        if list_origin[i] == str(only_title_list[chapter_in_list]).title() + ' ' + str(chapter):
            print(list_origin[i])
            chapter += 1
        
        final_dict[j].append(list_origin[i])
        last_book = j
        

print(dict_origin)
print(final_dict)
