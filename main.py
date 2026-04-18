# fichier en préparation
# Etape 3 : Initialisation de l architecture en couches et installation des dependances

from data.dao_salle import DataSalle

dao = DataSalle()
salle= dao.get_salle("S100")
if salle is not None:
    salle.afficher_infos()
else:
    print("Salle non trouvee")