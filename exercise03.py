list = [1, 5, 6, 10, 2]
#perintah for
for x in list:
	print(x)

#perintah while
index = 0
while index < len(list):
	print(list[index])
	index += 1



genap = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Untuk bilangan genap")
for i in range (11):
	if i %2 == 1:
		continue
	print(i)

print("Untuk bilangan ganjil")

for i in range ( 11):
	if i %2 == 0:
		continue
	print(i)




