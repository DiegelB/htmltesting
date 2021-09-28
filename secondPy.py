
def bigHomie():
	print("HAY")
	listMan = []
	with open("test.txt", "r") as f:
		for text in f.readlines():
			listMan.append(text)
	return listMan
