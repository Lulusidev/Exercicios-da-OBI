#https://olimpiada.ic.unicamp.br/pratique/p2/2020/f2/fotografia/
A ,L = [int(i) for i in input().split()]
N = int(input())
#a = Altura foto L = largura foto 
#m = n molduras
#X = [int(i) for i in input().split()] #altyura da modlura i 
mold_b = -1
a1 = A*L
a_m = 200*200
for i in range(N):
    mold = [int(i) for i in input().split()]
    if (A <= mold[0] and L <= mold[1]) or (L <= mold[0] and A <= mold[1]):
        if mold[0]*mold[1]-a1 < a_m :
            mold_b = 1+i
            a_m = mold[0]*mold[1] - a1
print(mold_b)