#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

pygame.init()
# игра - это бесконечный цикл, пока пользователь не нажмет крестик, не доиграет

display_width = 878
display_height = 550

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Fox_test')

icon = pygame.image.load('Sunny-land-files-nc/icon.png')
pygame.display.set_icon(icon)
# png разрешение, чтобы края незаполенные рисунком были прозрачные

class Crate:
	def __init__(self, x, y, width, height, speed):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed

	def move(self):
		if self.x >= -self.width:
			pygame.draw.rect(display, (224, 121, 32), (self.x, self.y, self.width, self.height))
			self.x -= self.speed
	else:
			self.x = display_width - 50

usr_width = 72
usr_height = 70
usr_x = display_width // 3
usr_y = display_height - usr_height - 100
# декартовые координаты - ось х и ось y

big_crate_w = 32
big_crate_h = 32
big_crate_x = display_width - 50
big_crate_y = display_height - big_crate_h - 100

clock = pygame.time.Clock()
# кол-во кадров в сек, кол-во обходов данного цикла (run_game)

make_jump = False
jump_counter = 30

def run_game(): # запускаем игру
	global make_jump
	game = True

	while game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			make_jump = True
		if make_jump:
			jump()

		display.fill((255, 255, 255))
		draw_crate()
		pygame.draw.rect(display, (0, 0, 255), (usr_x, usr_y, usr_width, usr_height))
		pygame.display.update()
		clock.tick(80) # 80 милисек

def jump():
	global usr_y, make_jump, jump_counter
	if jump_counter >= -30:
		usr_y -= jump_counter / 2.5
		jump_counter -=1
	else:
		jump_counter = 30
		make_jump = False

def draw_crate():
	global big_crate_w, big_crate_h, big_crate_x, big_crate_y

	if big_crate_x >= -big_crate_w:
		pygame.draw.rect(display, (224, 121, 32), (big_crate_x, big_crate_y, big_crate_w, big_crate_h))
		big_crate_x -= 4
	else:
		big_crate_x = display_width - 50


run_game()