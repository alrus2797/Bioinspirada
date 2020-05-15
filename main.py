import sys

print('Please run with Python: ^3.6.5')



options = [
    '(1 + 1)',
    '(mu + 1)',
    '(mu + lambda)',
    '(mu, lambda)',
    ]

if len(sys.argv) < 2:
    stdout = sys.stdout
    for idx, option in enumerate(options):
        print(f'{idx+1}.- {option}')
    choosed = int(input('Please choose an option: '))

    filename = f'output/{options[choosed - 1]}.txt'
    if choosed == 1:
        sys.stdout = open(filename, 'w')
        import lab2.es11
    else:
        if choosed == 2:
            sys.stdout = open(filename, 'w')
            import lab2.esu1 as es
            es.run({'_lambda' : 1})
        if choosed == 3:
            sys.stdout = open(filename, 'w')
            import lab2.esu1 as es
            es.run({'_lambda' : 6})
        if choosed == 4:
            sys.stdout = open(filename, 'w')
            import lab2.esu1 as es
            es.run({'_lambda' : 12})
        else:
            print('Wrong!')        
    sys.stdout = stdout
    print('\nDone, check file:', filename)


    



