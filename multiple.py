# This script will take an image file, and create a new identical image with a
# predetermined resolution. This will not overwrite the initial image.

from PIL import Image

images = ['testimg600x75.jpg', 'testimg600x50.jpg', 'testimg600x100.jpg',
		  'testimg801x253.jpg']


def multiple(files):
	for f in files:
		baseheight = 25
		img = Image.open(f)
		print(f'Original image: {img.size[0]}x{img.size[1]}')
		hpercent = (baseheight / float(img.size[1]))
		wsize = int((float(img.size[0]) * float(hpercent)))
		img = img.resize((wsize, baseheight), Image.ANTIALIAS)
		size = img.size

		if size[0] <= 200:
			print(
				f'Formatted image (height - 25): {img.size[0]}x'
				f'{img.size[1]}\nFile name: m-resized_{size[0]}x'
				f'{size[1]}.jpg\n')
			img.save(f'm-resized_{size[0]}x{size[1]}.jpg')
		else:
			basewidth = 200
			img = Image.open(f)
			wpercent = (basewidth / float(img.size[0]))
			hsize = int((float(img.size[1]) * float(wpercent)))
			img = img.resize((basewidth, hsize), Image.ANTIALIAS)
			size = img.size
			print(
				f'Formatted image (width - 200): {img.size[0]}x'
				f'{img.size[1]}\nFile name: m-resized_{size[0]}x'
				f'{size[1]}.jpg\n')
			img.save(f'm-resized_{size[0]}x{size[1]}.jpg')


multiple(images)
