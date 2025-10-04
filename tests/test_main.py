"""
Pruebas unitarias para el módulo principal
"""
import unittest
import sys
import os

# Agregar el directorio raíz al path para importar el módulo principal
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import main


class TestMain(unittest.TestCase):
    """Pruebas para la función main"""
    
    def test_main_runs_without_error(self):
        """Prueba que la función main se ejecuta sin errores"""
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised {type(e).__name__} unexpectedly: {e}")


if __name__ == '__main__':
    unittest.main()
