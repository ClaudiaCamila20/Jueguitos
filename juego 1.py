#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random
import math

# Inicializar pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Nombre aleatorio")

# Fuente de texto
font = pygame.font.SysFont(None, 40)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Lista de nombres
nombres = ["Inglaterra", "EEUU", "Alemania", "Rusia", "China", "Cuba","Francia"]

# Círculo rojo
radio = 50
centro_circulo = (200, 350)

# Contador de clics
clicks = 0

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener las coordenadas del clic
            pos = pygame.mouse.get_pos()
            x, y = pos
            
            # Calcular la distancia al centro del círculo
            distancia = math.sqrt((x - centro_circulo[0])**2 + (y - centro_circulo[1])**2)
            
            # Incrementar el contador de clics si el clic está dentro del círculo
            if distancia <= radio:
                clicks += 1
                
                # Generar un nuevo nombre aleatorio
                if clicks % 2 == 1:
                    nombre_aleatorio = random.choice(nombres)
                else:
                    nombre_aleatorio = ""
                
                # Mostrar el nombre aleatorio en pantalla
                nombre_mostrado = font.render(nombre_aleatorio, True, BLACK)
                screen.fill(WHITE)
                screen.blit(nombre_mostrado, (100, 100))
    
    # Dibujar el círculo
    pygame.draw.circle(screen, RED, centro_circulo, radio)
    
    # Actualizar pantalla
    pygame.display.flip()

# Salir de pygame
pygame.quit()


# In[2]:


pygame.quit()


# In[ ]:




