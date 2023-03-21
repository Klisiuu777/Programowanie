#warunek wykorzystuje zmienną sterującą i sprawdzany jest na początku pętli.
#aby pętla się skończyła zmienna sterująca musi zmienić się wewnątrz pętli.
a = 10
while a == 10:
    print(a)
print("koniec")

#########################################################################################

#nieskończona pętla.
a = 10
while a > 0:
    a = a + 1
    print(a)
print("koniec")

#########################################################################################

#czekamy aż user poda dobrą odpowiedź.
#gdy ją poda to po kliknięciu enter program się zakończy.
odpowiedz = " "
proby = 0
while odpowiedz != 't' and odpowiedz != 'n':
    proby = proby + 1
    odpowiedz = input("koniec? (t/n)")
print(f"Wybrales: {odpowiedz}")
print(f"Ilosc prob: {proby}")
