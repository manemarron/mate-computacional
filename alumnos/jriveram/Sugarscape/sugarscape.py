from __future__ import division
from random import randint, choice, shuffle
from math import sqrt
import numpy as np


__author__ = 'Javier'


class Mundo(object):
    """

    """

    def __init__(self,
                 reglas=['G', 'M', 'R', 'P', 'D', 'S', 'I', 'K', 'C'],
                 max_coord=(49, 49),
                 init_num_agentes=400,
                 metabol=(1, 4), vision=(1, 6), init_sugar=(5, 25),
                 aumento_sugar=1,
                 max_edad=(60, 100),
                 pol=(1, 1),
                 difusion_pol=1,
                 edad_reproduc_hombre=(12, 40, 50), edad_reproduc_mujer=(15, 50, 60),
                 long_cultura=11,
                 recom_ataque=float('inf')):

        # caracteristicas del mundo
        self.tiempo = 0
        self.max_coord = max_coord
        self.reglas = reglas
        self.aumento_sugar = aumento_sugar
        self.recom_ataque = recom_ataque

        # variables del mundo
        self.parcelas = list()
        self.lista_parcelas = list()
        self.lista_agentes = list()

        # caracteristicas de parcelas pertenecientes a este mundo
        self.pol = pol
        self.difusion_pol = difusion_pol

        # caracteristicas de agentes pertenecientes a este mundo
        self.metabol = metabol
        self.vision = vision
        self.max_edad = max_edad
        self.init_sugar = init_sugar
        self.edad_reproduc = {'H': edad_reproduc_hombre, 'M': edad_reproduc_mujer}
        self.long_cultura = long_cultura

        # crear parcelas
        self.parcelas = [[Parcela(self, (coord_0, coord_1), 0)
                          for coord_1 in range(self.max_coord[1] + 1)]
                         for coord_0 in range(self.max_coord[0] + 1)]
        self.lista_parcelas = [item for sublist in self.parcelas for item in sublist]

        # crear agentes
        for a in range(init_num_agentes):
            self.crea_agente()

        # crear montanas de sugar
        centros = [(15, 15), (34, 34)]
        radios = [(23, 1), (17, 2), (10, 3), (5, 4)]
        for r in radios:
            for c in centros:
                self.parcelas[c[0]][c[1]].crea_montana(r[0], r[1])

        # variables que utilizo para estudiar diferentes fenomenos
        self.reg_num_agentes = [len(self.lista_agentes)]
        # self.reg_prom_vision = [np.mean(map(lambda x: x.vision, self.lista_agentes))]
        # self.reg_prom_metabol = [np.mean(map(lambda x: x.metabol, self.lista_agentes))]
        self.reg_esperanza_vida = list()

    def obten_parcela(self, punto):
        if punto[0] not in range(self.max_coord[0] + 1):
            punto = (punto[0] % (self.max_coord[0] + 1), punto[1])
        if punto[1] not in range(self.max_coord[1] + 1):
            punto = (punto[0], punto[1] % (self.max_coord[1] + 1))
        return self.parcelas[punto[0]][punto[1]]

    def enlista_vacias(self, lista=None):
        if lista is None:
            lista = self.lista_parcelas
        return [p for p in lista if p.esta_vacia()]

    def crea_agente(self, parcela=None, progen=None):
        if parcela is None:
            parcela = choice(self.enlista_vacias())
        agente = Agente(mundo=self, parcela=parcela, progen=progen)
        self.lista_agentes.append(agente)
        return agente

    def difunde_pol(self):
        pol = list()
        for p in self.lista_parcelas:
            vecinos = map(lambda x: x.pol, p.obten_neumann())
            flujo = np.mean(vecinos)
            pol.append(flujo)
        for p in self.lista_parcelas:
            p.pol = pol.pop(0)

    def evoluciona(self):
        # evoluciona mundo
        self.tiempo += 1

        # evoluciona parcelas
        if 'D' in self.reglas:
            if self.tiempo % self.difusion_pol == 0:
                self.difunde_pol()

        for p in self.lista_parcelas:
            if 'G' in self.reglas:
                val = min(p.sugar + self.aumento_sugar, p.cap_sugar)
                p.sugar = val
                p.indice_pref = p.sugar

            if 'C' in self.reglas:
                if p.agente is not None:
                    p.indice_pref += min(p.agente.sugar, self.recom_ataque)

            if 'P' in self.reglas:
                p.indice_pref /= p.pol

        # evoluciona agentes
        shuffle(self.lista_agentes)
        for agente in self.lista_agentes:
            if 'C' in self.reglas:
                agente.atacar()
            elif 'M' in self.reglas:
                agente.mover()
            agente.establecer_vecinos()

            agente.recolectar()
            if agente.sugar < 0:
                agente.morir()
                continue

            if 'S' in self.reglas:
                agente.reproducir()

            if 'K' in self.reglas:
                agente.influenciar()
                agente.buscar_amigos()

            agente.edad += 1
            if agente.edad > agente.max_edad:
                agente.morir()
                continue

        # actualizar registros
        self.reg_num_agentes.append(len(self.lista_agentes))
        # self.reg_prom_vision.append(np.mean(map(lambda x: x.vision, self.lista_agentes)))
        # self.reg_prom_metabol.append(np.mean(map(lambda x: x.metabol, self.lista_agentes)))

    def obten_matriz_parcelas(self, attr='sugar'):
        m = [map(lambda p: getattr(p, attr), linea) for linea in self.parcelas]
        return np.matrix(m)

    def obten_matriz_agentes(self, attr='agente'):
        m = [map(lambda p: 1 if getattr(p, attr) is not None else 0, linea) for linea in self.parcelas]
        return np.matrix(m)

    def obten_matriz_general(self):
        m = [map(lambda p: max(p.sugar, (5 if p.agente is not None else 0)), linea) for linea in self.parcelas]
        return np.matrix(m)


