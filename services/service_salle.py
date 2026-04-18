# fichier en préparation

from data.dao_salle import DataSalle
from models.salle import Salle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()
    def ajouter_salle(self,salle):
        if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
            return False, "Tous les champs sont obligatoires"
        if salle.capacite < 1 :
            return False, "La capacite doit etre superieure ou egale 1"
        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutee avec succes"
