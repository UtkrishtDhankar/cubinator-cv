from PIL import Image, ImageFilter
import sys
import math

# Simple dict as a wrapper for colors
Colors = {
    "red" : (255, 0, 0),
    "blue" : (0, 0, 255),
    "orange" : (0, 0, 255),
    "yellow" : (0, 0, 255),
    "white" : (255, 255, 255),
    "green" : (0, 255, 0)
}

def main():
    imgname = ""
    try:
        imgname = sys.argv[1]
    except IndexError:
        raise ValueError("No input file name provided")

    im = Image.open(imgname)

    samples = build_samples(im, (185, 85), 20, 130)

    show_sample_regions(im, samples, (185, 85), 20, 130)

    sample_colors = {}
    for y in range(3):
        for x in range(3):
            sample_colors[(x, y)] = get_color(samples[y][x])
            print "(" + str(x) + ", " + str(y) + "):", sample_colors[(x, y)]


def get_distance(t1, t2):
    """
    Returns the distance between the two tuples t1 and t2
    """
    difference = (t1[0] - t2[0], t1[1] - t2[1], t1[2] - t2[2])
    distance_sqr = 0
    for d in difference:
        distance_sqr += difference * difference

    return math.sqrt(distance_sqr)

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
    new_im = im

    new_samples = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]

    for y in range(3):
        for x in range(3):
            box = (tls[0] + dtas * x, tls[1] + dtas* y, tls[0] + dtas * x + sbw, tls[1] + dtas * y + sbw)

            new_samples[y][x] = samples[y][x].point(lambda i : i * 5)

            new_im.paste(new_samples[y][x], box)

    im.show()

def get_color(im):
    colors = im.getcolors(1024)
    max_occurence, most_present = 0, 0
    for c in colors:
        if c[0] > max_occurence:
            (max_occurence, most_present) = c
    return most_present

if __name__ == '__main__':
    main()
