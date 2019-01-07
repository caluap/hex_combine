import random
tile_size = imageSize('tile.pdf')

def randomFilename():
    s = ['_','_','_','_','_','_']
    l = ['a','b','c','d','e','f']
    for i in range(6):
        if random.choice([True, False]):
            s[i] = l[i]
    return ''.join(s)

def pos(ix,iy):
    adj_x = int((iy % 2) * tile_size[0]/2)
    adj_y = int(tile_size[1] * 0.75)
    
    # I subtract half a tile_size so they go till they bleed the page
    x = ix*tile_size[0]+adj_x - tile_size[0]//2
    y = iy*adj_y - tile_size[1]//2
    return x, y

def main():
    size('A2')

    w = round(width()/tile_size[0]) + 1
    h = round(height()/(tile_size[1]*0.75)) + 1

    print(f'{w,h}')


    for iy in range(h):
        for ix in range(w):
            x,y = pos(ix,iy)

            rf = './combined/' + randomFilename() + '.pdf'
            image(rf, (x,y))
            
            image('tile.pdf', (x, y))
            
        
    
main()