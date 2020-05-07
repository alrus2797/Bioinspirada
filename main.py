import sys

print('Please run with Python: ^3.6.5')
if len(sys.argv) < 2:
    stdout = sys.stdout
    print('1.- Real Numbers')
    print('2.- TSP')
    choosed = int(input('Please choose an option: '))
    if choosed == 1:
        filename = 'output/real.txt'
        sys.stdout = open(filename, 'w')
        import lab1.reals
    elif choosed == 2:
        filename = 'output/tsp.txt'
        sys.stdout = open(filename, 'w')
        import lab1.tsp
    else:
        print('Wrong!')        
    sys.stdout = stdout

    print('\nDone, check file:', filename)


    



