interval = [0, None]

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
    {
        'name'  :'prediction',
        'type'  : 'program',
        'action': 5,
        'params': {
            'iterations'    : 500,
            'n_poblation'   : 16,
            'predict_seq'	: '0111001010011100101001110010100111001010',
        }
    },
    {
        'name'  :'Find function',
        'type'  : 'algorithm',
        'action': 6,
        'params': {
            'iterations': 150,
        }
    },
    {
        'name'  :'Diferential minimization',
        'type'  : 'estrategy',
        'action': 7,
        'params': {
            'iterations': 200,
        }
    },
]
