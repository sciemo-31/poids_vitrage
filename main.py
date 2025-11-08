#Calcul poids du vitrage

Lv = int(input("indiquer la largeur du vitrage en mm: "))
Hv = int(input("indiquer la hauteur du vitrage en mm: "))
ep = int(input("indiquer l' épaisseur totale de verre en mm: "))
densite = 2.5

Surface = (Lv * Hv)/1000000
volume = (Lv/1000) * (Hv/1000) * ep
Pv = volume * densite

#Affichage des résultats
print("surface de vitrage (en m²): " +str(Surface))
print("Poids du vitrage (en Kg): {0:.2f} ".format (Pv))
