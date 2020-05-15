import sys
from termcolor import colored

class Menu:
    def i1_reales(self, params, std = None):
        import genetic_algs.reals
    def i2_tsp(self, params, std = None):
        import genetic_algs.tsp
    def i3_es11(self, params, std = None):
        import evolution_estrats.es11 as mu_1
        mu_1.run(params, std)

    def i4_esu1(self, params, std = None):
        import evolution_estrats.esu1 as mu_lambda
        mu_lambda.run(params, std)
    options = [
        {
            'name':'reales',
            'action': 0,
            'params': {}
        },
        {
            'name':'tsp',
            'action': 1,
            'params': {}
        },
        {
            'name':'(1 + 1)',
            'action': 2,
            'params': {}
        },
        {
            'name':'(mu + 1)',
            'action': 3,
            'params': {'_lambda': 1}
        },
        {
            'name':'(mu + lambda)',
            'action': 3,
            'params': {
                'iterations': 250,
                '_lambda': 6
            }
        },
        {
            'name':'(mu, lambda)',
            'action': 3,
            'params': {
                'iterations': 100,
                '_lambda': 12
            }
        },
    ]
    def run(self):
        methods = [ m for m in dir(Menu) if not m.startswith('__') ]
        for function_key, option in enumerate(self.options):
            print(f'{function_key + 1}.- {option["name"]}')
        idx_choosed = int(input('Choose strategy: ')) - 1
        option_choosed = self.options[idx_choosed]


        f = getattr(self,methods[option_choosed['action']])
        params = option_choosed['params']
        print(f'Executing: {option_choosed["name"]} strategy')
        console_stdout      = sys.stdout
        sys.stdout  = open(f'output/{option_choosed["name"]}.txt', 'w')
        f(params, console_stdout)

        sys.stdout  = console_stdout
        print(colored('\n','blue'))
        print(colored(f'Done, check file: output/{option_choosed["name"]}.txt','green'))
            