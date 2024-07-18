import random
import datetime


def vytvor_tajenku(obtiznost: int) -> list:
    """
    Tato funkce vytvori tajenku podle zadane obtiznost. Budeme hadat 4-6 cislic.
    """
    zasobnik = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    tajenka = []
    for i in range(0, 3 + obtiznost):
        if i == 0:
            vybrana_cislice = random.choice(zasobnik[1:len(zasobnik) + 1])
        else:
            vybrana_cislice = random.choice(zasobnik)
        tajenka.append(vybrana_cislice)
        zasobnik.remove(vybrana_cislice)
    return tajenka


def hraj(hledane: list) -> int:
    """
    Tady probíha samotna hra. Funkce vraci pocet typu a ceklovy cas hry v sekundach.
    """
    sekvence = []
    hledane = list(hledane)
    print(f"Hledáme sekvenci {len(hledane)} číslic")
    start = datetime.datetime.now()
    pokus = 0

    while True:
        tip = input("Zadej svůj tip: ")
        if not tip.isdigit():
            print("Musíš zadat pouze číslice!")
            continue
        else:
            if len(tip) != len(hledane):
                print("Zadal jsi špatnou délku slova!")
                continue
            else:
                pokus += 1
                kravy = 0
                byci = 0
                slovo_byci = "BULLS"
                slovo_kravy = "COWS"

                for x in tip:
                    sekvence.append(int(x))

                for j in range(len(hledane)):
                    if sekvence[j] == hledane[j]:
                        byci += 1
                for i in sekvence:
                    if i in hledane:
                        kravy += 1

                kravy -= byci
                if kravy < 0:
                    kravy = 0

                if kravy == 1:
                    slovo_kravy = "COW"
                if byci == 1:
                    slovo_byci = "BULL"

                print(byci, slovo_byci, kravy, slovo_kravy)

        if byci == len(hledane):
            konec = datetime.datetime.now()
            break

        else:
            byci = 0
            kravy = 0
            sekvence = []

    cas_hry = (konec - start).seconds
    print(f"DOBRÁ PRÁCE, POKUSY: {pokus} ČAS: {datetime.timedelta(seconds=cas_hry)}")
    return pokus, cas_hry


