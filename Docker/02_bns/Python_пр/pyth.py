#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print("Hello")
# print(3 ** 2)
# print(3 + 2)
# print(2.56 - 45)
# print(25 // 7)
# # сколько 7 в числе 25 - вывод:3
# print(25 % 7) # остаток

# import sys
# print(sys.version_info)
# namge = input("Как Вас зовут? ")
# print("Привет,", namge)

#Works in Python 2 and 3:
# try: input = raw_input
# except NameError: pass
# print("Hi, " + input("Your name: "))

# num_1 = float (input ("Enter first num: "))
# num_2 = input ("Enter second num: ")
# res = num_1 + float (num_2)
# res += 5
# Res = input ("Enter your string: ")
# Res -= 5
# print(Res)
# print("Result is", res)

# num = input ("Your number: ")
# if int(num) > 0:
# 	if int(num) > 10:
# 		print("Pos10")
# 	else:
# 		print("Pos0to10")
# 	print("Pos\n")
# elif int(num) < -10:
# 	print("Neg")
# else:
# 	print("from -10 to 0")
# print("Port")

# name = input ()
# A = 'Yes' if name != "Test" else 'No'
# print (A)

# i = 0
# while i < 10:
# 	print(i)
# 	i += 2

# for j in 'hello world':
# 	if j == 'a':
# 		break # выходит из цикла
# else:
# 	print("Нет буквы а")

# lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'o', 'n', 'g']]
# print(lis)

# a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
# print(a)

# l = [] # пустой список
# l.append(23) # добавляет эл-нт в конец списка
# l.append(34)
# b = [2, 3]
# l.extend(b) # добавляет в конец списка эл-нты др. списка
# l.insert (1, 56) # в l[1] - вместо 34 ставит 56 вставляет эл-нт по индексу
# l.append(34)
# l.remove(34) 
# # удаляет эл-нт по значению, если эл-нт такой не находится выдает valueerror
# # удаляет первый 34
# l.pop ()
# # удаляет по индексу, если ничего не указывать - удаляет посл.эл-нт
# print(l.index(56)) # возвр-т индекс значения
# print(l.count(34)) # подсчитывает кол-во эл-тов со знач-ем 34
# l.sort () 
# # сортирует список на основе какой-либо функции
# # если ничего не вводить, то просто по возрастанию
# l.reverse() # переворачивает список
# # l.clear() - очищает список 
# print(l)

# l = [34, 'sd', 56, 34.34]
# print(l[-2::-2])

# a = (43, 56, 45.23, 'd') # кортеж
# b = [42, 56, 45.23, 'd'] # список

# print(a.__sizeof__()) # определяет размер
# print(b.__sizeof__())

# a = ("hello world")
# print (a)

# d = {} # пустой словарь
# b = {'name': "Robert", 'age': 12}
# c = dict(short='dict', longer='dictionary')
# c['short'] = 34 
# # была ошибка - выводил c['short'] = 34 NameError: name 'c' is not defined - ввела с на русском языке
# f = dict ([("name", "Susan"), ("age", 13)]) # внутри список, в списке - кортеж
# e = dict.fromkeys (['a', 'b'])
# j = dict.fromkeys (['a', 'b'], 1)
# h = {a : a ** 2 for a in range(7)} # а в пределах от 0 до 6 будет возводиться в степень
# print("b: ", b)
# print("c: ", c)
# print("f: ", f)
# print("e: ", e)
# print("j: ", j)
# print("h: ", h)

# person = {'name': {'last_name': 'Rojkov', 'first_name': 'Nicolay', 'middle_name': 'Petrovich'}, 'address': ['London', 'Bright Avenue 11', 'app.4'], 'phone': {'home_phone': '34-44-57', 'mobile_phone': '8-965-345-56-75'}}
# print(person)
# print("Name:\n", person['name'])
# print("Mobile phone:\n", person['phone']['mobile_phone'])
# print("Keys:\n", person.keys())
# print("Values:\n", person.values())

# a = set () # пустое множество
# print (a)
# print (type(a))
# b = set("hello")
# print (b)
# print (type(b))
# c = {'23', 32} # множества без ключей, если введем ключ, то класс поменяется на словарь
# print (c)
# print (type(c))
# d = {i ** 2 for i in range (10)}
# print (d)
# print (type(d))
# e = {}
# print (e)
# print (type(e))

# a = set ("Hello")
# b = frozenset("Qwerty") # как в кортежах не можем добавлять, удалять и заменять эл-нты
# a.add(1)
# b.add(1) # не сработает
# print (a)
# print (b)

# a = ['r', 's', 'w', 'a', 's', 'w'] 
# print (a) # просто список
# print (set (a)) # переопределили в множество

