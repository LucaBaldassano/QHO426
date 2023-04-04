import matplotlib.pyplot as plt

def small():
    x = [0, 1, 1, 0, 0]
    y = [0, 0, 1, 1, 0]
    plt.plot(x, y, "-.ro")


def medium():
    x = [0, 2, 2, 0, 0]
    y = [0, 0, 2, 2, 0]
    plt.plot(x, y, "--gs")

def large():
    x = [0, 4, 4, 0, 0]
    y = [0, 0, 4, 4, 0]
    plt.plot(x, y, "-bp")
small()
medium()
large()

plt.axis("Scaled")
plt.show()