from utils import *

def playgame():
    # Llamamos a la función de utils que prepara todo de una vez
    p1_tablero, p1_tablero_p2, p2_tablero, p2_tablero_p1 = inicializar_juego()

    # Mensaje de Bienvenida
    print_lento("=" * 60)
    print_lento(r"""
    ____      _      _          _      ____    ____     ___  
    | __ )    / \    | |        / \    |  _ \  |  _ \   / _ \ 
    |  _ \   / _ \   | |       / _ \   | | | | | |_) | | | | |
    | |_) | / ___ \  | |___   / ___ \  | |_| | |  _ <  | |_| |
    |____/ /_/   \_\ |_____| /_/   \_\ |____/  |_| \_\  \___/ 
                                                            
                🚢 PROYECTO NAVAL INICIADO 🚢
                🚢 EL JUEGO DE HUNDIR LA FLOTA 🚢
    """)
    print_lento("=" * 60)
    print_lento(f"{'¡BIENVENIDO, CAPITÁN!':^60}")
    print_lento(f"{'Prepárate para la batalla contra la CPU':^60}")
    print_lento("=" * 60)
    print_lento("\n")
    
    respuesta = input("¿Comenzamos el juego? (si/no): ").lower().strip()
    
    play = True if respuesta == "si" else False
    turno = True

    while play:
        if turno:
            print("\n" + "=" * 41)
            print(f"{'¡TU TURNO!':^41}")
            print("=" * 41)

            print("TABLERO:\n", p1_tablero)
            print("RADAR DE ATAQUE:\n", p1_tablero_p2)
            
            coord1 = input("Selecciona una fila (1-10): ")
            coord2 = input("Selecciona una columna (1-10): ")
            
            # Llamamos a tu función disparo con sus argumentos
            acertado = disparo(coord1, coord2, p2_tablero, p1_tablero_p2)
            
            if not acertado:
                turno = False
        else:
            print("\n____CPU____")
            coord_maquina = generador_coord()
            print(f"La CPU dispara a la casilla: {coord_maquina}")
            
            # La CPU dispara a tu tablero
            acertado_maquina = recibir_disparo(p1_tablero, p2_tablero_p1, coord_maquina)
            
            if not acertado_maquina:
                turno = True
            else:
                print("¡Que cabrón! Nos ha dado. Va a volver a disparar.")

        # COMPROBACIÓN DE VICTORIA
        if "O" not in p2_tablero:
            print("\n🏆 ¡Acabas de destruir toda la flota! ¡FELICIDADES!")
            play = False
        elif "O" not in p1_tablero:
            print("\n💀 Han destruido todos tus barcos... Has perdido.")
            play = False

if __name__ == "__main__":
    playgame()