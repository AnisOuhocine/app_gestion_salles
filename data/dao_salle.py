import json
import mysql.connector
from models.salle import Salle
class DataSalle:
    def get_connection(self):
        with open("./data/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        con = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return con

    def insert_salle(self, salle):
        con = self.get_connection()
        curseur = con.cursor()
        requete = "INSERT INTO salle(code, libelle, type, capacite) VALUES(%s, %s, %s, %s)"
        valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)
        curseur.execute(requete, valeurs)
        con.commit()
        curseur.close()
        con.close()

    def delete_salle(self, code):
        con = self.get_connection()
        curseur = con.cursor()

        requete = "DELETE FROM salle WHERE code = %s"
        curseur.execute(requete, (code,))
        con.commit()
        curseur.close()
        con.close()

    def update_salle(self, salle):
        con = self.get_connection()
        curseur = con.cursor()

        requete = "UPDATE salle SET libelle = %s, type = %s, capacite = %s WHERE code = %s"
        valeurs = (salle.libelle, salle.type, salle.capacite, salle.code)
        curseur.execute(requete, valeurs)
        con.commit()
        curseur.close()
        con.close()

    def get_salle(self, code):
        con = self.get_connection()
        curseur = con.cursor()

        requete= "SELECT * FROM salle WHERE code = %s"
        curseur.execute(requete,(code,))
        resultat=curseur.fetchone()

        curseur.close()
        con.close()

        if resultat :
            return Salle(resultat[0],resultat[1],resultat[2],resultat[3])
        else:
            return None


    def get_salles(self):
        con = self.get_connection()
        curseur = con.cursor()

        requete = "SELECT *FROM salle"
        curseur.execute(requete)
        resultats = curseur.fetchall()
        curseur.close()
        con.close()
        liste_salles=[]
        for ligne in resultats :
            salle = Salle(ligne[0],ligne[1],ligne[2],ligne[3])
            liste_salles.append(salle)

        return liste_salles