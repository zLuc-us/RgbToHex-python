rgb = [57, 107, 77]  # cor rgb
hex = '#' + format((rgb[0] << 16) | (rgb[1] << 8) | rgb[2], '06x')
print(hex)  # return #396b4d
