#https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/camisetas/

N = int(input())
tam = [int(i) for i in input().split()]
medi = int(input())
peqi = int(input())

med = tam.count(1)
peq = tam.count(2)

if medi == med and peqi == peq:
    print("S")
elif medi != med or peqi != peq:
    print("N")
else:
    print("erro")