#MON APPLICATION
import customtkinter as ctk
from sympy import latex

#fonction pour le calcul
def calcul_poids():
    Lv = float(Lv_entry.get()) # Concerne la largeur du vitrage
    Hv = float(Hv_entry.get()) # Concerne la hauteur du vitrage
    ep = float(ep_entry.get()) # Concerne l'épaisseur du vitrage
    densite = 2.5
    S = (Lv * Hv)/1000000
    result_label2.configure(text=f"La surface du vitrage est de: {S} m\u00b2")
    ctk.set_default_color_theme("green")

    Volume = (Lv/1000) * (Hv/1000) * ep
    Pv = Volume * densite

    result_label.configure(text=f"Le poids du vitrage est de: {Pv} Kg")
    ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("900x400")
app.title("Calcule du poids d'un vitrage")

frame = ctk.CTkFrame(app)
frame.pack(padx=10, pady=10)

# données pour la largeur
Lv_label = ctk.CTkLabel(frame, font=("Arial",20), text="Indiquer la largeur du vitrage en mm:")
Lv_label.grid(row=0, column=0, padx=(0, 10), sticky=ctk.W)
Lv_entry = ctk.CTkEntry(frame, width=100, font=("Arial",25),fg_color=("yellow"))
Lv_entry.grid(row=0, column=1, padx=(0, 10))


# données pour la hauteur 
Hv_label = ctk.CTkLabel(frame, font=("Arial",20),text="Indiquer la hauteur du vitrage en mm:")
Hv_label.grid(row=1, column=0, padx=(0, 10), sticky=ctk.W)
Hv_entry = ctk.CTkEntry(frame, width=100, font=("Arial",25),fg_color=("green"))
Hv_entry.grid(row=1, column=1, padx=(0, 10))


# données pour l'épaisseur 
ep_label = ctk.CTkLabel(frame, font=("Arial",20),text="Indiquer l'épaisseur total de verre en mm:")
ep_label.grid(row=2, column=0, padx=(0, 10), sticky=ctk.W)
ep_entry = ctk.CTkEntry(frame, width=100, font=("Arial",25),fg_color=("pink")) 
ep_entry.grid(row=2, column=1, padx=(0, 10))



frame = ctk.CTkFrame(app)
frame.pack(padx=10, pady=10)

#Bouton pour calculer.
calculate_button = ctk.CTkButton(frame, font=("Arial",30),text="Calcul du poids", command=calcul_poids)
calculate_button.grid(row=2, columnspan=2, pady=(10,20))


result_label = ctk.CTkLabel(frame,font=("Webdings",20), fg_color="red", text="")
result_label.grid(row=3, columnspan=2, pady=(30,20))

result_label2 = ctk.CTkLabel(frame,font=("Webdings",20), fg_color="green", text="")
result_label2.grid(row=4, columnspan=2, pady=(20,00))


app.mainloop()
