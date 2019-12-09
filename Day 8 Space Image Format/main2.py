'''
https://adventofcode.com/2019/day/8
What message is produced after decoding your image?
'''

from PIL import Image
with open(file='day08/input.txt', mode='r') as file:

    layers = []

    while code := file.read(150):
        layers.append(code)
    
    image = []

    l = len(layers)
    for i in range(150):
        image.append( int(layers[0][i]) )

    for i in range(1,100,1):
        for pix in range(150):
            if layers[i][pix] == '0' and image[pix] == 2:
                image[pix] = 0
            elif layers[i][pix] == '1' and image[pix] == 2:
                image[pix] = 1
    rgb = []
    for i in range(150):
        if image[i] == 2:
            rgb.append((255,255,0))
        elif image[i] == 1:
            rgb.append((255,255,255))
        elif image[i] == 0:
            rgb.append((0,0,0))

    img = Image.new('RGB', (25,6))
    img.putdata(rgb)
    img.save('image.png')