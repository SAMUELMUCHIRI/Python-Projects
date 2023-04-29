import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
data1, data2, data3, data4 = np.random.randn(4, 100)  

def plot1():
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.scatter(data1, data2, s=50, facecolor='green', edgecolor='k')
    plt.show()
def plot2():
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.plot(data1, 'o', label='data1')
    ax.plot(data2, 'd', label='data2')
    ax.plot(data3, 'v', label='data3')
    ax.plot(data4, 's', label='data4')
    ax.legend()
    plt.show()
def plot3():
    xpoint=np.array([3,5,7,2,9])
    ypoints=np.array([3**2,5**2,7**2,2**2,9**2])
    ypoints2=np.array([3**3,5**3,7**3,2**3,9**3])
    ypoints3=np.array([3**4,5**4,7**4,2**4,9**4])
    
    plt.plot(ypoints,marker='o',ms =1,mec ='#4CAF50',mfc='#4CAF50')
    plt.plot(ypoints2,marker='x',ms =1,mec ='green',mfc='green')
    plt.plot(ypoints3,marker='o',ms =1,mec ='yellow',mfc='yellow')
    
    plt.show()
fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

v02 = 5
z2 = g * t**2 / 2 + v02 * t

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()


def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = z[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()