# Moduł biblioteka
# Umożliwia tworzenie, czyszczenie i obsługę bazy danych biblioteka.db
# Wymagane moduły:
# sqlite3 - tworzenie i obsługa bazy danych SQL
# prettytable - wyświetlanie wyników zapytań w formie ładnych tabel


import sqlite3
from prettytable import PrettyTable


def stworz_baze_biblioteka():
    con = sqlite3.connect("biblioteka.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE Ksiazki(autor, tytul)")
    except:
        pass
    con.close()


def wyczysc_biblioteke():
    con = sqlite3.connect("biblioteka.db")
    cur = con.cursor()
    try:
        cur.execute("DROP TABLE Ksiazki;")
    except Exception as e:
        print(e)
    con.close()


def dodaj_ksiazke(autor, tytul):
    con = sqlite3.connect("biblioteka.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO Ksiazki VALUES('{autor}', '{tytul}');")
    con.commit()
    con.close()


def szukaj_ksiazki(slowo_klucz):
    con = sqlite3.connect("biblioteka.db")
    cur = con.cursor()
    result = cur.execute(
        f"""
            SELECT autor, tytul
            FROM Ksiazki
            WHERE INSTR(LOWER(autor), LOWER('{slowo_klucz}')) OR
                  INSTR(LOWER(tytul), LOWER('{slowo_klucz}'));
        """
    )
    result = cur.fetchall()
    con.close()
    t = PrettyTable(["Autor", "Tytuł"])
    t.add_rows(result)
    print(t)


def usun_ksiazke(autor, tytul):
    con = sqlite3.connect("biblioteka.db")
    cur = con.cursor()
    cur.execute(
        f"""
            DELETE FROM Ksiazki
            WHERE autor='{autor}' AND
                  tytul='{tytul}';
        """
    )
    con.commit()
    con.close()


def pokaz_ksiazki():
    con = sqlite3.connect("biblioteka.db")
    cur = con.cursor()
    result = cur.execute(
        f"""
            SELECT autor, tytul
            FROM Ksiazki;
        """
    )
    result = cur.fetchall()
    con.close()
    t = PrettyTable(["Autor", "Tytuł"])
    t.add_rows(result)
    print(t)


def start():
    stworz_baze_biblioteka()
    menu = ["1. dodaj", "2. szukaj", "3. usuń", "4. pokaż", "5. wyjdź"]
    while True:
        print(">>MENU<<")
        print(*menu, sep="\n")
        choice = input()
        if choice == "1":
            author = input("Podaj autora książki: ")
            title = input("Podaj tytuł książki: ")
            dodaj_ksiazke(author, title)
        elif choice == "2":
            key_word = input("Wpisz szukaną frazę: ")
            szukaj_ksiazki(key_word)
        elif choice == "3":
            author = input("Podaj autora książki, którą chcesz usunąć: ")
            title = input("Podaj tytuł książki, którą chcesz usunąć: ")
            usun_ksiazke(author, title)
        elif choice == "4":
            pokaz_ksiazki()
        elif choice == "5":
            return


if __name__ == "__main__":
    import sys

    print("Jest to plik modułu biblioteka.")
    print(
        "Zawarty w nim kod nie powinien być uruchamiany jako skrypt, lecz importowany jako moduł."
    )
    input("Naciśnij dowolny klawisz, aby zakończyć działanie programu.")
    sys.exit()
