import customtkinter as ctk

#fonction pour le calcul
def calculate_weight():
    volume = float(volume_entry.get()) # Get the volume from the entry field
    material = material_var.get() # Get the selected material from the combobox

    if material == "Glass":
        density = 2500 # Density of glass in kg/m^3
    elif material == "Plastic":
        density = 1400 # Density of plastic in kg/m^3

    weight = (density * volume) / 1000 # Convert m^3 to L and then convert kg to g
    result_label.configure(text=f"The weight of the glass is {weight} grams.")

ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("400x200")
app.title("Weight Calculator")

frame = ctk.CTkFrame(app)
frame.pack(padx=10, pady=10)

# Label and entry field for volume
volume_label = ctk.CTkLabel(frame, text="Enter the volume of the glass (in milliliters):")
volume_label.grid(row=0, column=0, padx=(0, 10), sticky=ctk.W)
volume_entry = ctk.CTkEntry(frame, width=10)
volume_entry.grid(row=0, column=1, padx=(0, 10))

# Combo box for selecting the material
material_options = ["Glass", "Plastic"]
material_var = ctk.StringVar(app)
material_var.set(material_options[0]) # Set default value

material_label = ctk.CTkLabel(frame, text="Select the material of the glass:")
material_label.grid(row=1, column=0, padx=(0, 10), sticky=ctk.W)
material_combo = ctk.CTkComboBox(frame, values=material_options, variable=material_var)
material_combo.grid(row=1, column=1, padx=(0, 10))

# Button to trigger calculation
calculate_button = ctk.CTkButton(frame, text="Calculate Weight", command=calculate_weight)
calculate_button.grid(row=2, columnspan=2, pady=(10, 0))


result_label = ctk.CTkLabel(frame, text="")
result_label = ctk.CTkLabel(fg="red")
result_label.grid(row=3, columnspan=2, pady=(10, 0))

app.mainloop()
