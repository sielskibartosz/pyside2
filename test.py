from database import DB
import random

a=DB()
#print(a.get_es_words())
print(a.get_pl_words())
#print(a.execute_command("SELECT slowa.pl,slowa.en FROM slowa ORDER BY RANDOM() LIMIT 3 ;"))
#print(random.choices((a.get_pl_words()),k =10))

lista=['s','e','g']
f = random.choice(lista)
print(f)
lista.remove(f)


f = random.choice(lista)
print(f)
lista.remove(f)


f = random.choice(lista)
print(f)
lista.remove(f)

if len(lista) == 0:
    print('lolo')
else:
    print('papa')

f = random.choice(lista)
print(f)
lista.remove(f)


f = random.choice(lista)
print(f)
lista.pop(f)


f = random.choice(lista)
print(f)
lista.pop(f)


f = random.choice(lista)
print(f)
lista.pop(f)


'''
u = (a.get_nr_of_rand_records(2))
print(u)
print(random.choice(u))
'''

