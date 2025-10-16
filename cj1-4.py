class Animal:

	def __init__(self, aleng, lleng, eyenum, tail, fur):
		self.arm_length = aleng
		self.leg_length = lleng
		self.number_of_eyes = eyenum
		self.has_tail = tail
		self.is_furry = fur

	def print(self):
		print("Here is my favorite animal")
		print(f"Its arms are {self.arm_length} feet long")
		print(f"Its legs are {self.leg_length} feet long")
		print(f"It has {self.number_of_eyes} eyes")
		print(f"Does it have a tail? {self.has_tail}")
		print(f"Is it furry? {self.is_furry}")

def main():

	Orca = Animal(6, 0, 2, "True", "False")

	Orca.print()

if __name__=="__main__":
	main()
