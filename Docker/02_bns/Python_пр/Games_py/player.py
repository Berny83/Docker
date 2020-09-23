#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from main_game import usr_y

if __name__ == "__main__":
	print("Hello, player module")

class Player:
	usr_width = 72
	usr_height = 70
	make_jump = False
	jump_counter = 30

	def jump(self, make_jump, jump_counter):
		global usr_y
		if self.jump_counter >= -30:
			usr_y -= self.jump_counter / 2.5
			self.jump_counter -=1
		else:
			self.jump_counter = 30
			self.make_jump = False