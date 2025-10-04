# Proyecto Python - Juego de Pacman

Un proyecto Python que incluye un juego completo de Pacman implementado con pygame.

## Descripción

Este proyecto incluye:
- **Juego de Pacman completo** con gráficos y sonido
- Estructura de directorios organizada
- Archivo de dependencias (requirements.txt)
- Configuración de Git (.gitignore)
- Documentación completa
- Sistema de pruebas unitarias

## Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd py_test_1
```

2. Crea un entorno virtual:
```bash
python -m venv venv
```

3. Activa el entorno virtual:
- En Windows:
```bash
venv\\Scripts\\activate
```
- En Linux/Mac:
```bash
source venv/bin/activate
```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar el juego de Pacman

**Opción 1: Ejecutar directamente**
```bash
python pacman_game.py
```

**Opción 2: Usar el menú principal**
```bash
python main.py
```

### Controles del juego
- **Flechas del teclado**: Mover a Pacman (↑↓←→)
- **ESC**: Salir del juego
- **Objetivo**: Recoger todos los puntos blancos evitando a los fantasmas

### Características del juego
- 🎮 **4 fantasmas** con IA que persiguen a Pacman
- 🏆 **Sistema de puntuación** (10 puntos por pellet)
- ❤️ **Sistema de vidas** (3 vidas iniciales)
- 🏁 **Condiciones de victoria/derrota**
- 🎨 **Gráficos coloridos** con pygame

## Estructura del Proyecto

```
py_test_1/
├── main.py              # Archivo principal con menú
├── pacman_game.py       # Juego de Pacman completo
├── requirements.txt     # Dependencias del proyecto
├── README.md           # Documentación
├── .gitignore          # Archivos ignorados por Git
├── src/                # Código fuente adicional
│   └── __init__.py
├── tests/              # Pruebas unitarias
│   ├── __init__.py
│   └── test_main.py
├── docs/               # Documentación adicional
│   └── README.md
└── venv/               # Entorno virtual (no incluido en Git)
```

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.
