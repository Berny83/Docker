#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random

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
			return True
		else:
			self.x = display_width + 100 + random.randrange(-80, 60)
			return False
		
	def return_self(self, radius):
		self.x = radius

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
	crate_arr = []
	create_crate_arr(crate_arr)

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
		draw_array(crate_arr)
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

def create_crate_arr(array):
	array.append(Crate(display_width + 32, display_height - 170, 20, 70, 4))
	array.append(Crate(display_width + 300, display_height - 150, 30, 50, 4))
	array.append(Crate(display_width + 600, display_height - 170, 25, 80, 4))

def find_radius(array):
	maximum = max(array[0].x, array[1].x, array[2].x)

	if maximum < display_width:
		radius = display_width
		if radius - maximum < 50:
			radius += 150
	else:
		radius = maximum

	choice = random.randrange(0, 5)
	if choice == 0:
		radius += random.randrange(10,15)
	else:
		radius += random.randrange(200,350)
	return radius

def draw_array(array):
	for crate in array:
		check = crate.move()
		if not check: # if check == false
			radius = find_radius(array)
			crate.return_self(radius)

run_game()