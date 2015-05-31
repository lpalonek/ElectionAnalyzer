__author__ = 'lpalonek'
from PIL import Image
from os import listdir

print(listdir(".."))
images = []

for file in listdir(".."):
	if ("png") in file:
		images.append(file)


print(images)
for image in images:
	im = Image.open("../"+image)
	new = im.crop([2256,364,5122,3242])
	new.save(image)