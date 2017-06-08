# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Window Interface with tkinter modul.
IN PROGRESS 
"""

import os
import main 
from tkinter import *

# Création de la fenêtre principale (main window)
wi = Tk()
wi.geometry('300x100+400+400')

# Création d'un widget Label (texte 'Bonjour tout le monde !')
title = Label(wi, text = 'Kilauea Project !', fg = 'red')
# Positionnement du widget avec la méthode pack()
title.pack()

# Création d'un widget Button (bouton Lancer)
go = Button(wi, text ='Run', command = main.main())
# Positionnement du widget avec la méthode pack()
go.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Quitter)
close = Button(wi, text = 'Close', command = wi.destroy)
close.pack()

# Création d'un widget Label (texte 'Résultat -> x')
result = Label(wi, textvariable = Texte, fg ='red', bg ='white')
result.pack(side = LEFT, padx = 5, pady = 5)

# Lancement du gestionnaire d'événements
wi.mainloop()





