def main():
 print("GRACZ1")
 name1 = input("Jak masz na imie? ")
 gracz1 = input("Wybierz papier, kamień lub nożyce: ")
 print("GRACZ2")
 name2 = input("Jak masz na imie? ")
 gracz2 = input("Wybierz papier, kamień lub nożyce: ")

 if gracz1 == gracz2:
    print("REMIS!")
 elif gracz1 == "kamień" and gracz2 == "papier":
    print(f"{name2} WYGRYWA!")
 elif gracz1 == "papier" and gracz2 == "kamień":
    print(f"{name1} WYGRYWA!")
 elif gracz1 == "nożyce" and gracz2 == "kamień":
    print(f"{name2} WYGRYWA!")
 elif gracz1 == "kamień" and gracz2 == "nożyce":
    print(f"{name1} WYGRYWA!")
 elif gracz1 == "papier" and gracz2 == "nożyce":
    print(f"{name2} WYGRYWA!")
 elif gracz1 == "nożyce" and gracz2 == "papier":
    print(f"{name1} WYGRYWA!")
 else:
     print("ZŁY input, wpisz jeszcze raz:")
     main()
    
main()