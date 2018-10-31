x = 10
class animal(object):
	"""docstring for animal"""
	def __init__(self, sound,name,age,fav_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.fav_color = fav_color
	def	eat(self,food):
		print("yummy!!" + self.name + " is eating " + food)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " +self.fav_color)
	def make_sound(self,sound):
		print(self.sound *x)

dog = animal("woof ","duck","6","white")

dog.eat("chocolate")
dog.description()
dog.make_sound("woof")

class person(object):
	"""docstring for person"""
	def __init__(self,name,age,gender,city,fav_breakfast,fav_movie):
		self.name = name
		self.age = age
		self.gender = gender
		self.city = city
		self.fav_breakfast =fav_breakfast
		self.fav_movie = fav_movie
	def eat_fav_breakfast(self):
		print(self.name + " is eating " + self.fav_breakfast + "which is his favorite breakfast")
	def see_fav_movie(self):
		print("im watching " + self.fav_movie + "now, its my favorite movie")
o = person("ohad",15,"male","jerusalem","cereal ","star wars 5 ")		
o.eat_fav_breakfast()
o.see_fav_movie()

class song(object):
	"""docstring for song"""
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me-a_song():
		for i in range[4]:	
			print(lyrics[y])
			

lyrcis_queen = ["another bites the dust","and another gone","and another gone","another bites the dust"]