class Parcela(object):
    """

    """

    def __init__(self, mundo, coord, cap_sugar):
        # ubicacion
        self.mundo = mundo
        self.coord = coord

        # caracteristicas que no cambian con el tiempo
        self.cap_sugar = cap_sugar

        # caracteristicas que cambian con el tiempo
        self.sugar = self.cap_sugar
        self.pol = 1
        self.agente = None
        self.indice_pref = self.sugar

    def __add__(self, other):
        if type(other) is tuple and len(other) == 2:
            parcela = (self.coord[0] + other[0], self.coord[1] + other[1])
            return self.mundo.obten_parcela(parcela)

    def __radd__(self, other):
        return self.__add__(other)

    def __cmp__(self, other):
        if self.indice_pref > other.indice_pref:
            return 1
        if self.indice_pref == other.indice_pref:
            return 0
        else:
            return -1

    def distancia(self, otra):
        return sqrt((self.coord[0] - otra.coord[0]) ** 2 + (self.coord[1] - otra.coord[1]) ** 2)

    def regenera_sugar(self):
        self.sugar = self.cap_sugar

    def crea_montana(self, radio, cap_sugar):
        for i in range(-radio, radio + 1):
            for j in range(-radio, radio + 1):
                parcela = self + (i, j)
                if self.distancia(parcela) <= radio:
                    parcela.cap_sugar = cap_sugar
                    parcela.regenera_sugar()

    def esta_vacia(self):
        return self.agente is None

    def obten_neumann(self, dist=1):
        vecinos = [self + (dist_0, dist_1)
                   for dist_0 in [0, dist, -dist]
                   for dist_1 in [0, dist, -dist]
                   if dist_0 != dist_1 and dist_0 != -dist_1]
        return vecinos

    def obten_moore(self, dist=1):
        vecinos = [self + (dist_0, dist_1)
                   for dist_0 in [0, dist, -dist]
                   for dist_1 in [0, dist, -dist]
                   if (dist_0, dist_1) != (0, 0)]
        return vecinos


