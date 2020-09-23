#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame # подключили библиотеку

pygame.init() # инициализировали библиотеку
window = pygame.display.set_mode((550, 550)) # создали окно с размером 550 на 550
pygame.display.set_caption("Cubes Game") # add the header of game
# export DISPLAY=localhost:0.0

# creating a player
# his position on display
x = 50
y = 480
# his width and height
width = 40
height = 60
# his speed of movement
speed = 10
# jump
isJump = False
jumpCount = 10

# бесконечный цикл отслеживания действий игрока
run = True
while run:
	pygame.time.delay(50) #милисекунды
	# цикл выполняется каждую 0.1 сек
	# время ч/з кот-е цикл будет обратно выполняться
	# было 100, поменяли на 50, чтобы игра обновлялась быстрее

	for event in pygame.event.get(): 
		#pygame.event.get() - массив с событиями, перебираем его
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	# массив нажатых кнопок
	if keys[pygame.K_LEFT] and x > speed:
		x -= speed
	if keys[pygame.K_RIGHT] and x < (550 - width - speed):
		x +=speed
	if not(isJump): # чтобы не перемещался вверх при прыжке
		if keys[pygame.K_UP] and y > speed:
			y -= speed
		if keys[pygame.K_DOWN] and y < (550 - height - speed):
			y +=speed
		if keys[pygame.K_SPACE]:
			isJump = True
	else: # прыжок по параболе
		if jumpCount >= -10:
			if jumpCount < 0:
				y += (jumpCount ** 2) / 2
			else:
				y -= (jumpCount ** 2) / 2
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10

	window.fill((0,0,0))
	# закрашиваем окно в черный цвет, чтобы создать эффект передвижения,
	# а то линии полностью рисуются
	pygame.draw.rect(window, (0,0,255), (x, y, width, height))
	# рисуем квадрат на поверхности window в цвете RGB - его расположение, ширину и высоту
	pygame.display.update()
	# обновляем окно - чтобы видеть изменения		

pygame.quit() # закрывает приложение