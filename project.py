import math
import matplotlib.pyplot as plt
# alenaaaaaa
increment = 0.2         # =! ajout au compteur #
yo = 0

def fonction(x):
    y = math.cos(x) + yo
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
position = 5
position = int(position * 10)
tangente = tangente_f(position)

x = []
y = []
compteur = 0
while compteur < 10:               # liste pour la fonction
    x.append(compteur)
    y.append(fonction(compteur))
    compteur += 0.1


# Somme des forces = P + Ff = ma #

def theta_f(der):
    t = []
    for i in range(0, len(der)):
        angle = math.atan(der[i])
        t.append(angle)
    return t



def time_f():
    t = []
    compteur = 0
    while compteur<10:
        t.append(compteur)
        compteur += 0.1 
    return t


def vitesse_f1(m, k, t, a):
    v = []
    for i in range(0,len(a)):
        vi = (math.sin(a[i])*g*m)/k + math.exp(-(k/m)*t[i]) 
        v.append(vi)
    return v

def vitesse_f2(px, py):
    v = []
    for i in range(0,len(px)):
        vi = math.sqrt(px[i]**2 + py[i]**2)/0.1
        v.append(vi)
    return v


def position_sans_normale(m, k, t, a):
    p = []
    for i in range(0, len(a)):
        r = -(m/k)*math.exp(-(k/m)*t[i]) + (math.sin(a[i])*g*m*t[i])/k 
        p.append(r)
    return p


def position_vraie_x(pos,a):
    x = []
    for i in range(0,len(pos)):
        x.append(-math.cos(a[i])*pos[i])
    return x


def position_vraie_y(pos,a):
    y = []
    for i in range(0,len(pos)):
        y.append(-math.sin(a[i])*pos[i] + yo)
    return y


#calcul
coef_frot = 10
masse = 1
g = 9.81
theta = theta_f(derivee)        #angle en radiant#
time = time_f()
#vitesse = vitesse_f1(masse, coef_frot, time, theta)
position_fausse = position_sans_normale(masse, coef_frot, time, theta)
x_traj = position_vraie_x(position_fausse, theta)
y_traj = position_vraie_y(position_fausse, theta)
vitesse = vitesse_f2(x_traj, y_traj)
print(vitesse)


plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, y, label='Fonction')
#plt.plot(x, derivee, label='Derivée')
#plt.plot(x, tangente, label=f'Tangente en x={position/10}')
plt.plot(x, vitesse, label='Vitesse')
plt.plot(x_traj, y_traj, label='Trajectoire')

#plt.annotate('Position = (%.1f ; %.1f)'%(x[position],y[position]), 
#             xy = (x[position], y[position]), 
#             xytext =(x[position], y[position]-derivee[position]/2), 
#             arrowprops=dict(arrowstyle = "->", facecolor='black'))
#plt.annotate('Derivée = %.1f'%(derivee[position]), 
#             xy = (x[position], derivee[position]), 
#             xytext =(x[position], derivee[position]-derivee[position]/2), 
#             arrowprops=dict(arrowstyle = "->", facecolor='black'))

plt.legend()
plt.show()