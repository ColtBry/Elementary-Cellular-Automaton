from PIL import Image
from math import floor

def create_automaton(rule_list, steps):

    def get_rule(image, x, y):
        bin_str = ''
        for shift in range(-1, 2): # Reads the 3 cells above the cell
            if 0 < x+shift < image.width:
                bin_str += str(1-int(image.getpixel((x+shift,y-1))/255))
            else:
                bin_str += '0'

        return bin_str

    if isinstance(rule_list, int): # Converts int to binary list
        if 0 > rule_list > 255:
            raise Exception('Int must be 0-255')
        binary = bin(rule_list)[2:].zfill(8)
        rule_list = list(map(int, binary))
    else:
        if len(rule_list) != 8:
            raise Exception('List must have a length of 8')

    rules = {}

    for rule in enumerate(rule_list): # Build rule list
        rules[bin(7-rule[0])[2:].zfill(3)] = rule[1]

    im = Image.new('L', (steps*2+1, steps+1), 'white')

    im.putpixel((floor(im.width/2), 0), 0)

    for y in range(1, im.height): # Walks the image
        for x in range(im.width):
            rule = get_rule(im, x, y)

            pixel = (1-rules[rule])*255 # Invert bit and convert to B/W 
            im.putpixel((x,y), pixel)

    return im
