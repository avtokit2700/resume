a = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5] #return 5


def find_it(seq):
    for s in seq:
        if seq.count(s) % 2 != 0:
            return s

print(find_it(a))