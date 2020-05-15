import scipy.stats as ss
import numpy as np

def is_between(value, _min, _max):
    return _min <= value <= _max

def get_percentil(x, sigma):
    return ss.norm(0,sigma).ppf(x)

def get_element_candidate(x, sigma, _range, verbose):
    candidate = float('-inf')
    while not is_between(candidate, *_range):
        rand_number = np.random.rand()
        percentil   = get_percentil(rand_number, sigma)
        candidate   =  x + percentil
        # print(candidate, percentil, rand_number, is_between(candidate, *_range), verbose)
    if verbose:
        print(f'Gen {verbose}:')
        print(f"\tRandom Number: {rand_number} - Percentile: {percentil}")
    return candidate

def get_candidate(subject, sigmas, _range, verbose = False):
    return [get_element_candidate(x, sigma, _range, idx + 1 if verbose else False) for idx, (x, sigma) in enumerate(zip(subject, sigmas))]

def sigma_uniform_cross(s1, s2):
    return list(map(lambda x, y: (x*y)**(1/2), s1, s2))

def get_delta_sigma(n):
    return 1/np.sqrt(2 * np.sqrt(n))

def sigma_mutation(s1, delta_sigma):
    rand_number = np.random.rand(len(s1))
    percentils  = get_percentil(rand_number, delta_sigma)
    change_rate = np.exp(percentils)
    print('Sigma mutacion: ')
    print(f'\t Numeros aleatorios para sigma: {rand_number}')
    print(f'\t Percentiles: {percentils} -> exp: {change_rate}')
    return s1 * change_rate

def subject_mutation(subject, sigmas, _range, verbose = False):
    print('Hijo Mutacion')
    return get_candidate(subject, sigmas, _range, verbose)
    
