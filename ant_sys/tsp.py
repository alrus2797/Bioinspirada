import math
import numpy as np
from tabulate import tabulate
import sys
from bisect import bisect_left
from itertools import accumulate
from random import random, shuffle

sep = '-----------------------------'
default_headers = ['route', 'fitness']

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
     11, 12, 13]

routes = [
    [0,	12, 3,  23, 1,  5,  23, 56, 12, 11],
    [12, 0, 9,  18, 3,	41,	45,	5,	41, 27],
    [3,	 9, 0,  89, 56,  21,  12, 48, 14, 29],
    [23, 18, 89,   0, 87,  46,  75, 17, 50, 42],
    [1, 3, 56,  87, 0,  55,  22, 86, 14, 33],
    [5, 41, 21,  46, 55,  0,  21, 76, 54, 81],
    [23, 45, 12,  75, 22,  21,  0, 11, 57, 48],
    [56, 5, 48,  17, 86,  76,  11, 0, 63, 24],
    [12, 41, 14,  50, 14,  54,  57, 63, 0, 9],
    [11, 27, 29,  42, 33,  81,  48, 24, 9, 0],
]


places = set(range(len(routes)))
places_names = [chr(65 + i) for i in places]


def get_route_cost(routes, route):
    res = 0
    last_place = route[0]
    for current_place in route[1:]:
        res += routes[last_place][current_place]
        # current_pheromone = pheromones[last_place][current_place]
        # print(f'{places_names[last_place]} - {places_names[current_place]}: Feromona = {current_pheromone:4.f}')
        # pheromones[last_place][current_place] = current_pheromone * fero_regu + res
        last_place = current_place
    return res


def update_pheromones(pheromones, ant_routes, fitnesses, rho=0.9):
    pair_routes = []
    for ant_route in ant_routes:
        pairs = []
        last_place = ant_route[0]
        for current_place in ant_route[1:]:
            pairs.append((last_place, current_place))
            last_place = current_place
        pair_routes.append(pairs)
    for i in range(len(pheromones)):
        for j in range(len(pheromones)):
            print(
                f'{places_names[i]} - {places_names[j]}: Feromona = {pheromones[i][j]}', end=' + ')
            pheromones[i][j] *= rho
            for idx, ant_route in enumerate(pair_routes):
                if (i, j) in ant_route:
                    print(f'{fitnesses[idx]}', end=' + ')
                    pheromones[i][j] += 1/fitnesses[idx]
                else:
                    print('0.0', end=' + ')
            print(f' = {pheromones[i][j]}')


class WeightedRandom:
    def __init__(self, items, weights):
        self.items = list(items)
        self.weights = list(weights)
        self.cum_wt = list(accumulate(weights))
        self.total_wt = self.cum_wt[-1]

    def random(self):
        value = random() * self.total_wt
        index = bisect_left(self.cum_wt, value)
        print("Numero Aleatorio: ", value)
        return self.items[index]

    def set_weights(self, weights):
        self.weights = weights
        self.cum_wt = list(accumulate(self.weights))
        self.total_wt = self.cum_wt[-1]

    def sample(self, n):
        items = set()
        while len(items) < n:
            items.add(self.random())
        items = list(items)
        shuffle(items)
        return items


default_params = {
    'iterations'	: 300,
    'n_poblation'	: 10,
    'fero_regu'		: 1,
    'visi_regu'		: 1,
    'n_places': len(routes)
}


def print_tab(poblation, title='', headers=default_headers, show_index='always'):
    align = ["center"] * (len(headers) + (1 if show_index else 0))
    print(f'{title}')
    print(tabulate(poblation, headers=headers, tablefmt='orgtbl',
                   showindex=show_index, colalign=align), '\n')


def print_route(route, title='Ruta', end=None):
    print(title, end=' ')
    for place in route:
        print(chr(65 + place), end='-')
    if end:
        print(end)
    print('\n')


print_tab(default_params.items(), title='Parametros',
          headers=['Name', 'Value'], show_index=None)
params = type('new_dict', (object,), default_params)

ants = []
for i in range(params.n_poblation):
    p = list(places)
    np.random.shuffle(p)
    ants.append(p)

initial_picked = np.random.randint(0, params.n_places)
initials = np.full(params.n_poblation, initial_picked)
ant_memory = [set([initial_picked]) for idx, ant in enumerate(ants)]
current = np.full(params.n_poblation, initial_picked)

routes = np.array(routes)
print_tab(routes, 'Matriz distancia', places_names, places_names)

visibility = 1 / routes
print_tab(visibility, 'Matriz visibilidad', places_names, places_names)

feromones = np.full((params.n_places, params.n_places), 0.1)

roulette = WeightedRandom(places, [0])

for iteration in range(params.iterations):
    print(f'{sep} Iteracion {iteration + 1} {sep}')
    print_tab(visibility, 'Matriz visibilidad', places_names, places_names)
    print_tab(feromones, 'Matriz feromonas', places_names, places_names)
    ant_routes = []
    fitnesses = []
    for idx, ant in enumerate(ants):
        print(f'Hormiga {idx + 1}')
        route = [current[idx]]
        for i in range(params.n_places - 1):
            posibly_paths = np.zeros(params.n_places)
            places_unwatched = places - ant_memory[idx]
            current_place = current[idx]
            for place_unwatched in places_unwatched:
                t_times_n = feromones[current_place][place_unwatched] * \
                    visibility[current_place][place_unwatched]
                posibly_paths[place_unwatched] = t_times_n
                print(f'{places_names[current_place]} - {places_names[place_unwatched]}: t = {feromones[current_place][place_unwatched]} n = {visibility[current_place][place_unwatched]} t*n = {t_times_n}')
            prob_sum = np.sum(posibly_paths)
            weights = posibly_paths / prob_sum
            print('Suma: ', prob_sum)
            for idx_w in places_unwatched:
                if places_names[current_place] != places_names[idx_w]:
                    weight = weights[idx_w]
                    print(
                        f'{places_names[current_place]} - {places_names[idx_w]} prob: {weight}')
            roulette.set_weights(weights)
            choosed = roulette.random()

            print("Siguiente ciudad: ", places_names[choosed])
            current[idx] = choosed
            ant_memory[idx].add(choosed)
            route.append(current[idx])
            print()
        ant_routes.append(route)
        fitness = get_route_cost(routes, route)
        fitnesses.append(fitness)
        print_route(route, title=f'Hormiga {idx}')

    print('----------------------------------------')
    for idx, route in enumerate(ant_routes):
        print_route(route, f'Hormiga {idx}', f'  fitness: {fitnesses[idx]}')

    update_pheromones(feromones, ant_routes, fitnesses)
    initial_picked = np.random.randint(0, params.n_places)
    initials = np.full(params.n_poblation, initial_picked)
    ant_memory = [set([initial_picked]) for idx, ant in enumerate(ants)]
    current = np.full(params.n_poblation, initial_picked)
