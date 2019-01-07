tile_size = imageSize('tile.pdf')

def pos(ix,iy):
    adj_x = int((iy % 2) * tile_size[0]/2)
    adj_y = int(tile_size[1] * 0.75)
    x = ix*tile_size[0]+adj_x
    y = iy*adj_y
    return x, y

def main():
    size('A3')

    w = round(width()/tile_size[0])
    h = round(height()/(tile_size[1]*0.75))

    print(f'{w,h}')


    for iy in range(h):
        for ix in range(w):
            x,y = pos(ix,iy)
            image('tile.pdf', (x, y))
        
    
main()