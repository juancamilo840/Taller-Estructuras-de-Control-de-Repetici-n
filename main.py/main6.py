"""
Entradas
Salidas
"""

if __name__ == '__main__':
	dividiendo = float()
	divisor = float()
	cont = float()
	rest = float()
	print("Ingrese el (dividiendo)")
	dividendo = input()
	print("Ingrese el (divisor)")
	divisor = float(input())
	cont = 0
	rest = dividiendo
	while rest-divisor>=0:
		rest = rest-divisor
		print((rest+divisor),"-",divisor,"=",rest)
	print("La division entre: ",dividiendo,"/",divisor,"=",rest)