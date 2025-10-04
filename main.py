#!/usr/bin/env python3
"""
Proyecto Python Principal
=========================

Este es el archivo principal del proyecto.
"""

def main():
    """Función principal del programa."""
    import sys
    
    print("¡Hola! Bienvenido a tu proyecto Python.")
    print("Este proyecto incluye un juego de Pacman.")
    print("\nOpciones disponibles:")
    print("1. Jugar Pacman (modo normal)")
    print("2. Jugar Pacman (modo dios - sin daño)")
    print("3. Salir")
    
    # Verificar argumentos de línea de comandos
    god_mode = "--god" in sys.argv or "-g" in sys.argv
    
    if god_mode:
        print("\nModo dios activado desde argumentos de línea de comandos")
        print("Iniciando juego de Pacman en modo dios...")
        try:
            from pacman_game import main as pacman_main
            pacman_main()
        except ImportError:
            print("Error: No se pudo importar el juego de Pacman.")
            print("Asegúrate de que pygame esté instalado: pip install pygame")
        except Exception as e:
            print(f"Error al ejecutar el juego: {e}")
            print("Para ejecutar el juego directamente, usa: python pacman_game.py")
        return
    
    while True:
        try:
            choice = input("\nElige una opción (1-3): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n¡Hasta luego!")
            break
        
        if choice == "1":
            print("\nIniciando juego de Pacman (modo normal)...")
            try:
                from pacman_game import main as pacman_main
                pacman_main()
            except ImportError:
                print("Error: No se pudo importar el juego de Pacman.")
                print("Asegúrate de que pygame esté instalado: pip install pygame")
            except Exception as e:
                print(f"Error al ejecutar el juego: {e}")
            break
        elif choice == "2":
            print("\nIniciando juego de Pacman (modo dios)...")
            try:
                from pacman_game import PacmanGame
                game = PacmanGame(god_mode=True)
                game.run()
            except ImportError:
                print("Error: No se pudo importar el juego de Pacman.")
                print("Asegúrate de que pygame esté instalado: pip install pygame")
            except Exception as e:
                print(f"Error al ejecutar el juego: {e}")
            break
        elif choice == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige 1, 2 o 3.")


if __name__ == "__main__":
    main()
