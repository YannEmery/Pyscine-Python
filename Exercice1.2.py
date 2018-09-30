import math
import sys
from datetime import datetime

import substring as substring

#Méthode qui permet la vérification d'une date
def VerifDate(date):
    date_format = '%d/%m/%Y'
    my_date = date
    try:
        valid_date = datetime.strptime(my_date,date_format)
    except ValueError:
        print('%s n est pas une date valide !' % my_date)
        return 0

#Méthode qui ajoute en fonction du mois de la date
def AjoutMois(mois):
    if mois == "1" or mois == "01" or mois == "10":
        moisretour = 0
    elif mois == "2" or mois == "02" or mois == "3" or mois == "03" or mois == "11":
        moisretour = 3
    elif mois == "4" or mois == "04" or mois == "7" or mois == "07":
        moisretour = 6
    elif mois == "5" or mois == "05":
        moisretour = 1
    elif mois == "6" or mois == "06":
        moisretour = 4
    elif mois == "08" or mois == "8":
        moisretour = 2
    else:
        moisretour = 5
    return  moisretour

#Méthode qui permet de savoir si l'année est Bissextile
def Bissextile(annee):
    verifannee = False
    quart = int(annee) / 4
    verifquart = isinstance(quart, int)
    if verifquart == False:
        return verifannee
    else:
        divisecent = int(annee) / 100
        verifcent = isinstance(divisecent, int)
        if verifcent == True:
            divise4cent = int(annee) / 400
            verif4cent = isinstance(divise4cent, int)
            if verif4cent == False:
                return verifannee
            else:
                verifannee = True
                return verifannee
        else:
            return verifannee

#Méthode qui permet d'ajouter en fonction du siècle de la date
def Siecle(annee):
    siecle = annee[0:2]
    anneeajout = 0
    if siecle == "16" or siecle == "20":
        anneeajout = 6
    elif siecle == "17" or siecle == "21":
        anneeajout = 4
    elif siecle == "18":
        anneeajout = 2
    else:
        anneeajout = 0
    return anneeajout

#Méthode qui donne le jour de la semaine
def JourSemaine(ajout):
    ajout = ajout % 7
    if ajout == 0:
        result = "Dimanche"
    elif ajout == 1:
        result = "Lundi"
    elif ajout == 2:
        result = "Mardi"
    elif ajout == 3:
        result = "Mercredi"
    elif ajout == 4:
        result = "Jeudi"
    elif ajout == 5:
        result = "Vendredi"
    else:
        result = "Samedi"
    return result

#Méthode qui identifie le mois entré par l'utillisateur
def Mois(mois):
    if mois == "janvier" or mois == "Janvier" or mois == "1" or mois == "01":
        moisnumero = "1"
    elif mois == "fevrier" or mois == "Fevrier" or mois == "février" or mois == "Février" or mois == "2" or mois == "02":
        moisnumero = "2"
    elif mois == "mars" or mois == "Mars" or mois == "3" or mois == "03":
        moisnumero = "3"
    elif mois == "avril" or mois == "Avril" or mois == "4" or mois == "04":
        moisnumero = "4"
    elif mois == "mai" or mois == "Mai" or mois == "5" or mois == "05":
        moisnumero = "5"
    elif mois == "juin" or mois == "Juin" or mois == "6" or mois == "06":
        moisnumero = "6"
    elif mois == "juillet" or mois == "Juillet" or mois == "7" or mois == "07":
        moisnumero = "7"
    elif mois == "aout" or mois == "Aout" or mois == "août" or mois == "Août" or mois == "8" or mois == "08":
        moisnumero = "8"
    elif mois == "septembre" or mois == "Septembre" or mois == "9" or mois == "09":
        moisnumero = "9"
    elif mois == "octobre" or mois == "Octobre" or mois == "10":
        moisnumero = "10"
    elif mois == "novembre" or mois == "Novembre" or mois == "11":
        moisnumero = "11"
    elif mois == "decembre" or mois == "Decembre" or mois == "décembre" or mois == "Décembre" or mois == "12":
        moisnumero = "12"
    else:
        return False
        brake
    return moisnumero

#Méthode qui vérifie si les valeurs sont bien entrées par l'utilisateur
def VerifDateEntiere(jour,mois,annee):
    if jour == "":
        message = "Le jour n'est pas renseigné"
        verif = 1
    else:
        verif = 0
    if mois == "" and verif == 1:
        message = "Ni le jour, ni le mois ne sont renseignés"
        verif2 = 1
    elif mois == "" and verif == 0:
        message = "Le mois n'est pas renseigné"
        verif2 = 1
    else:
        verif2 = 0
    if annee == "" and verif == 1 and verif2 == 0:
        message = "Ni le jour, ni l'année ne sont renseignés"
    elif annee == "" and verif2 == 1 and verif == 0:
        message = "Ni le mois, ni l'année ne sont renseignés"
    elif annee == "" and verif == 1 and verif2 == 1:
        message = "Ni le jour, ni le mois, ni l'année ne sont renseignés"
    elif annee == "" and verif == 0 and verif2 == 0:
        message = "L'année n'est pas renseignée"
    if annee != "" and verif == 0 and verif2 == 0:
        message = ""
    return message



#On demande à l'utilisteur d'entrer une date
jour_input = input("Entrez le jour du mois : ")
mois_input = input("Entrez le mois de l'année : ")
annee_input = input("Entrez l'année : ")

message = VerifDateEntiere(jour_input,mois_input,annee_input)
if message != "":
    print(message)
    sys.exit()

moisnumero = Mois(mois_input)
if moisnumero == False:
    print("Le mois entré n'est pas valide")
    sys.exit()

#Construction d'une chaine sous le format jj/mm/aaaa pour vérification de la date
date = jour_input + "/" + moisnumero + "/" + annee_input
if VerifDate(date) == 0:
    sys.exit()
elif int(annee_input) < 1600 or int(annee_input) > 2199:
    print("La date doit se situer entre 1600 et 2200")
    sys.exit()
else:
    #On garde les deux derniers chiffres de l'année
    annee = annee_input[2:]

    #On divise par 4 et garde la partie entière
    ajout = int(annee) + int(annee) / 4
    ajout = math.floor(ajout)

    #On ajoute la journée du mois
    ajout = ajout + int(jour_input)

    #On ajoute le numéro attribué au mois
    moisretour = AjoutMois(moisnumero)
    ajout = ajout + moisretour

    #On retire 1 si l'année est Bissextile et le mois est janvier ou février
    if int(moisnumero) == 1 or int(moisnumero) == 2:
        verification = "vrai"
    else:
        verification = "faux"
    if Bissextile(annee_input) == True and verification == "vrai":
        ajout = ajout - 1

    anneeajout = Siecle(annee_input)
    ajout = ajout + anneeajout
    result = JourSemaine(ajout)

    #On affiche le jour de la semaine
    print("Le jour de la semaine est : ",result)

#Yann EMERY