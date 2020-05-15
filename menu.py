import sys

class Menu:
    def i1_reales(self, params):
        import lab1.reals
    def i2_tsp(self, params):
        import lab1.tsp
    def i3_es11(self, params):
        import lab2.es11
    def i4_esu1(self, params):
        import lab2.esu1 as mu_lambda
        mu_lambda.run(params)
        

    options = {
        0: {
            'name':'reales',
            'params': {}
        },
        1: {
            'name':'tsp',
            'params': {}
        },
        2: {
            'name':'(1 + 1)',
            'params': {}
        },
        3: {
            'name':'(mu + 1)',
            'params': {'_lambda': 1}
        },
        3: {
            'name':'(mu + lambda)',
            'params': {'_lambda': 6}
        },
        3: {
            'name':'(mu, lambda)',
            'params': {'_lambda': 12}
        },
    }

    def run(self):
        methods = [ m for m in dir(Menu) if not m.startswith('__') ]
        for function_key, option in self.options.items():
            print(f'{function_key + 1}.- {option["params"]}')
        idx_choosed = int(input('Ingrese una opcion: ')) - 1
        f = methods[idx_choosed]
    
        option_choosed = self.options[idx_choosed]
        
        params = option_choosed['params']

        stdout      = sys.stdout
        sys.stdout  = open(f'output/{option_choosed["name"]}.txt', 'w')
        f(params)
        sys.stdout  = stdout
        print(f'\nDone, check file: output/{option_choosed["name"]}.txt')
        
            