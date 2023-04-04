import matplotlib.pyplot as plt

def small():
    x = [-0.5, 0.5, 0.5, -0.5, -0.5]
    y = [ -0.5, -0.5, 0.5, 0.5, -0.5]
    ply.pot(x, y, "-.ro")
    plt.exis("equal")
    plt.xlim([-1, 1])
    plt.xlim([-1, 1])
    plt.show()

def midium():
    small()
    x = [-1, 1, 1, -1, -1]
    y = [-1, -1, 1, 1, -1]
    plt.plot(x, y, "gs-", markersize=8)
    plt.show()

def large():
    midium()
    x = [-1.5, 1.5, 1.5, -1.5, -1.5]
    y = [-1.5, -1.5, 1.5, 1.5, -1.5]
    plt.plot(x, y, "bp-", markersize=12)
    plt.show()


large()


