"""
Entradas
Salidas
"""
if __name__ == '__main__':
	n = int()
	a = int()
	b = int()
	print("Ingrese cantidad n")
	n = int(input())
	a = 6
	b = 11
	for i in range(1,n+1):
		print(a)
		c = a+b
		a = b
		b = c