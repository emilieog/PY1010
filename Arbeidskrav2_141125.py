# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 - PY1010

Emilie Granviken
2025-11-14
"""

#%% Oppgave 1: Beregning av alder basert på fødselstall

from datetime import datetime

year_now = datetime.now().year  # Nåværende årstall
birthyear = int(input("Hvilket år er du født? "))  # Valgt fødselsår
age = year_now - birthyear  # Alder i år basert på gitt fødselsår
print("En person født i ", birthyear, "vil fylle ", age, "år i løpet av", year_now, ".")


#%% Oppgave 2: Beregning av mengde pizza som skal handles inn til klassefest

import math

antall_elever = int(input("Skriv inn antall elever: " ))
pizza_per_elev = 1/4  # Mengde pizza hver elev spiser på klassefesten.
antall_pizza = math.ceil(antall_elever * pizza_per_elev)  # Totalt antall pizza som trengs til festen.

print("Det må handles inn", antall_pizza, "pizzaer til klassefest.")


#%% Oppgave 3: Omregning fra grader til radianer

import numpy as np

v_grad = float(input("Skriv inn gradetallet: " ))  # Grader for en valgt vinkel.
v_rad = v_grad * np.pi/180  # Grader for vinkelen regnet om til radianer.

print("En vinkel på", v_grad, "grader tilsvarer en vinkel på", round(v_rad, 1), "radianer.")


#%% Oppgave 4: Dictionary for hovedsteder og innbyggertall

#a
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.873],
        "Italia": ["Roma", 2.873]
        }
#b
land = input("Skriv inn land: ")
print(data[land][0], "er hovedstaden i", land, "og det er", data[land][1], "mill. innbyggere i", data[land][0], ".")

#c
nytt_land = input("Legg til et land: ")  # Land som skal legges til i dictionary.
hovedstad_nytt_land = input("Skriv inn landets hovedstad: ")  # Hovedstad for landet som legges til.
innbyggere__hovedstad_nytt_land = input("Skriv inn antall innbyggere (i antall millioner) i hovedstaden: ") # Innbyggertall i hovedstaden.
data[nytt_land] = [hovedstad_nytt_land, innbyggere_hovedstad_nytt_land]  # Integrering i dictionary.
print("Oppdatert dictionary:", data)

#%% Oppgave 5: Beregning av areal og omkrets for figur

import math

def funksjon_figur(a, b):
    """Beregning av areal og omkrets for en figur satt sammen av en trekant og
    en halvsirkel, der trekantens lille katet utgjør diameteren for sirkelen.
    """
    hypotenus = math.sqrt(a**2 + b**2)
    areal = ((np.pi*a**2)/2) + (a*b/2)
    omkrets = ((2*np.pi*a)/2 + b + hypotenus)
    return (areal, omkrets)
    
store_katet = 10  # Lengde på trekantens store katet i cm.
lille_katet = 5  # Lengde på trekantens lille katet/sirkelens diameter i cm.
(areal_figur, omkrets_figur) = funksjon_figur(lille_katet, store_katet)
print("Areal og omkrets for en figur satt sammen av en trekant og en halvsirkel der trekantens store katet er", store_katet, "cm lang og dens lille katet (samt diameter for sirkelen) er", lille_katet, "cm lang er som følger:")
print("Areal =", round(areal_figur, 1), "cm^2")
print("Omkrets =", round(omkrets_figur, 1), "cm^2")


#%% Oppgave 6: Plotting av funksjon

import matplotlib.pyplot as plt

def funksjon(x):
    return -x**2 -5

x_verdier = np.linspace(-10, 10, 200)  # x-verdier for kurven som benyttes til å beregne y-verdiene for kurven.
y_verdier = funksjon(x_verdier)  # Beregning av y-verdier.

plt.plot(x_verdier, y_verdier)
plt.show()


    