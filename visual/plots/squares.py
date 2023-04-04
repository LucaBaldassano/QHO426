import matplotlib.pyplot as plt

def small():
    x = [0, 1, 1, 0, 0]
    y = [0, 0, 1, 1, 0]
    # plot the square as a red dotted line with circle markers
    plt.plot(x, y, "ro:", markersize=10, linewidth=2)
    plt.axis("equal")
    plt.show()

def medium():
    x = [0, 2, 2, 0, 0]
    y = [0, 0, 2, 2, 0]
    plt.plot(x, y, "gs--", markersize=10, linewidth=2)
    plt.axis("equal")
    plt.show()

def large():
    x = [0, 4, 4, 0, 0]
    y = [0, 0, 4, 4, 0]
    plt.plot(x, y, "bp-", markersize=10, linewidth=2)
    plt.axis("equal")
    plt.show()
large()