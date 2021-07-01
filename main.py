# This script will take an image file, and create a new identical image with a
# predetermined resolution. This will not overwrite the initial image.

from PIL import Image

file = 'testimg600x50.jpg'

baseheight = 25
img = Image.open(file)
print(f'Original image: {img.size[0]}x{img.size[1]}')
hpercent = (baseheight / float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((wsize, baseheight), Image.ANTIALIAS)
size = img.size

if size[0] <= 200:
	print(f'Formatted image (height - 25): {img.size[0]}x{img.size[1]}')
	img.save(f'resized_{size[0]}x{size[1]}.jpg')
else:
	basewidth = 200
	img = Image.open(file)
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
	size = img.size
	print(f'Formatted image (width - 200): {img.size[0]}x{img.size[1]}')
	img.save(f'resized_{size[0]}x{size[1]}.jpg')
