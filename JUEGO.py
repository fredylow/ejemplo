import pygame
import random

# Inicialización de Pygame
pygame.init()

# Tamaño de la pantalla del juego
ancho_pantalla = 800
alto_pantalla = 600

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

# Creación de la pantalla del juego
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Pac-Man")

# Posición y tamaño del Pac-Man
pacman_x = 400
pacman_y = 300
pacman_radio = 20

# Velocidad del Pac-Man
pacman_velocidad = 1

# Dirección inicial del Pac-Man
pacman_direccion = "derecha"

# Función para dibujar al Pac-Man en la pantalla
def dibujar_pacman(x, y):
    pygame.draw.circle(pantalla, rojo, (x, y), pacman_radio)
    pygame.draw.polygon(pantalla, negro, ((x, y), (x + pacman_radio, y + pacman_radio//2), (x + pacman_radio, y - pacman_radio//2)))

# Bucle principal del juego
terminado = False
while not terminado:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True

    # Movimiento del Pac-Man
    teclas_pulsadas = pygame.key.get_pressed()
    if teclas_pulsadas[pygame.K_LEFT]:
        pacman_x -= pacman_velocidad
        pacman_direccion = "izquierda"
    if teclas_pulsadas[pygame.K_RIGHT]:
        pacman_x += pacman_velocidad
        pacman_direccion = "derecha"
    if teclas_pulsadas[pygame.K_UP]:
        pacman_y -= pacman_velocidad
        pacman_direccion = "arriba"
    if teclas_pulsadas[pygame.K_DOWN]:
        pacman_y += pacman_velocidad
        pacman_direccion = "abajo"

    # Lógica del juego

    # Dibujar en la pantalla
    pantalla.fill(negro)
    dibujar_pacman(pacman_x, pacman_y)
    pygame.display.update()

# Finalizar Pygame
pygame.quit()