def main():
  number = int(input("Wybierz liczbę którą sprawdzimy, czy jest liczbą pierwszą: "))

  x = list(range(1, number+1))
  
  lista_dzielnikow = []

  for i in x:
   if number % i == 0:
      lista_dzielnikow.append(i)
  print("DZIELNIKI WYBRANEJ LICZBY:")
  print(lista_dzielnikow)
  if len(lista_dzielnikow) <= 2:
     print("Jest to liczba pierwsza, ponieważ ma tylko dwa dzielniki")
  elif len(lista_dzielnikow) > 2:
     print("NIE jest to liczba pierwsza, ponieważ ma więcej niż 2 dzielniki")         
main()

