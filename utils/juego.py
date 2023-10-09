import pandas as pd
import re
from time import sleep

class Ahorcado:

	__base = pd.read_csv('base/data.csv')
	__dificultad = {
		1 :{
			'intentos' : 36,
			'min_long_palabra' : 4
		},
		2 :{
			'intentos' : 12,
			'min_long_palabra' : 4
		},
		3 :{
			'intentos' : 6,
			'min_long_palabra' : 6
		},
		4 :{
			'intentos' : 4,
			'min_long_palabra' : 6
		}
	}

	def __init__(self, modelo):
		self.__modelo = modelo
		self.__nivel_dificultad = 0
		self.__letras = dict()
		self.__palabra = ''
		self.__palabraTablero = ''
		self.__status = False
		self.__tablero = ''

	def ejecutar(self):

		print()
		print('**************************************************')
		print('*         Bienvenidos al juego del ahorcado      *')
		print('**************************************************\n')

		sleep(1)

		eleccion = Ahorcado.__menu(['Fácil', 'Normal', 'Difícil', 'Infierno'])
		if eleccion == '*':
			print('Adios!!!')
			return
		self.__nivel_dificultad = int(eleccion)

		print('\n\n¡¡¡Vamos a jugar!!!\n\n')

		sleep(2)

		self.buscar_palabra()
		modelo = self.__modelo(self.__dificultad[self.__nivel_dificultad]['intentos'])

		self.__crear_tablero()

		while (not self.__status) and modelo.intentos_faltantes != 0:
			#print(f'La palabra es {self.__palabra.palabra_para_jugar.values[0]}')
			print(modelo.dibujo)

			print('Encuentra la palabra:')
			print(self.__tablero)

			eleccion = input('>>> ').strip()

			if not self.revisar_letra(eleccion):
				modelo.hacer_intento()

				if modelo.intentos_faltantes > 0:
					print('\n    Has fallado. ¡Inténtalo de nuevo!\n')

			self.__crear_tablero()

		if modelo.intentos_faltantes == 0:
			print(modelo.dibujo)
			print('    Has perdido el juego')
		else:
			print('\n    ¡¡¡Has ganado la partida!!!\n')

		sleep(3)

		print(f'\nLa palabra secreta es {self.__palabra}\n')

	@staticmethod
	def __menu(opciones):
		eleccion = '0'
		print('Selecciona un nivel de dificultad:')
		identificador = []

		for n in range(len(opciones)):
			identificador.append(str(n + 1))
			print(f'{str(n + 1)}) {opciones[n]}')
		print('*) Salir')
		identificador.append('*')

		while eleccion not in identificador:
			eleccion = input('>>> ').strip()
			if eleccion not in identificador:
				print('Selecciona una opción válida:')

		return eleccion


	def buscar_palabra(self):
		min_long_palabra = self.__dificultad[self.__nivel_dificultad]['min_long_palabra']
		palabra = self.__base[self.__base.Palabra.str.len() >= min_long_palabra].sample(1)
		self.__palabraTablero = palabra.palabra_para_jugar.values[0]
		self.__palabra = palabra.Palabra.values[0]

	def __crear_tablero(self):

		represe = re.sub('[A-Z]', '_', self.__palabraTablero)
		represe = list(represe)

		for l in self.__letras:
			represe[l] = self.__letras[l]

		self.__status = ''.join(represe) == self.__palabraTablero
		self.__tablero = '\n' + ' ' + ' '.join(represe) + '\n'

	def revisar_letra(self, eleccion):

		if eleccion.isalpha():
			eleccion = eleccion.upper()
		else:
			return False

		matches = list(re.finditer(eleccion, self.__palabraTablero))

		if matches and eleccion not in self.__letras.values():
			nuevos = {i.span()[0]: eleccion for i in matches}
			self.__letras.update(nuevos)
			return True

		return False