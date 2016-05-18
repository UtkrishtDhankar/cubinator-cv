from PIL import Image, ImageFilter
import sys

# the location of the top left sample
top_left_sample = (100, 100)

# box width of the sample for the cube
sample_box_width = 20

distance_to_adjacent_sample = 100

imgname = ""
try:
	imgname = sys.argv[1]
except IndexError:
	raise ValueError("No input file name provided")


im = Image.open(imgname)
samples = [[None, None, None],
           [None, None, None],
           [None, None, None]]

for y in range(3):
	for x in range(3):
		box = (top_left_sample[0] + distance_to_adjacent_sample * x, top_left_sample[1] + distance_to_adjacent_sample* y, top_left_sample[0] + distance_to_adjacent_sample * x + sample_box_width, top_left_sample[1] + distance_to_adjacent_sample * y + sample_box_width)

		samples[y][x] = im.crop(box)

		samples[y][x] = samples[y][x].point(lambda i : i * 5)

		im.paste(samples[y][x], box)

im.show()
