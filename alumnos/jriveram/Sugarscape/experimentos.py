
import sugarscape as sugarscape
import graf_sugarscape as graf

import os as os
import pickle
import matplotlib.pyplot as plt


__author__ = 'Javier'


def llevame(exp):
    fn = os.path.join(os.path.dirname(__file__), exp)
    if not os.path.exists(fn):
        os.makedirs(fn)
    os.chdir(fn)


def guardar(mundo):
    with open('mundo.pkl', 'wb') as output:
        pickle.dump(mundo, output, pickle.HIGHEST_PROTOCOL)


def cargar():
    with open('mundo.pkl', 'rb') as input:
        return pickle.load(input)


def experimento_generico(exp, mundo, tiempo, graficas_mapa=None, inclusiones=None, graficas_reg=[]):
    llevame(exp)

    m_gen = list()
    m_gen.append(mundo.obten_matriz_general())

    for i in range(tiempo):
        mundo.evoluciona()
        # if (graficas_mapa and (i + 1) in graficas_mapa)
        # or (inclusiones and (i + 1) in inclusiones and inclusiones[i + 1] != 0):
        m_gen.append(mundo.obten_matriz_general())
        # else:
        #     m_gen.append(None)
    print('termine: evolucionar mundo')

    graf.anima_mapa(fo='agentes_parcelas', matrices=m_gen, graficas=graficas_mapa, inclusiones=inclusiones)
    print('termine: animar mapa')
    plt.close()

    for i in graficas_reg:
        graf.grafica(x=range(i + 1), y=mundo.reg_num_agentes[:i + 1], xlabel='tiempo', ylabel='numero de agentes')
        plt.savefig('agentes_%d' % i)
        plt.close()
    print('termine: graficar registro')


def experimento_0():
    print('INICIE EXPERIMENTO 0')
    exp = 'EXP_0'
    llevame(exp)
    mundo = sugarscape.Mundo(init_num_agentes=0, reglas='G')

    m_gen = list()
    m_gen.append(mundo.obten_matriz_general())

    graf.anima_mapa(fo='agentes_parcelas', matrices=m_gen, graficas=[0], colorbar=True)
    print('TERMINE EXPERIMENTO 0')


def experimento_1():
    print('INICIE EXPERIMENTO 1')
    exp = 'EXP_1'
    mundo = sugarscape.Mundo(reglas='GM', max_edad=(1000, 1000), aumento_sugar=float('inf'))
    inclusiones = dict()
    for i in range(11):
        inclusiones[i] = 5
    for i in range(51, 501):
        inclusiones[i] = 0
    experimento_generico(exp=exp, mundo=mundo, tiempo=500, graficas_mapa=[0, 10, 100, 500], inclusiones=inclusiones,
                         graficas_reg=[10, 100, 500])
    print('TERMINE EXPERIMENTO 1')


def experimento_2():
    print('INICIE EXPERIMENTO 2')
    exp = 'EXP_2'
    mundo = sugarscape.Mundo(reglas='GM', max_edad=(1000, 1000))
    inclusiones = dict()
    for i in range(11):
        inclusiones[i] = 5
    for i in range(101, 501):
        inclusiones[i] = 0
    experimento_generico(exp=exp, mundo=mundo, tiempo=500, graficas_mapa=[0, 10, 100, 500], inclusiones=inclusiones,
                         graficas_reg=[10, 100, 500])
    print('TERMINE EXPERIMENTO 2')


def experimento_3():
    print('INICIE EXPERIMENTO 3')
    exp = 'EXP_3'
    llevame(exp)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('vision media')
    ax.set_ylabel('capacidad de carga')

    vision_media = [2, 4, 6, 8, 10]
    reg_1, reg_2, reg_3 = list(), list(), list()

    for v in [(1, 3), (2, 6), (4, 8), (6, 10), (8, 12)]:
        mundo_1 = sugarscape.Mundo(reglas='GM', init_num_agentes=500, vision=v, metabol=(1, 1), max_edad=(10000, 10000))
        mundo_2 = sugarscape.Mundo(reglas='GM', init_num_agentes=500, vision=v, metabol=(2, 2), max_edad=(10000, 10000))
        mundo_3 = sugarscape.Mundo(reglas='GM', init_num_agentes=500, vision=v, metabol=(3, 3), max_edad=(10000, 10000))
        for i in range(500):
            mundo_1.evoluciona()
            mundo_2.evoluciona()
            mundo_3.evoluciona()

        reg_1.append(mundo_1.reg_num_agentes[-1])
        reg_2.append(mundo_2.reg_num_agentes[-1])
        reg_3.append(mundo_3.reg_num_agentes[-1])

    plt.plot(vision_media, reg_1, label='<m> = 1', lw=2)
    plt.plot(vision_media, reg_2, label='<m> = 2', lw=2)
    plt.plot(vision_media, reg_3, label='<m> = 3', lw=2)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.savefig('comparaciones', bbox_inches='tight')
    plt.close()
    print('TERMINE EXPERIMENTO 3')


def experimento_4():
    def lorentz_data():
            sugar = map(lambda a: a.sugar, mundo.lista_agentes)
            sugar.sort()
            curva = list()
            curva.append(0)
            [curva.append(curva[-1] + s) for s in sugar]
            return curva

    print('INICIE EXPERIMENTO 4')
    exp = 'EXP_4'
    llevame(exp)
    mundo = sugarscape.Mundo(reglas='GMR', init_num_agentes=250)
    graficas = [0, 25, 50, 100]
    for i in range(101):
        if i in graficas:
            riqueza = map(lambda x: x.sugar, mundo.lista_agentes)
            graf.histograma(riqueza, titulo='Tiempo %d' % i, xlabel='riqueza', ylabel='agentes')
            plt.savefig('hist_%d' % i)
            plt.close()
        if i in graficas:
            gini = graf.lorentz(lorentz_data(), xlabel='% poblacion', ylabel='% riqueza')
            plt.suptitle('Tiempo %d, coef. Gini: %1.3f' % (i, gini))
            plt.savefig('gini_%d' % i)
            plt.close()
        mundo.evoluciona()
    print('TERMINE EXPERIMENTO 4')


def experimento_5():
    print('INICIE EXPERIMENTO 5')
    exp = 'EXP_5_1'
    llevame(exp)

    mundo = sugarscape.Mundo(reglas='GM', max_edad=(1000, 1000))
    graficas_mapa = range(0, 501, 25)

    inclusiones = dict()
    inclusiones[50] = 10


    m_gen = list()
    m_gen.append(mundo.obten_matriz_general())

    for i in range(200):
        if i == 50:
            mundo.reglas = 'GMP'
        if i == 50:
            mundo.reglas = 'GMPD'
        mundo.evoluciona()
        # if (graficas_mapa and (i + 1) in graficas_mapa)
        # or (inclusiones and (i + 1) in inclusiones and inclusiones[i + 1] != 0):
        m_gen.append(mundo.obten_matriz_general())
        # else:
        #     m_gen.append(None)
    print('termine: evolucionar mundo')

    graf.anima_mapa(fo='agentes_parcelas', matrices=m_gen, graficas=graficas_mapa, inclusiones=inclusiones)
    print('termine: animar mapa')
    plt.close()
    print('TERMINE EXPERIMENTO 5')




# experimento_0()
# experimento_1()
# experimento_2()
# experimento_3()
# experimento_4()
experimento_5()