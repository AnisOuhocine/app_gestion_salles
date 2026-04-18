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
