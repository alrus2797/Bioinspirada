import sys

class Menu:
    def i1_reales(self, params, std = None):
        import lab1.reals
    def i2_tsp(self, params, std = None):
        import lab1.tsp
    def i3_es11(self, params, std = None):
        import lab2.es11
    def i4_esu1(self, params, std = None):
        import lab2.esu1 as mu_lambda
        mu_lambda.run(params, std)
    options = [
        {
            'name':'reales',
            'function': 0,
            'params': {}
        },
        {
            'name':'tsp',
            'function': 1,
            'params': {}
        },
        {
            'name':'(1 + 1)',
            'function': 2,
            'params': {}
        },
        {
            'name':'(mu + 1)',
            'function': 3,
            'params': {'_lambda': 1}
        },
        {
            'name':'(mu + lambda)',
            'function': 3,
            'params': {'_lambda': 6}
        },
        {
            'name':'(mu, lambda)',
            'function': 3,
            'params': {'_lambda': 12}
        },
    ]
    def run(self):
        methods = [ m for m in dir(Menu) if not m.startswith('__') ]
        for function_key, option in enumerate(self.options):
            print(f'{function_key + 1}.- {option["name"]}')
        idx_choosed = int(input('Choose strategy: ')) - 1
        option_choosed = self.options[idx_choosed]


        f = getattr(self,methods[option_choosed['function']])
        params = option_choosed['params']

        console_stdout      = sys.stdout
        sys.stdout  = open(f'output/{option_choosed["name"]}.txt', 'w')
        f(params, console_stdout)

        sys.stdout  = console_stdout
        print(f'\nDone, check file: output/{option_choosed["name"]}.txt')
            