def helloWorld(name):
	print("Hello, %s" %name)
#	print(f"Hello", {name})
helloWorld("Luke Skywalker")


def secondfunction():
	name = "Luke Skywalker"
	return helloWorld(name)



def printnegative(index, length):
	if index == "" and length =="":
		return

	while index < length:
		if index  % 2 == 1:
			print(index)
		index += 1

printnegative(0, 10)
