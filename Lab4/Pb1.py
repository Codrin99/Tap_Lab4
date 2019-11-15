f = open("date.txt", "r")
n = int(f.readline())
print(n)
Vect = []
Vect = f.readline().split()
for i in range (n):
    Vect[i] = int(Vect[i])
print(Vect)
def DEI( prim, ult):
    mij =int((prim + ult) / 2)
    if (mij == Vect[mij]):
        print(mij)
        exit(0)
    if(prim < ult):
        if(mij < Vect[mij]):
            DEI(prim, mij)
        else:
            DEI(mij, ult)
DEI(0,n)