print("Condicionales")

a = 5

b = 6

c = 0

r = (a < 6 and c > 6)

print(r)

while c <= 10:
    c += 1

    if c == 9:
        break

    if c == 7:
        continue

    if c % 2 == 0:
        print("Es par", c)

    if c % 2 != 0:
        print("Es impar", c)

    print("Contador: ", c)

lista = [1,2,3,'a','b','c',4,5,6,7]

for l in lista:
    print(l)

print("----")

lista = [13, 2, 3, 4, 5, 6, 12, 2, 3, 4, 5, 1, 2, 3, 5]

for l in set(lista):
    print(l)