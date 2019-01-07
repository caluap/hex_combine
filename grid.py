import random
from pprint import pprint
tile_size = imageSize('tile.pdf')


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.filename = randomFilename()
        self.pos_x, self.pos_y = pos(x,y)
        
    def print(self, print_tile_border = False):
        rf = './combined/' + self.filename + '.pdf'
        image(rf, (self.pos_x, self.pos_y))
        if print_tile_border:
            image('tile.pdf', (self.pos_x, self.pos_y))



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
    
    tiles = []

    for iy in range(h):
        tiles.append([])
        for ix in range(w):
            tiles[iy].append(Tile(ix,iy))
            tiles[iy][ix].print(True)
            
        
    
main()