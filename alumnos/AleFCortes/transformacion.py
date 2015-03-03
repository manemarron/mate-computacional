
def polar(x,y):
    """
    x, y son un par ordenado
    """
    r = sqrt(x**2 + y**2)
    theta = atan(y/x)
    print r, theta