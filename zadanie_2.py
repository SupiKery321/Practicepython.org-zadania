phone_number = int(input("Podaj proszę swój numer telefonu:"))
sprawdzanie_podzielnosci = int(input("Podaj liczbę przez którą chcesz podzielić swój numer"))

if phone_number % 4 == 0:
    print(f"{phone_number} jest podzielny przez 4")
elif phone_number % 2 == 0:
    print(f"{phone_number} jest liczbą parzystą")
else:
    print(f"{phone_number} jest liczbą nieparzystą")
    
if phone_number % sprawdzanie_podzielnosci == 0:
    print(f"{phone_number} jest podzielny przez {sprawdzanie_podzielnosci}")
else:
    print(f"{phone_number} NIE jest podzielny przez {sprawdzanie_podzielnosci}")
    