#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame # подключили библиотеку

pygame.init() # инициализировали библиотеку
window = pygame.display.set_mode((878, 550)) # создали окно с размером 550 на 550
pygame.display.set_caption("Cubes Game") # add the header of game
# export DISPLAY=localhost:0.0

# sprites
walkRight = [pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-1.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-2.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-3.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-4.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-5.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-6.png')]

walkLeft = [pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-7.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-8.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-9.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-10.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-11.png'), pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/run/player-run-12.png')]

playerStand = pygame.image.load('Sunny-land-files-nc/PNG/sprites/player/idle/player-idle-1.png')
bg = pygame.image.load('Sunny-land-files-nc/PNG/environment/layers/back1.png')

clock = pygame.time.Clock()

# creating a player
# his position on display
x = 50
y = 470
# his width and height
width = 72
height = 70
# his speed of movement
speed = 5
# jump
isJump = False
jumpCount = 10 # при значении 3 - падает вниз за экран
# animation - right and left - игрок не двигается влево или вправо, стоит на месте
left = False
right = False
animCount = 0

# вынесли функцию, кот-я рисует
def drawWindow():
	global animCount
	window.blit(bg, (0, 0)) # изображ и координаты

	if animCount + 1 >= 30: # в нашей игре 30 кадров в сек = (FPS) frames per second
		animCount = 0
		# чтобы не вышли за рамки списка
	if left:
		window.blit(walkLeft[animCount // 5], (x,y)) # округление к меньшему
		animCount += 1
		# если движется влево - рисуем, проигрывается анимация
	elif right:
		window.blit(walkRight[animCount // 5], (x,y))
		animCount += 1
	else:
		window.blit(playerStand, (x,y))

	pygame.display.update()
	# обновляем окно - чтобы видеть изменения

# бесконечный цикл отслеживания действий игрока
run = True
while run:
	clock.tick(30) # 30 кадров в сек
	# время ч/з кот-е цикл будет обратно выполняться

	for event in pygame.event.get(): 
		#pygame.event.get() - массив с событиями, перебираем его
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	# массив нажатых кнопок
	# удалили идти вверх
	if keys[pygame.K_LEFT] and x > speed:
		x -= speed
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x < (878 - width - speed):
		x +=speed
		left = False
		right = True
	else:
		left = False
		right = False
		animCount = 0
		# кол-во проигранных анимаций = 0, чтобы как только мы начнем ходить анимацию начала проигрываться с 0, первого спрайта.

	if not(isJump): # чтобы не перемещался вверх при прыжке
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
	drawWindow()

pygame.quit() # закрывает приложение