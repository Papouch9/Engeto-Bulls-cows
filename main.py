'''
BULLS AND COWS: druhy projekt do Engeto Online Python Akademie
author: Miroslav Kalík
email: mira.kalik@seznam.cz
discord: mira_47271
'''

import my_game_machine as mgm
import file_manager as fm


def vyber_ukon() -> None:
    """
    Tato funkce umoznuje hraci vybrat, jestli chce hrat novou hru nebo se
    podivat na vysledky. Pokud vybere hru, dostane na vyber obtiznost.
    Pokud chce videt vysledky, dostava na vyber kolik nejlepsich vysledku
    chce videt. Tento pocet se pak zobrazi pro kazdou obtiznost.
    """
    while True:
        volba_ukonu = input("Co chceš udělat? 1: Hrát hru 2: Podívat se na výsledky  ")
        if volba_ukonu == "1":
            vyber_obtiznost()
            break
        elif volba_ukonu == "2":
            while True:
                pocet_pozic = input("Kolik pozic si přeješ zobrazit?")
                try:
                   pocet_pozic = int(pocet_pozic)
                except ValueError:
                    print("Musíš zadat celeé číslo!")
                else:
                    break
            fm.nacti_vysledky(pocet_pozic)
            vyber_ukonceni()
        else:
            print("Máš na výbě jen dvě možnosti 1: Hrát 2: Vidět výsledky!")


def vyber_ukonceni() -> None:
    """
    Tato funkce dava hraci na vyber, jestli chce ve hre pokracovat nebo ji ukoncit
    """
    while True:
        volba_konce = input("Chceš hru zavřít? 1: ano 2: ne  ")
        if volba_konce == "1":
            exit()
        elif volba_konce == "2":
            print("Jedeme znovu")
            vyber_ukon()
        else:
            print("Neplatná volba4")


def vyber_obtiznost() -> None:
    """
    V teto funkci hrac vybira ze tri obtiznosti hry.
    """
    while True:
        vybrana_obtiznost = input("Vyber obtížnost: 1: lehká 2: střední 3: těžká  ")
        if vybrana_obtiznost.isdigit():
            vybrana_obtiznost = int(vybrana_obtiznost)
            if vybrana_obtiznost > 0 and vybrana_obtiznost < 4:
                jmeno_hrace = input("Zadej jméno hráče: ")
                ziskana_tajenka = mgm.vytvor_tajenku(vybrana_obtiznost)
                tahu, herni_cas = mgm.hraj(ziskana_tajenka)
                fm.uloz_vysledek(jmeno_hrace, vybrana_obtiznost, tahu, herni_cas)
                vyber_ukonceni()
                break
            else:
                print("Musíš zadat obtížnost jako číslo 1, 2 nebo 3")
        else:
            print("Obtížnost musí být zadaná jako číslice!")


if __name__ == "__main__":
    print("Vítej ve hře BULLS and COWS")
    vyber_ukon()