# a = {32, 45, 43.23, 76}
# x = 45
# b = 56
# c = {67, 12, 90}
# d = {32, 45, 76}
# e = {32, 45, 76, 43.23}
# print (len(a))
# print (x in a)
# print (b in a)
# print (a.isdisjoint(c)) # истина, если не имеют общих эл-нтов
# print ("a == d:", a == d)
# print ("a == e:", a == e)

# a = {32, 45, 43.23, 76}
# x = {23, 45, 12, 43.23}
# # a.intersection_update(x) # выводит пересечения (одинаковые) числа
# # a.difference_update(x) # выводит разность - все числа множества а, кот-х нет в х
# # a.update(x)
# # a.symmetric_difference_update(x) # строгая дизъюннкция ( исключающее или) - все неодинаковые числа в множествах а и х: есть в а, но нет в х - или есть в х, но нет а
# # a.add (23)
# # a.remove(32)
# # a.discard(11) # в отличие от add не выдает ошибку, если не находит значение
# # a.pop() # удаляет первый элемент из множества
# # a.clear()
# print(a)

# def func (x):
# 	def add (a):
# 		return x + a
# 	return add

# test = func(100)
# print (test (200))

# def func (r, w, y = 2):
# 	res = r + w
# 	res *= y
# 	return res
# print (func(4,2))

# def func (*args):
# 	return args
# print (func('sd', 45.2, 3))

# def func (**args):
# 	return args
# print (func (a=23, n=56, k=90))

# def func (**args):
# 	return args
# print (func (short='dict', longer='donslmcm'))

# add = lambda x, y: x + y
# add2 = lambda x, y: x * y
# print(add(5, 2))
# print (add2('q', 4))
# print ((lambda u, p: u - p)(8, 3))

# try:
# 	x = int(input())
# 	y = int(input())
# 	res = x / y
# except ZeroDivisionError:
# 	res = "You can't divide to 0"
# except ValueError:
# 	res = "It's string."
# else:
# 	res = "Okay"
# finally:
# 	print ("Выполнится 100%")
# print (res)

# f = open ('text.txt') # по умолчанию стоит rt, форматы можно совмещать
# # f = open ('text.txt', 'rt')
# # print (f.read(4)) - выводит 4 символа
# # print (f.read()) - выводит все
# for line in f:
# 	print (line)
# f.close()

# f = open ('text.txt', 'w')
# f.write ("Hi, is's me\nNet")
# f.close

# with open('test.txt', 'wt', encoding='utf-8') as File:
# 	num = int(input())
# 	line = str('1 / ' + str(num) + ' = ' + str(1/num))
# 	print(line)
# 	File.write(line)

# import math
# # модуль (библиотека )с матем. функциями

# print (math.pi)
# print (math.e)
# print (math.cos(1))

# import time
# import os
# import random as r # псевдоним для модуля
# # если неуверен, что модуль существует, чтобы программа не накрылась
# try:
# 	import nomodule
# except ImportError:
# 	print ("Модуля nomodule не существует")

# import moduleM as m

# print(time.time())
# print (os.getcwd()) # путь - типа pwd
# print (os.uname())
# print (r.random()) # рандомное число
# m.hi()
# print (m.add(45,15))

# from moduleM import hi

# hi()

# class Person:
# 	name = "Ivan"
# 	age = 10

# 	def __init__(self, name1, age1):
# 		self.name = name1
# 		self.age = age1

# 	def set(self, name1, age1):
# 		self.name = name1
# 		self.age = age1

# class Student (Person):
# 	course = 1

# 	def set(self, name1, age1, course1):
# 		self.name = name1
# 		self.age = age1
# 		self.course = course1

# igor = Student("Igor", 19)
# # igor._Person__set ("Igor", 19)
# igor.set("Игорь", 23, 5)
# print ("Name: ", igor.name, ", age: ", igor.age, ", course: ", igor.course)

# vlad = Person ("Влад", 25)
# # vlad._Person__set ("Влад", 25)
# print (vlad.name + " " + str(vlad.age))

# ivan = Person ("Иван", 55)
# # ivan._Person__set ("Иван", 55)
# print (ivan.name + " " + str(ivan.age))

# def decorator(func):
# 	def wrapper():
# 		print("Код до выполнения функции")
# 		func()
# 		print("Код, кот-й сработал после функции")
# 	return wrapper

# def qwe(func):
# 	def wrapper():
# 		print("Код до выполнения функции 2")
# 		func()
# 		print("Код, кот-й сработал после функции 2")
# 	return wrapper

# @decorator # decorator оборачивает qwe, qwe оборачивает функцию show
# @qwe
# def show():
# 	print("Я обычная функция")

# show()
# # dec = decorator(show)
# # dec()

def decorator(func):
	def wrapper():
		print("Код до выполнения функции")
		func()
		print("Код, кот-й сработал после функции")
	return wrapper

def show():
	print("Я обычная функция")

show()
dec = decorator(show)
dec()