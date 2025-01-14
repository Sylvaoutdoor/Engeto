"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Sylva Zemánková
email: don.klokan@seznam.cz

"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


registrovani_uzivatele = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

uzivatel_jmeno = input("Dobrý den, zadejte vaše uživatelské jméno:\n")
uzivatel_heslo = input("Zadejte vaše heslo.\n")

if uzivatel_jmeno in registrovani_uzivatele and registrovani_uzivatele[uzivatel_jmeno] == uzivatel_heslo:
    print(f"Vítejte {uzivatel_jmeno}.\nMůžete analyzovat texty.\nNa výběr máte ze tří textů.")

    
    vyber_textu = input("Jaký text si zvolíte? Napište číslo 1, 2, 3.\n")

    if vyber_textu == "1":
        # počet slov v textu 1
        rozdeleni = TEXTS[0].split()
        pocet_slov = len(rozdeleni)
        print(f"Počet slov textu 1 je: {pocet_slov}")


        # počet slov začínající velkým písmenem
        rozdeleni_1 = TEXTS[0].split()

        velka_pismena = 0
        for slovo in rozdeleni_1:
            if slovo[0].isupper():
                velka_pismena = velka_pismena + 1

        print(f"Počet slov začínající velkým písmenem v textu 1 je: {velka_pismena}")
        

        # počet slov psaných velkými písmeny
        rozdeleni_1 = TEXTS[0].split()

        velka_pismena = 0
        for slovo in rozdeleni_1:
            if slovo.isupper():
                velka_pismena = velka_pismena + 1

        print(f"Počet slov psaných velkým písmenem v textu 1 je: {velka_pismena}")


        # počet slov psaných malými písmeny

        rozdeleni_1 = TEXTS[0].split()

        mala_pismena = 0
        for slovo in rozdeleni_1:
            if slovo.islower():
                mala_pismena = mala_pismena + 1

        print(f"Počet slov psaných malým písmenem v textu 1 je: {mala_pismena}")


        # počet čísel (ne cifer)
        rozdeleni_1 = TEXTS[0].split()
        pocet_cisel = 0

        for cislo in rozdeleni_1:
            spojenec = cislo.strip(",.").replace("N","")
            if spojenec.isdigit():
                pocet_cisel = pocet_cisel + 1
        print(f"Počet čísel v textu 1 je: {pocet_cisel}")



        # sumu všech čísel (ne cifer) v textu
        rozdeleni_1 = TEXTS[0].split()
        soucet_cisel = 0

        for cislo in rozdeleni_1:
            spojenec = cislo.strip(",.").replace("N","")
            if spojenec.isdigit():
                soucet_cisel = soucet_cisel + int(spojenec)

        print(f"Součet všech čísel v textu 1 je: {soucet_cisel}")


        # Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.

        rozdeleni_1 = TEXTS[0].split()
        spojenec = [slovo.strip(",.") for slovo in rozdeleni_1]

        spojenec = [slovo for slovo in spojenec if all(c.isalpha() for c in slovo)]

        delky = {}
        for slovo in spojenec:
            delka = len(slovo)
            if delka in delky:
                delky[delka] = delky[delka] + 1
            else:
                delky[delka] = 1


        print("Sloupcový graf četnosti délek slov v textu 1 je:")
        for delka, cetnost in sorted(delky.items()):
            print(f"{delka:2} | {'*' * cetnost} {cetnost}")



    elif vyber_textu == "2":
        # počet slov v textu 2
        rozdeleni = TEXTS[1].split()
        pocet_slov = len(rozdeleni)
        print(f"Počet slov textu 2 je: {pocet_slov}")

        # počet slov začínající velkým písmenem
        rozdeleni_2 = TEXTS[1].split()

        velka_pismena = 0
        for slovo in rozdeleni_2:
            if slovo[0].isupper():
                velka_pismena = velka_pismena + 1

        print(f"Počet slov začínající velkým písmenem v textu 2 je: {velka_pismena}")


        # počet slov psaných velkými písmeny
        rozdeleni_2 = TEXTS[1].split()

        velka_pismena = 0
        for slovo in rozdeleni_2:
            if slovo.isupper():
                velka_pismena = velka_pismena + 1

        print(f"Počet slov psaných velkým písmenem v textu 2 je: {velka_pismena}")


        # počet slov psaných malými písmeny

        rozdeleni_2 = TEXTS[1].split()

        mala_pismena = 0
        for slovo in rozdeleni_2:
            if slovo.islower():
                mala_pismena = mala_pismena + 1

        print(f"Počet slov psaných malým písmenem v textu 2 je: {mala_pismena}")


        # počet čísel (ne cifer)
        rozdeleni_2 = TEXTS[1].split()
        pocet_cisel = 0

        for cislo in rozdeleni_2:
            spojenec = cislo.strip(",.")
            if spojenec.isdigit():
                pocet_cisel = pocet_cisel + 1
        print(f"Počet čísel v textu 2 je: {pocet_cisel}")



        # sumu všech čísel (ne cifer) v textu
        rozdeleni_2 = TEXTS[1].split()
        soucet_cisel = 0

        for cislo in rozdeleni_2:
            spojenec = cislo.strip(",.")
            if spojenec.isdigit():
                soucet_cisel = soucet_cisel + int(spojenec)

        print(f"Součet všech čísel v textu 2 je: {soucet_cisel}")

        # Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.
        rozdeleni_2 = TEXTS[1].split()
        spojenec = [slovo.strip(",.") for slovo in rozdeleni_2]

        spojenec = [slovo for slovo in spojenec if all(c.isalpha() for c in slovo)]

        delky = {}
        for slovo in spojenec:
            delka = len(slovo)
            if delka in delky:
                delky[delka] = delky[delka] + 1
            else:
                delky[delka] = 1


        print("Sloupcový graf četnosti délek slov v textu 2 je:")
        for delka, cetnost in sorted(delky.items()):
            print(f"{delka:2} | {'*' * cetnost} {cetnost}")
    





    elif vyber_textu == "3":
        # počet slov v textu 3
        rozdeleni = TEXTS[2].split()
        pocet_slov = len(rozdeleni)
        print(f"Počet slov textu 3 je: {pocet_slov}")

        # Počet slov začínající velkým písmenem
        rozdeleni_3 = TEXTS[2].split()

        velka_pismena = 0
        for slovo in rozdeleni_3:
            if slovo[0].isupper():
                velka_pismena = velka_pismena + 1

        print(f"Počet slov začínající velkým písmenem v textu 3 je: {velka_pismena}")

        # počet slov psaných velkými písmeny
        rozdeleni_3 = TEXTS[2].split()

        velka_pismena = 0
        for slovo in rozdeleni_3:
            if slovo.isupper():
                velka_pismena = velka_pismena + 1

        print(f"Počet slov psaných velkým písmenem v textu 3 je: {velka_pismena}")

        # počet slov psaných malými písmeny

        rozdeleni_3 = TEXTS[2].split()

        mala_pismena = 0
        for slovo in rozdeleni_3:
            if slovo.islower():
                mala_pismena = mala_pismena + 1

        print(f"Počet slov psaných malým písmenem v textu 3 je: {mala_pismena}")

        # počet čísel (ne cifer)
        rozdeleni_3 = TEXTS[2].split()
        pocet_cisel = 0

        for cislo in rozdeleni_3:
            spojenec = cislo.strip(",.")
            if spojenec.isdigit():
                pocet_cisel = pocet_cisel + 1
        print(f"Počet čísel v textu 3 je: {pocet_cisel}")

        # sumu všech čísel (ne cifer) v textu
        rozdeleni_3 = TEXTS[2].split()
        soucet_cisel = 0

        for cislo in rozdeleni_3:
            spojenec = cislo.strip(",.")
            if spojenec.isdigit():
                soucet_cisel = soucet_cisel + int(spojenec)

        print(f"Součet všech čísel v textu 3 je: {soucet_cisel}")

        # Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.
        rozdeleni_3 = TEXTS[2].split()
        spojenec = [slovo.strip(",.") for slovo in rozdeleni_3]

        spojenec = [slovo for slovo in spojenec if all(c.isalpha() for c in slovo)]

        delky = {}
        for slovo in spojenec:
            delka = len(slovo)
            if delka in delky:
                delky[delka] = delky[delka] + 1
            else:
                delky[delka] = 1


        print("Sloupcový graf četnosti délek slov v textu 3 je:")
        for delka, cetnost in sorted(delky.items()):
            print(f"{delka:2} | {'*' * cetnost} {cetnost}")

    else:
        print("Zadali jste neplatné číslo nebo jiný znak.\nProgram se ukončuje.")

else:
    print("Dobrý den, vaše uživatelské jméno a heslo nejsou správné.\nProgram se ukončuje.")










