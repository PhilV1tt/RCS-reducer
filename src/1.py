'''Première simulation d'une onde EM en 1D'''

import math
import matplotlib.pyplot as plt

SIZE = 200
qTime = 0
maxTime = 1000
imp0 = 377.0

ez = [0.0]*SIZE
hy = [0.0]*SIZE
historique = []

for qTime in range(maxTime):
    for mm in range (SIZE-1):
        hy[mm] = hy[mm] + (ez[mm + 1] - ez[mm]) / imp0
    for mm in range (1,SIZE):
        ez[mm] = ez[mm]+(hy[mm]-hy[mm-1])*imp0
    ez[0] = math.exp(-(qTime - 30.0) * (qTime - 30.0) / 100.0)
    
    if qTime % 10 == 0:  # Tous les 10 pas de temps
        historique.append(ez[:])  # Copie du tableau

plt.figure(figsize=(10, 6))
plt.plot(ez)
plt.xlabel('Position')
plt.ylabel('Champ électrique Ez')
plt.title('Onde EM après 250 itérations')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
for i, snapshot in enumerate(historique):
    plt.clf()
    plt.plot(snapshot)
    plt.ylim(-1, 1)
    plt.xlabel('Position')
    plt.ylabel('Ez')
    plt.title(f'Temps = {i*10}')
    plt.grid(True)
    plt.pause(0.1)
plt.show()


