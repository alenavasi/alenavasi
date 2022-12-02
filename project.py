import matplotlib.pyplot as plt

# Ourvir et lire le fichier
file = open("Resultats", 'r')
results = file.readlines()
file.close()

compteur = 0
vitesse = []
vitesse_moyenne = []
puissance = []
maximum = []
x = []
y = []
for line in results:
    if line[0].isdigit() == False:
        compteur += 1
    else:
        if compteur == 1:
            vitesse.append(float(line))
        elif compteur == 2:
            vitesse_moyenne.append(float(line))
        elif compteur == 3:
            puissance.append(float(line))
        elif compteur == 4:
            maximum.append(float(line))
        elif compteur == 5:
            step = int(line)
        elif compteur == 6:
            x.append(float(line))
        elif compteur == 7:
            y.append(float(line))
maximum[1] = int(maximum[1])

maximum_p = maximum[0]
x_max = maximum[1]/step

plt.xlabel('Horizontal distance (hm)')
plt.ylabel('Hauteur (m)')
plt.plot(x, y, label='Fonction')
plt.plot(x, vitesse, label='Vitesse')
plt.plot(x, puissance, label='Puissance')
plt.annotate('Puissance maximale = %.1f (kJ)'%maximum_p, 
             xy = (x_max, maximum_p), 
             xytext =(x_max, maximum_p + 10), 
             arrowprops = dict(arrowstyle = "->", facecolor='black'))
plt.legend()
plt.show()