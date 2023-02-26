#wczytaj z klawiatury trzy liczby do zmiennych
#a,b,c
#a następnie wyświetl ich sumę
a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))
print(f"suma liczba a+b+c = {a+b+c}")

#oblicz i wyświetl resztę z dzielenia przez 2 liczby a
print(f"reszta z dzielenia przez 2 liczby a = {a%2}")
# oblicz i wyświetl wynik dzielenia całkowitego przez 10
# liczby b 
print(f"Wynik dzielenia całkowitego b i 10 = {b // 10}")
#oblicz i wyświetl pierwiastek kwadratowy z liczby c 
print(f"Pierwiastek kwadratowy c  = { c**0.5}")

#zwiększ wartość liczby c o 2 i wyświetl liczbę c
c = c+2
print(c)

#zwiększ wartość liczby b dwa razy i wyświetl liczbę b
b *= 2
print(b)

# do zmiennej a przypisz kwadrat liczby c
# i wyświetl liczbę a
a = c**2
print(a)
# przypisz do zmiennej b napis "Koniec ćw" połączony
# z wartością ze zmiennej a. Wyświetl zmienną b 
b = "Koniec ćw" + str(a)
print(b)

