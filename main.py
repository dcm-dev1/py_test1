#!/usr/bin/env python3
"""
Proyecto Python Principal
=========================

Este es el archivo principal del proyecto.
"""

def main():
    """Función principal del programa."""
    print("¡Hola! Bienvenido a tu proyecto Python.")
    print("Este proyecto incluye un juego de Pacman.")
    print("\nIniciando juego de Pacman...")
    
    try:
        from pacman_game import main as pacman_main
        pacman_main()
    except ImportError:
        print("Error: No se pudo importar el juego de Pacman.")
        print("Asegúrate de que pygame esté instalado: pip install pygame")
    except Exception as e:
        print(f"Error al ejecutar el juego: {e}")
        print("Para ejecutar el juego directamente, usa: python pacman_game.py")


if __name__ == "__main__":
    main()
