import models.bomba.config as config

def main():

	b = Bomba(12)

	for i in range(12):
		print(b.dibujo)
		b.hacer_intento()

	b.hacer_intento()

	print(b.dibujo)

class Bomba:
	__disegno = config.dibujar()['disegno']
	__c1 = config.dibujar()['c1']
	__c2 = config.dibujar()['c2']
	__mecha = config.dibujar()['mecha']
	__boom = config.dibujar()['boom']

	__longitud = 36

	def __init__(self, intentos):
		self.__maxIntentos = intentos
		self.__intentos = intentos
		self.__decremento = self.__longitud // intentos

	def hacer_intento(self):
		if self.__intentos != 0:
			self.__longitud -= self.__decremento
			self.__intentos -= 1

	def reiniciar(self):
		self.__longitud = 36
		self.__intentos = self.__maxIntentos

	@property
	def intentos_faltantes(self):
		return self.__intentos

	@property
	def dibujo(self):

		salida = self.__disegno
		espacios = ' ' * (self.__longitud - 1)
		mecha = '=' * (self.__longitud - 1)

		mensaje = ''

		if self.__intentos == 0:
			return self.__boom
		elif self.__intentos == 1:
			espacios = ' '
			mecha = '='
			mensaje = '¡¡Todos abajo!!'
		elif self.__intentos == 2:
			mensaje = 'Tengo un mal presentimiento'
		elif self.__intentos == 3:
			mensaje = 'Esto es malo'
		elif self.__intentos == 4:
			mensaje = 'Esto no esta funcionando'

		reemplazos = {
			'C1' : f'{espacios}{self.__c1}',
			'C2' : f'{espacios}{self.__c2}',
			'M' : f'{mecha}{self.__mecha}    {mensaje}'
		}

		for r in reemplazos:
			salida = salida.replace(r, reemplazos[r])

		return salida


if __name__ == '__main__':
	main()



