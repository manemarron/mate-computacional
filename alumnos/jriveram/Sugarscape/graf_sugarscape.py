from __future__ import division
import numpy as np
from scipy.integrate import trapz
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation as animation


__author__ = 'Javier'


def grafica(x, y, xlabel='', ylabel=''):
    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel(ylabel=ylabel)
    plt.plot(x, y, lw=2)
    plt.ylim(ymin=0)


def histograma(x, bars=10, titulo='', xlabel='', ylabel=''):
    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel(ylabel=ylabel)
    plt.suptitle(titulo)
    d = dict()
    for c in x:
        if c not in d:
            d[c] = 0
        d[c] += 1
    keys = d.keys()
    frequencies = d.values()
    n, bins, patches = plt.hist(keys, bars, weights=frequencies, color='#1c9099')


def lorentz(curva, xlabel='', ylabel=''):
    x = range(len(curva))
    for i in range(len(x)):
        x[i] /= x[-1]
        x[i] *= 100
    for i in range(len(curva)):
        curva[i] /= curva[-1]
        curva[i] *= 100

    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel(ylabel=ylabel)
    ax.set_aspect('equal')
    plt.plot([0, 100], [0, 100], color='black')
    plt.plot(x, curva, color='black')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    ax.fill_between(x, 0, curva, facecolor='#df65b0')
    triangulo = trapz(y=[0, 100], x=[0, 100])
    gini = (triangulo - trapz(y=curva, x=x)) / triangulo
    return gini


def guarda_animacion(fo, animacion):
    writer = animation.writers['ffmpeg']
    metadata = dict(title=fo, artist='Javier')
    my_writer = writer(fps=10, bitrate=1800, metadata=metadata)
    animacion.save('%s.mp4' % fo, writer=my_writer)


def anima_mapa(fo, matrices, graficas=[], coord_max=(50, 50), inclusiones=None, colorbar=False):
    ims = list()
    fig = plt.figure()
    plt.axes().set_aspect('equal')
    plt.xlim(0, coord_max[0])
    plt.ylim(0, coord_max[1])

    if not inclusiones:
        inclusiones = dict()
    pendientes = list()

    cmap = mpl.colors.ListedColormap(['#f2f0f7', '#cbc9e2', '#9e9ac8', '#756bb1', '#54278f', '#f03b20'])

    if colorbar:
        cmap = mpl.colors.ListedColormap(['#f2f0f7', '#cbc9e2', '#9e9ac8', '#756bb1', '#54278f'])

    for i in range(len(matrices)):
        if i in inclusiones and inclusiones[i] == 0:
            if i in graficas:
                pendientes.append(i)
            continue

        matriz = np.array(matrices[i])
        quad = plt.pcolormesh(matriz, cmap=cmap)

        if i == 0 and colorbar:
            bounds = [0, 1, 2, 3, 4, 5]
            ax = fig.add_axes([0.85, 0.1, 0.03, 0.8])
            cb = mpl.colorbar.ColorbarBase(ax, cmap=cmap, spacing='proportional', boundaries=bounds)
            cb.ax.get_yaxis().set_ticks([])
            for j, lab in enumerate(['$0$','$1$','$2$','$3$', '$4$']):
                cb.ax.text(.5, (2 * j + 1) / 10, lab, ha='center', va='center')
            cb.ax.get_yaxis().labelpad = 15
            cb.ax.set_ylabel('Capacidad de sugar', rotation=270)

        if i not in inclusiones:
            inclusiones[i] = 1
        for j in range(inclusiones[i]):
            ims.append([quad])
        if i in graficas:
            fig.suptitle('Tiempo %d' % i)
            nombre = '%s_%d.png' % (fo, i)
            plt.savefig(nombre, bbox_inches='tight')
            fig.suptitle('')

    if len(ims) > 0:
        im_ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)
        guarda_animacion(fo, im_ani)

    for i in pendientes:
        matriz = np.array(matrices[i])
        quad = plt.pcolormesh(matriz, cmap=cmap)
        fig.suptitle('Tiempo %d' % i)
        nombre = '%s_%d.png' % (fo, i)
        plt.savefig(nombre, bbox_inches='tight')
        fig.suptitle('')



