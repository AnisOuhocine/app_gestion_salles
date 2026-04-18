# fichier en préparation

class Salle :
    def __init__(self, code,libelle,type,capacite):
        self.code=code
        self.libelle=libelle
        self.type=type
        self.capacite=capacite

    def afficher_infos(self):
        print(f"code : {self.code}")
        print(f" libelle : {self.libelle}")
        print(f" type : {self.type}")
        print(f" capacite : {self.capacite}")


