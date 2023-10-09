
from models.bomba.bomba import Bomba
from utils.juego import Ahorcado

def main():
	juego = Ahorcado(Bomba)
	juego.ejecutar()

if __name__ == '__main__':
	main()
