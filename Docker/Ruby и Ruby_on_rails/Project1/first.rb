puts("Hello, world!")

#puts("Введите свое имя: ")
#name = gets.chomp()
#puts("Ваше имя: " + name + ", ты крут!")

#print("Put first number:")
#x = gets.chomp()
#print("Put second number:")
#y = gets.chomp().to_i
#puts(x.to_i + y)

#arr = Array[4, 6, 8, 12, true, "Hello", 5.64]
#puts(arr)

#names = Array["Gear", "Marie", "Elein"]
#puts(names[1])
#puts(names[-1])

#list = Array.new
#list[0] = 12
#list[7] = 36
#puts list
#puts list.length()
#puts list.include? 12

# countries = {
# 	"RU" => "Russia",
# 	1 => 1.01,
# 	:UA => "Ukraine"
# }
# puts countries["RU"]
# puts countries[1]
# puts countries[:UA]

# def	sayHello
# 	puts "Hello, world!"
# end

# sayHello
# sayHello
# sayHello

def	saywHello(word="Ruby", num=2)
	puts "Hello, world!"
	puts ("Your word: " + word + " and your num: " + num.to_s)
end

saywHello

#def	summa(x, y)
#	return x + y, 70
#end

#res = summa(6, 5)
#puts res
#puts res[0]
#puts res[1]

x = 23
y = 3

if x < y
	puts("Smaller")
	puts("!")
elsif x == y
	puts("same")
elsif x == 23
	puts("x = 5")
	if x > 12
		puts("123")
	end
elsif x == 3
	puts("x = 3")
elsif x == 6
	puts("x = 6")
else
	puts("Bigger")
end

isSmall = true
if isSmall and x !=8
	puts("OK")
end

day = '1'
puts "Monday" if day == '1'

def	getDayWeek(day)
	nameOfDay = ""

	case day
	when 1
		nameOfDay = "Monday"
	when 2
		nameOfDay = "Tuesday"
	when 3
		nameOfDay = "Wednesday"
	when 4
		nameOfDay = "Thursday"
	when 5
		nameOfDay = "Friday"
	when 6, 7
		nameOfDay = "weekend"
	else
		nameOfDay = "Wrong"
	end

	return nameOfDay
end

puts getDayWeek(6)

# i = 0
# while i <= 5
# 	puts i
# 	i += 1
# end

# secret = "Blue"
# guess = ""

# while guess != secret
# 	puts("Input your word: ")
# 	guess = gets.chomp()
# end

puts "You win!"

# for el in 0..5
# 	puts el
# end

# arr = [4, 6, 8, 12, true, "Hello", 5.64]
# puts(arr)

# names = ["Bob", "Helena", "Alex", "Rina"]

# for name in names
# 	name += "!"
# 	puts name
# end
# puts names

# for el in 0..names.length() - 1
# 	names[el] += "!"
# end
# puts names

# 6.times do |index|
# 	puts index
# end

# names.each do |nm|
# 	puts nm += "!"
# end

# File.open("text/sample.txt", "r") do |file|
# 	puts file
# 	puts file.read()
# 	puts file.read().include? "b"
# 	puts file.readline()
# 	puts file.readline()
# 	puts file.readchar()

# 	for line in file.readlines()
# 		puts line
# 	end
# end

# file = File.open("text/sample.txt", "r")
# puts file.read()

# file.close()

# File.open("text/sample.txt", "a") do |file|
# 	file.write("\nRuby on Rails")
# end

# File.open("text/index.html", "w") do |file|
# 	file.write("<h4>Hello, world!<h4>")
# end
# list = [10, 2, 5, 8, 12]

# begin
# 	list["dog"]
# 	num = 10 / 0
# rescue TypeError => e
# 	puts e
# rescue ZeroDivisionError
# 	puts "Zero division"
# end

# puts "Hello"

# class Car
# 	# 1 буква в верхнем регистре, остальные в нижнем
# 	attr_accessor :speed, :model, :color

# 	# конструктор - выполняются всякий раз когда мы создаем новый объект
# 	# выведет Hello дважды, т.к. при создании новых объектов Car.new()
# 	def initialize()
# 		puts "Hello"
# 	end
# end

# bmw = Car.new()
# bmw.speed = 230
# bmw.model = "BMW"
# bmw.color = "Black"

# audi = Car.new()
# audi.speed = 250
# audi.model = "audi"
# audi.color = "white"

# puts bmw.speed
# puts audi.speed

# class Car
# 	attr_accessor :speed, :model, :color, :wheels
# 	# можем не только устанавливать, но и получать данные/переменные
# 	def initialize(speed, model, color)
# 		@speed = speed
# 		@model = model
# 		@color = color
# 	end

# 	def is_speed_car?
# 		if @speed > 200
# 			return true
# 		end
# 		return false
# 	end
# end

# bmw = Car.new(199, "BMW", "Black")
# audi = Car.new(250, "audi", "White")

# puts bmw.is_speed_car?()
# puts audi.is_speed_car?()

# class Transport
# 	attr_accessor :color, :wheels

# 	def sayBipBip
# 		puts "Bip Bip"
# 	end
# end

# class Car < Transport
# 	attr_accessor :is_mechanic
# 	def saySome
# 		puts @color
# 	end
# end

# class Moto < Transport
# 	def sayBipBip
# 		puts "Bip Bip 2"
# 	end
# end

# bmw = Car.new()
# audi = Car.new()
# yamaha = Moto.new()
# bmw.color = "Black"
# audi.color = "Red"

# puts bmw.color
# puts audi.saySome
# puts audi.sayBipBip
# puts yamaha.sayBipBip

require_relative "tools.rb"
include Tools

Tools.sayHello("Fara")
Tools.sayBye("Ana")