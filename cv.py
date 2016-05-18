from PIL import Image
import sys

imgname = ""
try:
	imgname = sys.argv[1]
except IndexError:
	raise ValueError("No input file name provided")


im = Image.open(imgname)
im.show()
