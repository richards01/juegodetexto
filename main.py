# Pide el nombre del jugador por teclado
jugador = input("Ingrese su nombre: ")

# Imprime un mensaje de bienvenida con el nombre del jugador
print(f"Bienvenid@ al juego de laberintos, {jugador}!")

import readchar

def main():
    print("Presiona ↑ para salir.")
    
    while True:
        char = readchar.readkey()
        print(f"Tecla presionada: {char}")
        
        if char == '\x1b[A':  # '\x1b' representa la tecla Escape, seguida por [A para ↑
            print("Tecla ↑ presionada. Saliendo...")
            break

if __name__ == "__main__":
    main()