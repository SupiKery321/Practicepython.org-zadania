wyraz = input("Proszę wpisz wyraz: ")

reversed = wyraz[::-1]

if wyraz == reversed:
    print(f"Wyraz {wyraz} jest palindromem")
else:
    print(f"Wyraz {wyraz} NIE jest palindromem")
        