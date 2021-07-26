M = input()
L = M.count(":-)")
C = M.count(":-(")

if L > C :
	print("divertido")

elif L == C :
	print("neutro")

elif L < C :
	print("chateado")
