string = input("Give me a string: ")
dupStr = set(" ".join(str(string)).split(' '))

for char in dupStr:
	print(f"{char} is {string.count(char)} times in string")

