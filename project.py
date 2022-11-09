import math
import matplotlib.pyplot as plt
# alenaaaaaa
increment = 0.2         # =! ajout au compteur #

def fonction(x):
    y = math.cos(x)
    return y

def derivee_f():
    der = []
    compteur = 0
    while compteur < 10:
        fp = (fonction(compteur+increment) - fonction(compteur))/increment
        der.append(fp)
        compteur += 0.1
    return der
derivee = derivee_f()

def tangente_f(a):
    f = []
    compteur = 0
    while compteur < 10:
        y = fonction(a/10) + derivee[a]*(compteur-a/10)
        f.append(y)
        compteur += 0.1
    return f

# Ou veut on tracer la tangente ? #
position = 6
position = int(position * 10)
tangente = tangente_f(position)

x = []
y = []
compteur = 0
while compteur < 10:               # liste pour la fonction
    x.append(compteur)
    y.append(fonction(compteur))
    compteur += 0.1


plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, y, label='Fonction')
#plt.plot(x, derivee, label='Derivée')
plt.plot(x, tangente, label=f'Tangente en x={position/10}')

plt.annotate('Position = (%.1f ; %.1f)'%(x[position],y[position]), 
             xy = (x[position], y[position]), 
             xytext =(x[position], y[position]-derivee[position]/2), 
             arrowprops=dict(arrowstyle = "->", facecolor='black'))
#plt.annotate('Derivée = %.1f'%(derivee[position]), 
#             xy = (x[position], derivee[position]), 
#             xytext =(x[position], derivee[position]-derivee[position]/2), 
#             arrowprops=dict(arrowstyle = "->", facecolor='black'))

plt.legend()
plt.show()