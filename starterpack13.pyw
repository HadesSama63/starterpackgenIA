import tkinter as tk
from tkinter import PhotoImage, filedialog
import webbrowser

def generate_prompt():
    prompt_template = """Crée un rendu 3D de haute qualité d'une figurine en style cartoon, présentée sous blister, à la manière d'un jouet de collection. Le fond en carton est {couleur} et porte une étiquette de jouet rétro. En haut au centre, en grandes lettres majuscules et en gras, dans un cadre jaune au contour noir, écris "{titre}". Juste en dessous, tu peux écrire {nom} en plus petit en bas à droite. En haut à droite, un badge bleu circulaire indique "{role}". En haut à gauche, une petite bulle blanche indique "{pegi}".
Le personnage se tient debout, moulé dans une boîte en plastique transparente fixée sur un support en carton plat. Il doit ressembler à la photo que je joins. Son visage est {visage}, avec une pose {pose}. Le ton général est léger et réaliste.
La figurine porte {vetements}. Sur le côté de la figurine, intégrés dans des moules en plastique distincts, expose 3 accessoires miniatures : {accessoire1}, {accessoire2}, {accessoire3}. Chaque accessoire s'insère parfaitement dans son propre compartiment moulé.
L'emballage est photographié ou rendu avec des ombres douces, un éclairage uniforme et un fond blanc épuré pour donner l'impression d'une séance photo commerciale. Le style doit allier réalisme et stylisation du dessin animé 3D, à l'image de Pixar ou des maquettes de jouets modernes. Assure-toi que la disposition et les proportions du produit ressemblent à celles d'un véritable jouet vendu en magasin."""

    prompt = prompt_template.format(
        couleur=entries["Couleur"].get(),
        titre=entries["Titre"].get(),
        nom=entries["Nom"].get(),
        role=entries["Rôle"].get(),
        pegi=entries["PEGI"].get(),
        visage=entries["Visage"].get(),
        pose=entries["Pose"].get(),
        vetements=entries["Vêtements"].get(),
        accessoire1=entries["Accessoire 1"].get(),
        accessoire2=entries["Accessoire 2"].get(),
        accessoire3=entries["Accessoire 3"].get()
    )

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, prompt)
    
    # Demande à l'utilisateur de choisir le nom et l'emplacement du fichier
    fichier_sauvegarde = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                       filetypes=[("Fichiers texte", "*.txt")], 
                                                       title="Enregistrer le fichier")
    if fichier_sauvegarde:
        with open(fichier_sauvegarde, "w", encoding="utf-8") as fichier:
            fichier.write(prompt)

def check_updates():
    webbrowser.open("https://github.com/HadesSama63/starterpackgenIA")

root = tk.Tk()
root.title("Starter Pack IA Generator 1.3")
root.geometry("800x600")

# Ajout du fond d'écran
background_image = PhotoImage(file="backstarter.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

labels = ["Couleur", "Titre", "Nom", "Rôle", "PEGI", "Visage", "Pose", "Vêtements", "Accessoire 1", "Accessoire 2", "Accessoire 3"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(frame, text=label, bg="white", font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(frame, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry  # Utilisation des clés avec majuscules

# Zone d'affichage du prompt généré
result_text = tk.Text(frame, height=10, width=60, font=("Arial", 12))
result_text.grid(row=len(labels) + 2, columnspan=2, pady=10)

# Bouton de génération
generate_button = tk.Button(frame, text="Générer et enregistrer", font=("Arial", 12), command=generate_prompt)
generate_button.grid(row=len(labels), column=1, pady=10)

# Bouton de recherche de mise à jour
update_button = tk.Button(frame, text="Rechercher mise à jour", font=("Arial", 12), command=check_updates)
update_button.grid(row=len(labels) + 1, column=1, pady=10)

root.mainloop()


