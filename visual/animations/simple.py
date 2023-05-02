import matplotlib.pyplot as plt
import matplotlib.animation as a
import random
fig, ax = plt.subplots(1,1)

def animate(f):
    ax.cla()
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    colors = ["r", "b", "y", "g"]
    color = colors[random.randint(0, 3)]
    x = random.randint(0,10)
    y = random.randint(0,10)
    ax.plot(f, f, "o"+color)

def run():
    karen = a.FuncAnimation(fig, animate, frames=10, interval=1500)
    plt.show()
run()