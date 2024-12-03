from datetime import *
class Titulaire :
    def __init__(self,nom,prenom):
        self.__nom = nom
        self.__prenom = prenom

    @property
    def nom(self):
        return   self.__nom
    @nom.setter
    def nom(self,nouvelleNom):
        self.__nom = nouvelleNom

    @property
    def prenom(self):
        return self.__nom
    @prenom.setter
    def prenom(self, nouvellePrenom):
        self.__nom = nouvellePrenom

    def __str__(self):
        return (f"le nom :{self.__nom}\n"
                f"le prenom : {self.__prenom}")

class CompteBancaire :
    __auto = 0
    def __init__(self , titulaire , dateCeaction , sold = 0 , decouvertAutoriser = 0 ):
        CompteBancaire.__auto += 1
        self.__numero =  CompteBancaire.__auto
        self.__titulaire = titulaire
        self.__datecreation =  datetime.strptime(dateCeaction, "%d/%m/%Y")
        self.__solde = sold
        self.__decouvertAutoriser = decouvertAutoriser

    @property
    def titulaire(self):
        return self.__numero
    @titulaire.setter
    def titulaire(self, nouveautitule):
        self.__titulaire = nouveautitule

    @property
    def datecreation(self):
        return  self.__datecreation
    @datecreation.setter
    def datecreation(self, nouvelleDate):
        self.__datecreation = nouvelleDate

    @property
    def solde(self):
        return self.__solde
    @solde.setter
    def solde(self, nouveauSolde):
        self.__solde = nouveauSolde

    def depot(self,montant):
        if montant > 0:
            self.__solde += montant
            return (f"Le montant depot est [{montant}DH ], solde est [{self.__solde} DH]")
        return (f"le montant est n'est pas en depot")

    def retrait(self,montant):
        if montant > 0 :
            if self.__solde >= montant :
               self.__solde -= montant
            return (f"le montant retrait est [{montant}DH] , solde est [{self.solde} DH]")
        return (f"le montant n'est pas e retrait")

    def decouverAutoriser(self,montant):
        if montant > 0 :
            self.__solde += montant
            return self.__solde
        return (f"le decouvert autorisé ne peut pas etre negatif ")

    def __str__(self):
        return(f"Titulaire : { self.__titulaire }\n"
               f"la date de creation : {self.__datecreation}\n"
               f" le solde initiale : { self.__solde}DH\n"
               f"le depot : {self.depot(400)}\n"
               f"retrait : {self.retrait(100)}\n"
               f"le decouvert : {self.decouverAutoriser} DH")

T1 = Titulaire("meriem","moukrim")
print(T1)
C1 = CompteBancaire("meriem moukrim ","08/05/2025",8000)
print(C1)














