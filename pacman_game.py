#!/usr/bin/env python3
"""
Juego de Pacman
==============

Un juego clásico de Pacman implementado en Python con pygame.
"""

import pygame
import sys
import random
from enum import Enum

# Inicializar pygame
pygame.init()

# Constantes del juego
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.speed = 0.1
        self.radius = 8
        
    def update(self, maze):
        # Cambiar dirección si es posible
        if self.can_move(maze, self.next_direction):
            self.direction = self.next_direction
        
        # Mover en la dirección actual
        if self.can_move(maze, self.direction):
            dx, dy = self.direction.value
            self.x += dx * self.speed
            self.y += dy * self.speed
            
            # Mantener dentro de los límites
            self.x = max(0, min(GRID_WIDTH - 1, self.x))
            self.y = max(0, min(GRID_HEIGHT - 1, self.y))
    
    def can_move(self, maze, direction):
        dx, dy = direction.value
        new_x = int(self.x + dx)
        new_y = int(self.y + dy)
        
        if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
            return maze[new_y][new_x] != 1
        return False
    
    def set_direction(self, direction):
        self.next_direction = direction
    
    def draw(self, screen):
        center_x = int(self.x * CELL_SIZE + CELL_SIZE // 2)
        center_y = int(self.y * CELL_SIZE + CELL_SIZE // 2)
        pygame.draw.circle(screen, YELLOW, (center_x, center_y), self.radius)

class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.direction = Direction.UP
        self.speed = 0.05
        self.radius = 8
        
    def update(self, maze, pacman):
        # IA simple: moverse hacia Pacman
        dx = pacman.x - self.x
        dy = pacman.y - self.y
        
        # Elegir dirección basada en la distancia
        if abs(dx) > abs(dy):
            if dx > 0 and self.can_move(maze, Direction.RIGHT):
                self.direction = Direction.RIGHT
            elif dx < 0 and self.can_move(maze, Direction.LEFT):
                self.direction = Direction.LEFT
        else:
            if dy > 0 and self.can_move(maze, Direction.DOWN):
                self.direction = Direction.DOWN
            elif dy < 0 and self.can_move(maze, Direction.UP):
                self.direction = Direction.UP
        
        # Mover en la dirección elegida
        if self.can_move(maze, self.direction):
            dx, dy = self.direction.value
            self.x += dx * self.speed
            self.y += dy * self.speed
            
            # Mantener dentro de los límites
            self.x = max(0, min(GRID_WIDTH - 1, self.x))
            self.y = max(0, min(GRID_HEIGHT - 1, self.y))
    
    def can_move(self, maze, direction):
        dx, dy = direction.value
        new_x = int(self.x + dx)
        new_y = int(self.y + dy)
        
        if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
            return maze[new_y][new_x] != 1
        return False
    
    def draw(self, screen):
        center_x = int(self.x * CELL_SIZE + CELL_SIZE // 2)
        center_y = int(self.y * CELL_SIZE + CELL_SIZE // 2)
        pygame.draw.circle(screen, self.color, (center_x, center_y), self.radius)

class PacmanGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pacman Game")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Crear laberinto simple
        self.maze = self.create_maze()
        
        # Crear Pacman
        self.pacman = Pacman(1, 1)
        
        # Crear fantasmas
        self.ghosts = [
            Ghost(18, 1, RED),
            Ghost(18, 8, PINK),
            Ghost(1, 8, CYAN),
            Ghost(9, 4, ORANGE)
        ]
        
        # Puntuación y vidas
        self.score = 0
        self.lives = 3
        self.pellets = self.create_pellets()
        
        # Fuente para texto
        self.font = pygame.font.Font(None, 36)
    
    def create_maze(self):
        """Crear un laberinto simple"""
        maze = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        
        # Paredes exteriores
        for i in range(GRID_WIDTH):
            maze[0][i] = 1
            maze[GRID_HEIGHT-1][i] = 1
        for i in range(GRID_HEIGHT):
            maze[i][0] = 1
            maze[i][GRID_WIDTH-1] = 1
        
        # Paredes internas
        for i in range(5, 15):
            maze[5][i] = 1
            maze[10][i] = 1
        
        for i in range(5, 10):
            maze[i][5] = 1
            maze[i][15] = 1
        
        return maze
    
    def create_pellets(self):
        """Crear pellets (puntos) en el laberinto"""
        pellets = []
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.maze[y][x] == 0:
                    pellets.append((x, y))
        return pellets
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pacman.set_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.pacman.set_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.pacman.set_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.pacman.set_direction(Direction.RIGHT)
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self):
        # Actualizar Pacman
        self.pacman.update(self.maze)
        
        # Actualizar fantasmas
        for ghost in self.ghosts:
            ghost.update(self.maze, self.pacman)
        
        # Verificar colisiones con pellets
        pacman_grid_x = int(self.pacman.x)
        pacman_grid_y = int(self.pacman.y)
        
        if (pacman_grid_x, pacman_grid_y) in self.pellets:
            self.pellets.remove((pacman_grid_x, pacman_grid_y))
            self.score += 10
        
        # Verificar colisiones con fantasmas
        for ghost in self.ghosts:
            distance = ((self.pacman.x - ghost.x)**2 + (self.pacman.y - ghost.y)**2)**0.5
            if distance < 0.5:
                self.lives -= 1
                if self.lives <= 0:
                    self.game_over()
                else:
                    # Resetear posición de Pacman
                    self.pacman.x = 1
                    self.pacman.y = 1
        
        # Verificar victoria
        if len(self.pellets) == 0:
            self.victory()
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Dibujar laberinto
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.maze[y][x] == 1:
                    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(self.screen, BLUE, rect)
        
        # Dibujar pellets
        for x, y in self.pellets:
            center_x = x * CELL_SIZE + CELL_SIZE // 2
            center_y = y * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(self.screen, WHITE, (center_x, center_y), 2)
        
        # Dibujar Pacman
        self.pacman.draw(self.screen)
        
        # Dibujar fantasmas
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        
        # Dibujar UI
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        
        pygame.display.flip()
    
    def game_over(self):
        """Mostrar pantalla de game over"""
        self.screen.fill(BLACK)
        game_over_text = self.font.render("GAME OVER", True, RED)
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        restart_text = self.font.render("Press ESC to exit", True, WHITE)
        
        self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))
        self.screen.blit(score_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
        self.screen.blit(restart_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 50))
        pygame.display.flip()
        
        # Esperar a que presione ESC
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    waiting = False
                    self.running = False
    
    def victory(self):
        """Mostrar pantalla de victoria"""
        self.screen.fill(BLACK)
        victory_text = self.font.render("VICTORY!", True, GREEN)
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        restart_text = self.font.render("Press ESC to exit", True, WHITE)
        
        self.screen.blit(victory_text, (SCREEN_WIDTH//2 - 80, SCREEN_HEIGHT//2 - 50))
        self.screen.blit(score_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
        self.screen.blit(restart_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 50))
        pygame.display.flip()
        
        # Esperar a que presione ESC
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    waiting = False
                    self.running = False
    
    def run(self):
        """Bucle principal del juego"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

def main():
    """Función principal"""
    print("¡Bienvenido al juego de Pacman!")
    print("Controles:")
    print("- Usa las flechas del teclado para mover a Pacman")
    print("- Recoge todos los puntos blancos para ganar")
    print("- Evita a los fantasmas")
    print("- Presiona ESC para salir")
    print("\n¡Que comience el juego!")
    
    game = PacmanGame()
    game.run()

if __name__ == "__main__":
    main()
