from PIL import Image, ImageFilter
import sys

def main():
	imgname = ""
	try:
		imgname = sys.argv[1]
	except IndexError:
		raise ValueError("No input file name provided")

	im = Image.open(imgname)

	samples = build_samples(im, (185, 85), 20, 130)

	show_sample_regions(im, samples, (185, 85), 20, 130) 

def build_samples(im, tls, sbw, dtas):
	"""
	Builds and returns samples from image
	tls - the coordinates tuple of the top left samples
	sbw - the sampling box' width
	dtas - distance between two adjacent samples
	"""
	samples = [[None, None, None],
	           [None, None, None],
	           [None, None, None]]

	for y in range(3):
		for x in range(3):
			box = (tls[0] + dtas * x, tls[1] + dtas* y, tls[0] + dtas * x + sbw, tls[1] + dtas * y + sbw)

			samples[y][x] = im.crop(box)

	return samples

def show_sample_regions(im, samples, tls, sbw, dtas):
	"""
	Shows an image with the samples highlighted
	"""

	for y in range(3):
		for x in range(3):
			box = (tls[0] + dtas * x, tls[1] + dtas* y, tls[0] + dtas * x + sbw, tls[1] + dtas * y + sbw)

			samples[y][x] = samples[y][x].point(lambda i : i * 5)

			im.paste(samples[y][x], box)

	im.show()

if __name__ == '__main__':
	main()
