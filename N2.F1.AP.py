#https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/acelerador/
D = int(input())

# 3 + 8x + 3=> ace 1 => D = 8x + 6 D%8= 6
# 3 + 8x + 4=> ace 2 => D%8=7
# 3 + 8x + 5=> ace 3 D%8 = 0

if D%8 == 6 :
    print(1)
elif D%8 == 7 :
    print(2)
elif D%8 == 0 :
    print(3)
else :
    print("Erro")