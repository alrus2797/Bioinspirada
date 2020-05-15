interval = [2, None]

options = [
    {
        'name'  :'reals',
        'type'  : 'algorithm',
        'action': 1,
        'params': {}
    },
    {
        'name'  :'tsp',
        'type'  : 'algorithm',
        'action': 2,
        'params': {}
    },
    {
        'name'  :'(1 + 1)',
        'type'  : 'strategy',
        'action': 3,
        'params': {}
    },
    {
        'name'  :'(mu + 1)',
        'type'  : 'strategy',
        'action': 4,
        'params': {'_lambda': 1}
    },
    {
        'name'  :'(mu + lambda)',
        'type'  : 'strategy',
        'action': 4,
        'params': {
            'iterations': 250,
            '_lambda': 6
        }
    },
    {
        'name'  :'(mu, lambda)',
        'type'  : 'strategy',
        'action': 4,
        'params': {
            'iterations': 100,
            '_lambda': 12
        }
    },
]
