d1 = {'nombre':'daniel' , 'edad' : 23 , 'a' : 3}
# Imprime los key del diccionario
for x in d1:
    print(d1[x])
d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado