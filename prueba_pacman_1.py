#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pygame')


# In[2]:


import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pac-Man")

# Definir los colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Definir las variables del juego
player_x = 320
player_y = 240
player_speed = 5

# Definir la función de dibujo
def draw():
    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (player_x, player_y), 10)
    pygame.display.update()

# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_UP:
                player_y -= player_speed
            elif event.key == pygame.K_DOWN:
                player_y += player_speed

    # Dibujar la pantalla
    draw()


# In[ ]:


import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Corriendo")

# Definir los colores
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Definir las variables del juego
person_x = 0
person_y = 240
person_speed = 5
person_color = BLUE

# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                person_x -= person_speed
            elif event.key == pygame.K_RIGHT:
                person_x += person_speed
            elif event.key == pygame.K_UP:
                person_y -= person_speed
            elif event.key == pygame.K_DOWN:
                person_y += person_speed
            elif event.key == pygame.K_SPACE:
                person_color = RED

    # Dibujar la pantalla
    screen.fill(BLACK)
    pygame.draw.circle(screen, person_color, (person_x, person_y), 10)
    pygame.display.update()


# In[ ]:





# In[ ]:




