import Image
import random

def diff(colour1, colour2):
  return abs(colour1[0] - colour2[0]) + abs(colour1[1] - colour2[1]) + abs(colour1[2] - colour2[2])

def badness(image, colour, position):
	total = 0
	if (position[0] > 0):
		total += diff(image.getpixel((position[0] - 1, position[1])), colour)
	if (position[0] < 255):
		total += diff(image.getpixel((position[0] + 1, position[1])), colour)
	if (position[1] > 0):
		total += diff(image.getpixel((position[0], position[1] - 1)), colour)
	if (position[1] < 255):
		total += diff(image.getpixel((position[0], position[1] + 1)), colour)

	return total

def switch(image, pos1, pos2):
		temp = image.getpixel(pos1)
		image.putpixel(pos1, image.getpixel(pos2))
		image.putpixel(pos2, temp)

img = Image.new("RGB", (256,256))
for i in range(0,256):
    for j in range(0,256):
        img.putpixel((i,j),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))


for j in range(0,100):

	avgTotal = 0

	for i in range(0,100000):
		pos1 = (random.randint(0,255), random.randint(0,255))
		pos2 = (random.randint(0,255), random.randint(0,255))

		currentBadness = badness(img, img.getpixel(pos1), pos1) + badness(img, img.getpixel(pos2), pos2)
		newBadness = badness(img, img.getpixel(pos1), pos2) + badness(img, img.getpixel(pos2), pos1)

		avgTotal += currentBadness

		if (newBadness < currentBadness):
			switch(img, pos1, pos2)

	avgTotal /= 100000.0

	for i in range(0,25000):
		pos1 = (random.randint(1,255), random.randint(1,255))
		pos2 = (random.randint(1,255), random.randint(1,255))

		currentBadness = badness(img, img.getpixel(pos1), pos1)
		currentBadness += badness(img, img.getpixel((pos1[0] - 1, pos1[1])), 		 (pos1[0] - 1, pos1[1]))
		currentBadness += badness(img, img.getpixel((pos1[0] - 1, pos1[1] - 1)), (pos1[0] - 1, pos1[1] - 1))
		currentBadness += badness(img, img.getpixel((pos1[0], 		 pos1[1] - 1)), (pos1[0], 		pos1[1] - 1))

		currentBadness += badness(img, img.getpixel(pos2), pos2)
		currentBadness += badness(img, img.getpixel((pos2[0] - 1, pos2[1])), 		 (pos2[0] - 1, pos2[1]))
		currentBadness += badness(img, img.getpixel((pos2[0] - 1, pos2[1] - 1)), (pos2[0] - 1, pos2[1] - 1))
		currentBadness += badness(img, img.getpixel((pos2[0], 		 pos2[1] - 1)), (pos2[0], 		pos2[1] - 1))

		newBadness = badness(img, img.getpixel(pos1), pos2)
		newBadness += badness(img, img.getpixel((pos1[0] - 1, pos1[1])), 		 (pos2[0] - 1, pos2[1]))
		newBadness += badness(img, img.getpixel((pos1[0] - 1, pos1[1] - 1)), (pos2[0] - 1, pos2[1] - 1))
		newBadness += badness(img, img.getpixel((pos1[0], 		 pos1[1] - 1)), (pos2[0], 		pos2[1] - 1))

		newBadness += badness(img, img.getpixel(pos2), pos1)
		newBadness += badness(img, img.getpixel((pos2[0] - 1, pos2[1])), 		 (pos1[0] - 1, pos1[1]))
		newBadness += badness(img, img.getpixel((pos2[0] - 1, pos2[1] - 1)), (pos1[0] - 1, pos1[1] - 1))
		newBadness += badness(img, img.getpixel((pos2[0], 		 pos2[1] - 1)), (pos1[0], 		pos1[1] - 1))

		if (newBadness < currentBadness):
			switch(img, pos1, pos2)
			switch(img, (pos1[0] - 1, pos1[1]), (pos2[0] - 1, pos2[1]))
			switch(img, (pos1[0] - 1, pos1[1] - 1), (pos2[0] - 1, pos2[1] - 1))
			switch(img, (pos1[0], pos1[1] - 1), (pos2[0] - 1, pos2[1]))

	img.save("output" + str(j) + ".bmp")

#img.save("output.bmp")