class Agente(object):
    """

    """

    def __init__(self, mundo, parcela, progen=None):
        # ubicacion
        self.mundo = mundo
        self.parcela = parcela
        self.parcela.agente = self

        # caracteristcas que no cambian con el tiempo
        #   geneticas
        self.progen = progen
        if progen is None:
            self.metabol = randint(self.mundo.metabol[0], self.mundo.metabol[1])
            self.vision = randint(self.mundo.vision[0], self.mundo.vision[1])
            self.max_edad = randint(self.mundo.max_edad[0], self.mundo.max_edad[1])
            self.sugar_inicial = randint(self.mundo.init_sugar[0], self.mundo.init_sugar[1])
        else:
            self.metabol = choice([progen[0].metabol, progen[1].metabol])
            self.vision = choice([progen[0].vision, progen[1].vision])
            self.max_edad = choice([progen[0].max_edad, progen[1].max_edad])
            self.sugar_inicial = progen[0].sugar_inicial / 2 + progen[1].sugar_inicial / 2
        #   no geneticas
        self.genero = choice(['H', 'M'])
        edad_reproduc = self.mundo.edad_reproduc[self.genero]
        self.min_edad_reproduc = edad_reproduc[0]
        self.max_edad_reproduc = randint(edad_reproduc[1], edad_reproduc[2])

        # caracteristicas que cambian con el tiempo
        self.edad = 0
        self.sugar = self.sugar_inicial
        if progen is None:
            self.cultura = map(lambda x: choice((0, 1)), range(self.mundo.long_cultura))
        else:
            self.cultura = map(lambda x: choice((progen[0].cultura[x], progen[1].cultura[x])),
                               range(self.mundo.long_cultura))
            self.grupo = self.obtener_grupo
        self.vecinos = list()
        self.hijos = list()
        self.amigos = list()

    def mover(self):
        self.parcela.agente = None
        mejores = list()
        mejores.append(self.parcela)
        max_mejor = self.parcela.indice_pref
        for i in range(1, self.vision + 1):
            parcelas = [p for p in self.parcela.obten_neumann(i) if p.esta_vacia]
            max_p = max(parcelas).indice_pref
            parcelas = filter(lambda x: x.indice_pref == max_p, parcelas)
            if max_p > max_mejor:
                max_mejor = max_p
                mejores = parcelas

        self.parcela = choice(mejores)
        self.parcela.agente = self

    def atacar(self):
        self.parcela.agente = None
        max_enemigo_sugar = self.sugar
        parcelas = list()
        parcleas_ocupadas = list()
        parcelas.append(self.parcela)

        for i in range(1, self.vision + 1):
            parcelas.append([])
            parcleas_ocupadas.append([])

            for p in self.parcela.obten_neumann(i):
                if p.esta_vacia:
                    parcelas[-1].append(p)
                else:
                    if p.agente.grupo != self.grupo:
                        if p.agente.sugar > max_enemigo_sugar:
                            max_enemigo_sugar = p.agente.sugar
                        if self.sugar > p.agenete.sugar:
                            parcleas_ocupadas[-1].append(p)

        saqueo = lambda x: min(self.mundo.recom_ataque, x.agente.sugar)
        sugar = lambda x: self.sugar + x.sugar + saqueo(x)
        parcelas_ocupadas = map(lambda x: filter(lambda s: sugar(s) >= max_enemigo_sugar, x), parcleas_ocupadas)
        parcelas = (sum(x) for x in zip(parcelas, parcelas_ocupadas))
        max_mejor = max([p for sub in parcelas for p in sub]).indice_pref

        filtro = []
        while not any(filtro):
            linea = next(parcelas)
            filtro = filter(lambda x: x.indice_pref == max_mejor, linea)

        self.parcela = choice(filtro)
        if not self.parcela.esta_vacia():
            self.sugar += saqueo(self.parcela)
            self.parcela.agente.sugar -= saqueo(self.parcela)
            self.parcela.agente.morir()
        self.parcela.agente = self

    def recolectar(self):
        self.sugar += self.parcela.sugar - self.metabol
        if 'P' in self.mundo.reglas:
            metabolice = self.metabol
            if self.sugar < 0:
                metabolice += self.sugar
            self.parcela.pol += self.mundo.pol[0] * self.parcela.sugar + self.mundo.pol[1] * metabolice
        self.parcela.sugar = 0

    def establecer_vecinos(self):
        self.vecinos = [p.agente for p in self.parcela.obten_neumann() if not p.esta_vacia]

    def soy_fertil(self):
        if self.min_edad_reproduc <= self.edad <= self.max_edad_reproduc and self.sugar >= self.sugar_inicial:
            return True
        return False

    def buscar_pareja(self):
        posibles = [m for m in self.vecinos if self.genero != m.genero and m.soy_fertil()]
        neumann = map(lambda x: self.mundo.enlista_vacias(self.parcela.obten_neumann + x.parcela.obten_neumann),
                      posibles)
        par = [p for p in zip(posibles, neumann) if len(p[1]) > 0]
        if len(par) == 0:
            return None
        return choice(par)

    def reproducir(self):
        if not self.soy_fertil():
            return
        mate = self.buscar_pareja()
        if mate is None:
            return

        pareja, parcela = mate[0], choice(mate[1])
        self.sugar -= self.sugar_inicial / 2
        pareja.sugar -= pareja.sugar_inicial / 2

        hijo = self.mundo.crea_agente(parcela=parcela, progen=(self, pareja))
        self.hijos.append(hijo)
        pareja.hijos.append(hijo)

        self.reproducir()

    def obtener_grupo(self):
        if self.cultura.count(0) > self.cultura.count(1):
            return 0
        return 1

    def influenciar(self):
        for vecino in self.vecinos:
            tag = choice(range(self.mundo.long_cultura))
            if self.cultura[tag] != vecino.cultura[tag]:
                vecino.cultura[tag] = self.cultura[tag]
                vecino.grupo = vecino.obtener_grupo()

    def hamming(self, otro):
        iguales = filter(lambda x: x[0] == x[1], zip(self.cultura, otro.cultura))
        return self.mundo.long_cultura - len(iguales)

    def buscar_amigos(self):
        self.amigos += self.vecinos
        self.amigos.sort(key=lambda x: self.hamming(x))
        self.amigos = self.amigos[:5]

    def morir(self):
        self.parcela.agente = None
        self.mundo.lista_agentes.remove(self)
        if 'R' in self.mundo.reglas:
            self.mundo.crea_agente()
        if 'I' in self.mundo.reglas:
            for hijo in self.hijos:
                hijo.sugar += self.sugar / len(self.hijos)

        self.mundo.reg_esperanza_vida.append(self.edad)