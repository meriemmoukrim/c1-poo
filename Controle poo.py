from datetime import datetime

class Titulaire:
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nouvelleNom):
        self.__nom = nouvelleNom

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, nouvellePrenom):
        self.__prenom = nouvellePrenom

    def __str__(self):
        return f"le nom : {self.__nom}\nle prenom : {self.__prenom}"

class CompteBancaire:
    __auto = 0

    def __init__(self, titulaire, dateCreation, solde=0, decouvertAutorise=0):
        CompteBancaire.__auto += 1
        self.__numero = CompteBancaire.__auto
        self.__titulaire = titulaire
        self.__dateCreation = datetime.strptime(dateCreation, "%d/%m/%Y")
        self.__solde = solde
        self.__decouvertAutorise = decouvertAutorise

    @property
    def titulaire(self):
        return self.__titulaire

    @titulaire.setter
    def titulaire(self, nouveautitule):
        self.__titulaire = nouveautitule

    @property
    def dateCreation(self):
        return self.__dateCreation

    @dateCreation.setter
    def dateCreation(self, nouvelleDate):
        self.__dateCreation = nouvelleDate

    @property
    def solde(self):
        return self.__solde

    @solde.setter
    def solde(self, nouveauSolde):
        self.__solde = nouveauSolde

    def depot(self, montant):
        if montant > 0:
            self.__solde += montant
            return f"Le montant déposé est [{montant} DH], solde est [{self.__solde} DH]"
        return "Le montant n'est pas valide pour un dépôt"

    def retrait(self, montant):
        if montant > 0:
            if self.__solde >= montant:
                self.__solde -= montant
                return f"Le montant retiré est [{montant} DH], solde est [{self.__solde} DH]"
            return f"Solde insuffisant pour un retrait de [{montant} DH]"
        return "Le montant n'est pas valide pour un retrait"

    def decouvertAutorise(self, montant):
        if montant >= 0:
            self.__decouvertAutorise = montant
            return f"Le découvert autorisé est de [{self.__decouvertAutorise} DH]"
        return "Le découvert autorisé ne peut pas être négatif"

    def __str__(self):
        return (f"° Titulaire : {self.__titulaire}\n"
                f"° Date de création : {self.__dateCreation}\n"
                f"° Solde initial : {self.__solde} DH\n"
                f"° {self.depot(400)}\n"
                f"° {self.retrait(100)}\n"
                f"° {self.decouvertAutorise(500)}\n")

# Test
T1 = Titulaire("Meriem", "Moukrim")
print(T1)
C1 = CompteBancaire(T1, "08/05/2025", 8000)
print(C1)


  












