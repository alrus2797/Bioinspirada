import numpy.random as npr
def shuffle(array):
    return npr.permutation(array)

def choice(array, num = None):
    return npr.choice(array, num)

def randint(_min, _max = None):
    if _max:
        return npr.randint(_min, _max)
    return npr.randint(_min)

def show_subjects(subjects, desc=''):
    print(desc)
    for idx, subject in enumerate(subjects):
        print(idx,'\t',subject.full_representation())
    print()