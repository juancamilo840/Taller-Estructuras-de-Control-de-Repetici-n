if __name__ == '__main__':
	contador = float()
	sum = float()
	contador = 97
	sum = 0
	while True:
		contador = contador+2
		sum = sum+contador
		print("-",contador)
		if contador==1003: break
	print("Suma pares:",sum)