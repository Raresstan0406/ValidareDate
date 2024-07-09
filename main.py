import csv
import datetime
import os


# 1
def caractere_interzise(c_i, date):
    for cuvant in date:
        for j in cuvant:
            if j in c_i:
                return 1
    return 0


# 2
def validare_nume(nume):
    for c in nume:
        if c.isdigit():
            return 1
    return 0


# 3
def validare_prenume(date):
    for cuvant in date:
        for c in cuvant:
            if c.isdigit():
                return 1
    return 0


# 4
def cnp_numar(cnp):
    if not cnp.isnumeric():
        return 1
    return 0


# 5
def lunigme_cnp(cnp):
    if len(cnp) != 13:
        return 1
    return 0


# 6
def validare_ultima_cifra_cnp(verif, cnp):
    alg = []
    for nr in range(12):
        alg.append(int(cnp[nr]) * int(verif[nr]))
    suma = sum(alg)
    cifra_control = suma % 11
    if cifra_control == 10:
        cifra_control = 1
    if cifra_control != int(cnp[12]):
        return 1
    return 0


def validare(index, dict, date):
    ok = 0
    if caractere_interzise('+@!?\/', date) == 1:
        print("Datele contin caractere interzise")
        ok = 1
    if validare_nume(date[0]) == 1:
        print("Numele nu este valid")
        ok = 1
    if validare_prenume(date[1:-1]) == 1:
        print("Prenumele nu este valid")
        ok = 1
    if cnp_numar(date[-1]) == 1:
        print("CNP-ul nu este un numar")
        ok = 1
    elif lunigme_cnp(date[-1]) == 1:
        print("Lungimea CNP-ului este incorecta")
        ok = 1
    elif validare_ultima_cifra_cnp('279146358279', date[-1]) == 1:
        print("CNP-ul nu este valid")
        ok = 1
    if ok == 0:
        if len(date) == 3:
            dict.update({"ID ": index,
                         "Nume ": date[0],
                         "Prenume 1 ": date[1],
                         "Prenume 2 ": "-",
                         "CNP ": date[2]})
        elif len(date) == 4:
            dict.update({"ID ": index,
                         "Nume ": date[0],
                         "Prenume 1 ": date[1],
                         "Prenume 2 ": date[2],
                         "CNP ": date[3]})


def impartire_prenume(prenume, p):
    if '-' in prenume:
        impartire = prenume.split('-')
        for cuv in impartire:
            p.append(cuv)
    else:
        p.append(prenume)


def impartire_date(cursant, date):
    date_prime = cursant.split(' ')
    if len(date_prime) == 3:
        date.append(date_prime[0])
        impartire_prenume(date_prime[1], date)
        date.append(date_prime[-1])
    else:
        for cuv in date_prime:
            date.append(cuv)


def delete(lista):
    how_to = input("dupa ID/CNP:")
    if how_to == "ID":
        cursant_pt_sters = input("ID cursant: ")
        for cursant in lista:
            if cursant["ID "] == int(cursant_pt_sters):
                    lista.remove(cursant)
                    garbage.append(cursant)
    elif how_to == "CNP":
        cursant_pt_sters = input("CNP cursant: ")
        for cursant in lista:
            if cursant["CNP "] == cursant_pt_sters:
                lista.remove(cursant)
                garbage.append(cursant)
def saved_csv(director, lista, date_curente):
    director_csv = os.path.join(director, f'{date_curente}.csv')
    for dictionar in lista:
        nume_col = dictionar.keys()
        if dictionar:
            with open(director_csv, 'a', newline='') as file:
                w = csv.DictWriter(file, fieldnames=nume_col)
                if file.tell() == 0:
                    w.writeheader()
                w.writerow(dictionar)
    lista.clear()


def saved_txt(director, lista, date_curente):
    director_txt = os.path.join(director, f'{date_curente}.txt')
    for dictionar in lista:
        nume_col = dictionar.keys()
        if dictionar:
            with open(director_txt, 'a', newline='') as file:
                if file.tell() == 0:
                    header = ' | '.join(nume_col) + '\n'
                    file.write(header)
                row = ' | '.join(str(dictionar[field]) for field in nume_col) + '\n'
                file.write(row)
    lista.clear()

def SAVE(director, lista):
    timestamp = datetime.datetime.now()
    date_curente = f'Lista_cursanti_{timestamp.date().year}_{timestamp.date().month}_{timestamp.date().day}_' \
                   f'{timestamp.time().hour}_{timestamp.time().minute}'
    decizie = input("Tip fisier: TXT/CSV: ")
    if decizie == "CSV":
        saved_csv(director, lista, date_curente)
    if decizie == "TXT":
        saved_txt(director, lista, date_curente)

lista_gata_salvare = []
lista_update = []
lista = []
director = r"C:\Users\RARES\Desktop\date_cursanti"
lista_fisiere = os.listdir(director)
index = 1
garbage = []
while True:
    dict = {}
    date = []
    lista_fisiere = os.listdir(director)
    if not lista:
        if lista_fisiere:
            cale_completa = os.path.join(director, lista_fisiere[-1])
            print(cale_completa)
            with open(cale_completa, 'r') as fisier_dorit:
                if '.txt' in cale_completa:
                    fisier_dorit_split = fisier_dorit.read().splitlines()
                    ultimul_rand = fisier_dorit_split[-1]
                    ultimul_rand_split = ultimul_rand.split(" | ")
                    index = int(ultimul_rand_split[0]) + 1
                elif '.csv' in cale_completa:
                    citire = csv.DictReader(fisier_dorit)
                    for rand in citire:
                        ultimul_rand = rand
                    index = int(ultimul_rand["ID "]) + 1
    cursant = input("Introduceti date cursanti sau una din comenzile EXIT/SAVE/DELETE/GARBAGE:")
    if cursant == "EXIT":
        break
    elif cursant == "SAVE":
        SAVE(director, lista)
    elif cursant == "DELETE":
        delete(lista)
    elif cursant == "GARBAGE":
        director_garbage = os.path.join(director, 'garbage.csv')
        for dictionar in garbage:
            nume_col = dictionar.keys()
            if dictionar:
                with open(director_garbage, 'a', newline='') as file:
                    w = csv.DictWriter(file, fieldnames=nume_col)
                    if file.tell() == 0:
                        w.writeheader()
                    w.writerow(dictionar)
    else:
        impartire_date(cursant, date)
        for i in range(len(date) - 1):
            if date[i][0] != date[i][0].upper():
                date[i] = date[i].capitalize()
        validare(index, dict, date)
        if dict:
            index = index + 1
        lista.append(dict)
        print(lista)
