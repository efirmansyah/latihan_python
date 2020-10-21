def bilangan_3(baris = None):
	if baris == None or baris < 3:
		return

	for bil in range(baris):
		if bil == 0:
			continue

		if bil % 3 == 0:
			print(bil)

bilangan_3(10)


def bilangan3(baris=None):
	if baris == None or baris < 3:
		return

	index = 1
	while index < baris:
		if index % 3 == 0:
			print(index)

		index += 1
bilangan3(50)






