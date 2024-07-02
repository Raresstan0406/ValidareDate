import csv

#1
def caractere_interzise(c_i, date):
    for cuvant in date:
        for j in cuvant:
            if j in c_i:
                return 1
    return 0
#2
def validare_nume(nume):
    for c in nume:
        if c.isdigit():
            return 1
    return 0
#3
def validare_prenume(date):
    for cuvant in date:
        for c in cuvant:
                return 1
    return 0
#4
def cnp_numar(cnp):
    if not cnp.isnumeric():
        return 1
    return 0
#5
def lunigme_cnp(cnp):
    if len(cnp) != 13:
        return 1
    return 0
#6
def validare_ultima_cifra_cnp(verif, cnp):
    alg = []
    for nr in range(12):
        alg.append(int(cnp[nr]) * int(verif[nr]))
    suma = sum(alg)
    if suma % 11 != int(cnp[12]):
        return 1
    return 0

def validare(dict, date):
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
            dict.update({"Nume ": date[0],
                         "Prenume 1 ": date[1],
                         "Prenume 2": "-",
                         "CNP ": date[2]})
        elif len(date) == 4:
            dict.update({"Nume": date[0],
                         "Prenume 1": date[1],
                         "Prenume 2": date[2],
                         "CNP": date[3]})

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

dict = {}
date = []
cursant = input("Introduceti date cursant:")
impartire_date(cursant, date)
for i in range(len(date)-1):
    if date[i][0]!= date[i][0].upper():
        date[i]= date[i].capitalize()
validare(dict, date)
nume_col=dict.keys()
if dict:
    with open('data.csv', 'a', newline='') as file:
        w = csv.DictWriter(file, fieldnames=nume_col)
        if file.tell() == 0:
            w.writeheader()
        w.writerow(dict)
