import sys

if len(sys.argv) < 2:
    stdout = sys.stdout
    print('1.- Real Numbers')
    print('2.- TSP')
    choosed = int(input('Please choose an option: '))
    if choosed == 1:
        filename = 'real.txt'
        sys.stdout = open(filename, 'w')
        import lab1.reals
    elif choosed == 2:
        filename = 'tsp.txt'
        sys.stdout = open(filename, 'w')
        import lab1.tsp
    else:
        print('Wrong!')        
    sys.stdout = stdout
    print('Done, check file:', filename)


    



