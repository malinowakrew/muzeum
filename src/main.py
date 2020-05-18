import sql.eksponaty as api
import os
import sql.wystawy as wystawy
import datetime


print("Witamy w naszym muzeum")
print("Zaloguj się na swoje konto aby mieć dostęp do większej ilości funkcjonalności")
zmienna = 1


while(zmienna):
    print("Wybierz co chcesz zrobić z naszego menu: \n"
          "1. Zaloguj się \n"
          "2. Załóż konto \n"
          "3. Przeglądaj zbiory bez konta \n")
    funkcjonalnosc = input("Podaj numer, który Cię interesuje: ")

    if (funkcjonalnosc == "1"):
        # clear = lambda: os.system('cls')
        # clear()
        print("Witamy u nas")
    elif (funkcjonalnosc == "2"):
        pass
    elif (funkcjonalnosc == "3"):
        print("\n \t ################### \n"
              "Witamy, możesz w ograniczonu sposób korzystać z naszej bazy. \n"
              "1. Sprawdź aktualne wystawy \n"
              "2. Sprawdź popularne wystawy \n")
        funkcjonalnosc = input("Podaj numer, który Cię interesuje: ")
        niezalogowany = wystawy.niezalogowany()

        if (funkcjonalnosc == "1"):
            dzis = datetime.datetime.now()
            niezalogowany.wyszukiwarka_aktywnych_wystaw()
            zmienna =  0
        elif (funkcjonalnosc == "2"):
            niezalogowany.najczesciej_odwiedzane_wystawy()
        print("\n \t ################### \n")

    else:
        print("Mamy błąd - źle wybrałeś spróbuj ponownie.")
        zmienna = 1

