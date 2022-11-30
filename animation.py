import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# ATTENTION: len(vitesses)=len(distances)-1

# ENTREES:
# 1) liste vitesses qui est deja moyennée
# 2) max_value_x
# 3) la fonction

vitesses = [10,15,25] # ou une autre liste

fig, ax = plt.subplots()
entered_function = "-(x**2)"
max_value_x = 20
ax.set_xlim(0,max_value_x)
ax.set_ylim(-max_value_x**2,-1) # !!!!!! voir comment faire pour une fonction rentree

entered_function="-(x**2)"
fig = plt.figure() # important psk sinon pas bien cadre sur la figure
lines = plt.plot([],"o", color='blue', linewidth=2, markersize=10) # rayon de la boule
line = lines[0] # fait apparaitre la figure

distances=[]
for v in range(0,len(vitesses)):
    distances.append(round(max_value_x/len(vitesses)*v))
distances.append(max_value_x) # sinon pas de derniere valeur

def animation(frame):
    x = frame
    y = -(frame**2) # !!!!!! voir comment faire pour une fonction rentree
    line.set_data((x,y))

x = np.linspace(0,max_value_x,100)
y = -(x**2)
plt.plot(x, y, ':k', label=entered_function) # plot the slope. sinon :r pour rouge
plt.title('Position of a chunk of an avalanche on a slope depending on speed')
plt.xlabel('x', color='black')
plt.ylabel('y', color='black')
plt.legend(loc='upper right')
plt.grid() # la grille c mieux 

from_value=[]
to_value=[]
spacing_value=[]

for i in range(1,len(distances)):
    from_value.append(distances[i-1])
    to_value.append(distances[i]+0.01) # 0.2
    spacing_value.append(round(vitesses[i-1]/800,2)) # 800 mieux que 1000(trop lent) et 500(saute trop). Regarder en fonction des vitesses qu'on a 

frame=[]
for p in range(0,len(vitesses)):
    frame.append(np.arange(from_value[p],to_value[p],spacing_value[p]))

final_list=[]
for t in frame:
    for s in t:
        final_list.append(round(s,2))

print(final_list)

anim=FuncAnimation(fig,animation,frames=np.array(final_list),interval=1,repeat=False)
plt.show()
