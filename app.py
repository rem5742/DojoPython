class dojo:
	def __init__(self, x, y, s):
		self.menor = x
		self.mayor = y
		self.salto = s
		self.rango = range(menor, mayor, salto)
	def sumar(self):
		suma = 0
		for i in self.rango:
			suma += i # sumar
		return suma

print("Ingrese Menor")
menor = int(input())
print("Ingrese Mayor")
mayor = int(input())
print("Ingrese salto")
salto = int(input())

calcular = dojo(menor, mayor, salto)

print("La suma es: ", calcular.sumar())