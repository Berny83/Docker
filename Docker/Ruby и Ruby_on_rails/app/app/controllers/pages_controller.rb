class PagesController < ApplicationController
	def about
		@heading = "Страничка про нас!"
		@text = 'Some text...'
	end
end
