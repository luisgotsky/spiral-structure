import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Rotación rígida

t = np.linspace(0, 15, 1500)
w = 10
r = np.linspace(-1, 1, 20)
xR = lambda r: np.array([r*np.cos(w*i) for i in t])
yR = lambda r: np.array([r*np.sin(w*i) for i in t])

figR = plt.figure(figsize=(6, 6))
axR = plt.axes()
axR.set_xlim(-1.1, 1.1)
axR.set_ylim(-1.1, 1.1)

def update(frame):
    
    axR.cla()
    
    for i in r:
        
        axR.scatter(xR(i)[frame], yR(i)[frame])
        
    axR.set_xlim(-1.1, 1.1)
    axR.set_ylim(-1.1, 1.1)
        
aniR = FuncAnimation(figR, update, frames=300, interval=0.1)
aniR.save("Animación rigida.gif")

#Rotación diferencial

v = 10
r = np.linspace(-1, 1, 20)
xD = lambda r: np.array([r*np.cos(abs(v/r)*i) for i in t])
yD = lambda r: np.array([r*np.sin(abs(v/r)*i) for i in t])

figD = plt.figure(figsize=(6, 6))
axD = plt.axes()
axD.set_xlim(-1.1, 1.1)
axD.set_ylim(-1.1, 1.1)

def update(frame):
    
    axD.cla()
    
    for i in r:
        
        axD.scatter(xD(i)[frame], yD(i)[frame])
        
    axD.set_xlim(-1.1, 1.1)
    axD.set_ylim(-1.1, 1.1)
        
aniD = FuncAnimation(figD, update, frames=300, interval=0.1)
aniD.save("Animación diferencial.gif")