number = int(input("Wybierz numer którego wypiszemy dzielniki: "))


x = list(range(1, number+1))

lista_dzielnikow = []


for i in x:
 if number % i == 0:
    lista_dzielnikow.append(i)


print(lista_dzielnikow)