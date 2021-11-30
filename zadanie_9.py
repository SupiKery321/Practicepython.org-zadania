import random 

random_number = random.randint(1,9)

def main():
 choosing_number = int(input("Wybierz numer od 1 do 9: "))

 if random_number == choosing_number:
     print("ZGADŁEŚ, JESTEŚ GIGA KOKSEM!")
 elif choosing_number > random_number:
     print("Wylosowany numer jest trochę mniejszy, zgaduj dalej!")
     main() 
 elif choosing_number < random_number:
     print("Wylosowany numer jest większy, zgaduj dalej")
     main()

main()