
size('A3')

tile_size = imageSize('tile.pdf')

w = round(width()/tile_size[0])
h = round(height()/(tile_size[1]*0.75))

print(f'{w,h}')


for iy in range(h):
    adj_x = int((iy % 2) * tile_size[0]/2)
    adj_y = int(tile_size[1] * 0.75)
    for ix in range(w):
        x = ix*tile_size[0]+adj_x
        y = iy*adj_y
        image('tile.pdf', (x, y))
        # print(f'{x},{y}')