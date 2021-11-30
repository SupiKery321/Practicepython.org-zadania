import random 

a = random.sample(range(1,30), 10)
b = random.sample(range(1,30), 14)

random_b_list_without_duplicate = set(b)
random_a_list_without_duplicate = set(a)

wynik = []


for numberB in random_b_list_without_duplicate:
    for numberA in random_a_list_without_duplicate:
        if numberB == numberA:
            wynik.append(numberB)

print("WYLOSOWANE LISTY:")
print(random_a_list_without_duplicate)
print(random_b_list_without_duplicate)

print("WYNIK(wspólne elementy dwóch powyższych losowych list:")
print(wynik)