
# Extract colours from image.jpg

import colorgram

colours_rgb = []

colours = colorgram.extract('image.jpg', 30)

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    rgb = (r, g, b)
    colours_rgb.append(rgb)

print(colours_rgb)
