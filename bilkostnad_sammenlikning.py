# -*- coding: utf-8 -*-
"""
Sammenlikning av årlige kostnader for elbil og bensinbil

Laget av Emilie Granviken
2025.09.25
"""

trafikkforsikringsavgift = 8.38 * 365  # Trafikkforsikringsavgift, kr per år
kjorelengde = 10000  # Kjørelengde per år i km

forsikring_elbil = 5000  # Forsikring elbil, kr per år
stromforbruk = 0.2  # Strømforbruk elbil, kWh/km
strompris = 2.00  # Strømpris, kr/kWh
bomavgift_elbil = 0.1  # Bomavgift elbil, kr/km
elbil_totalkostnad = trafikkforsikringsavgift + forsikring_elbil + stromforbruk*kjorelengde*strompris + bomavgift_elbil*kjorelengde
print("Total årlig kostnad for elbil: ", elbil_totalkostnad, " kr")

forsikring_bensinbil = 7500  # Forsikring bensinbil, kr per år
drivstofforbruk = 1.0  # Drivstofforbruk bensinbil, kr/km
bomavgift_bensinbil = 0.3  # Bomavgift bensinbil, kr/km
bensinbil_totalkostnad = trafikkforsikringsavgift + forsikring_bensinbil + drivstofforbruk*kjorelengde + bomavgift_bensinbil*kjorelengde
print("Total årlig kostnad for bensinbil: ", bensinbil_totalkostnad, " kr")

print("Årlig kostnadsdifferanse: ", elbil_totalkostnad - bensinbil_totalkostnad, " kr")