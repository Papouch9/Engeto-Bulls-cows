import datetime


def uloz_vysledek(jmeno: str, obtiznost: int, tahy: int, cas: int) -> None:
    """
    Tato funkce uklada vysledky hry do konktetniho souboru podle toho, jakou
    obtiznost hrac hral. Hracovo skore je vypocitano jako nasobek poctu tipu
    a delky hry. Je cilem dosahovat co nejnissiho skore.
    """
    match obtiznost:
        case 1:
            jmeno_souboru = "easy.txt"
        case 2:
            jmeno_souboru = "medium.txt"
        case 3:
            jmeno_souboru = "hard.txt"

    with open(jmeno_souboru, mode="a") as soubor:
        skore = tahy * cas
        zapis = str(skore) + " " + str(tahy) + " " + str(cas) + " " + str(jmeno) + " " + str(datetime.datetime.now().date()) + "\n"
        soubor.write(zapis)

def nacti_vysledky(pocet_top_hracu: int) -> None:
    """
    Tato funkce nacita uzivateli vysledky odehranych her. V textovych souborech
    jsou vysledky ulozeny chronologicky. Az pri nacteni jsou serazeny vzestupne
    podle skore a je vybran pocet zobrazenych vysledku podle prani hrace pro
    kazdou obtiznost hry.
    """
    soubory = ("easy.txt", "medium.txt", "hard.txt")

    for i in soubory:
        vysledky_k_serazeni = {}
        print(f"TOP {pocet_top_hracu} výsledků na úrovni {i.strip(".txt")}")

        with open(i, mode="r") as obtiznost:
            jednotlive_vysledky = obtiznost.readlines()

            for j in range(len(jednotlive_vysledky)):
                skore, tahu, cas, nick, datum = jednotlive_vysledky[j].split(" ")
                vysledky_k_serazeni[int(skore)] = {"jmeno_hrace": nick, "pocet_tahu": tahu, "cas_hry": str(datetime.timedelta(seconds=int(cas))), "odehrano": datum,
                                                   "skore": skore}
                poradi_vysledku = list(vysledky_k_serazeni.keys())
                poradi_vysledku = sorted(poradi_vysledku)

            for k in range(0, pocet_top_hracu):
                try:
                    vysledky_k_serazeni[poradi_vysledku[k]]
                except:
                    print(f"{k + 1}. Pozice neobsazena")
                else:
                    print(f"{k + 1}. Jméno: {vysledky_k_serazeni[poradi_vysledku[k]]["jmeno_hrace"]},"
                          f"počet tahů: {vysledky_k_serazeni[poradi_vysledku[k]]["pocet_tahu"]},"
                          f"čas hry: {vysledky_k_serazeni[poradi_vysledku[k]]["cas_hry"]},"
                          f"odehráno: {vysledky_k_serazeni[poradi_vysledku[k]]["odehrano"]}", end="")
