from pojistenec import Pojistenec
print("______________________________\nEVIDENCE POJIŠTĚNÝCH \n")
pokracovat = True
seznam_pojistenych=[]
while pokracovat == True:
    akce = int(input("Vyberte si akci:\n"
                      "1 - Přidat nového pojištěného\n"
                      "2 - Vypsat všechny pojištěné\n"
                      "3 - Vyhledat pojištěného\n"
                      "4 - Konec\n"))

    if akce == 1:
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmené pojištěného:\n")
        telefon = int(input("Zadejte telefonní číslo:\n"))
        vek = int(input("Zadejte věk:\n"))
        pojisteny = Pojistenec(jmeno,prijmeni,telefon,vek)
        seznam_pojistenych.append(pojisteny)
        pokracovat = True

    elif akce == 2:
        for pojistenec in seznam_pojistenych:
            print(pojistenec)
        input("\nPokračujte stisknutím libovolné klávesy...")
        pokracovat = True

    elif akce==3:
        hledej_jmeno = input("Zadejte jméno, které chcete vyhledat: \n")
        hledej_prijmeni = input("Zadejte příjmení, které chcete vyhledat:\n")
        for pojistenec in seznam_pojistenych:
            if pojistenec.prijmeni == hledej_prijmeni and pojistenec.jmeno == hledej_jmeno:
                    print(pojistenec)
        pokracovat = True
        input("\nPokračujte stisknutím libovolné klávesy...")

    elif akce == 4:
        pokracovat = False
        print("program ukončen")

    else:
        print("zadali jste nesprávnou hodnotu, zadejte číslo v platném rozsahu (1,2,3,4)")
        print("\n")
input()
