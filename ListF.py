# ListF - Short for List Functions
import random

# returns a list of random unique integers 
def randomIntList(length) -> list:
    a = [ i for i in range(length) ]
    random.shuffle(a)
    return a

def listIsSorted(a) -> bool:
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            return False
    return True
