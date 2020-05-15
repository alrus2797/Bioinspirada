import sys
from termcolor import colored

from settings import options, interval

class Menu:
    def __init__(self):
        self.interval   = slice(*interval) if interval else slice(0, None)
        self.options    = options
    def a_function(self):
        pass
    def i1_reales(self, params, std = None):
        import genetic_algs.reals
    def i2_tsp(self, params, std = None):
        import genetic_algs.tsp
    def i3_es11(self, params, std = None):
        import evolution_strats.es1_1 as mu_1
        mu_1.run(params, std)
    def i4_esu1(self, params, std = None):
        import evolution_strats.esmu_lambda as mu_lambda
        mu_lambda.run(params, std)

    def run(self):
        methods = [ m for m in dir(Menu) if not m.startswith('__') ]
        options_interval = self.options[self.interval]
        for function_key, option in enumerate(options_interval):
            print(f'{function_key + 1}.- {option["name"]}')
        idx_choosed = int(input('Choose strategy: ')) - 1 + self.interval.start
        if idx_choosed not in range(self.interval.start, self.interval.start + len(options_interval)):
            print('Wrong option!')
            return
        option_choosed = self.options[idx_choosed]

        f = getattr(self,methods[option_choosed['action']])

        params = option_choosed['params']
        print(f'Executing: {option_choosed["name"]} {option_choosed["type"]}')
        console_stdout      = sys.stdout
        sys.stdout  = open(f'output/{option_choosed["name"]}.txt', 'w')
        f(params, console_stdout)

        sys.stdout  = console_stdout
        print(colored('\n','blue'))
        print(colored(f'Done, check file: output/{option_choosed["name"]}.txt','green'))
            