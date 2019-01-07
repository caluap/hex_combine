import random
from pprint import pprint

class Tile:
    tile_size = 97, 112
    l = ['a','b','c','d','e','f']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos_x, self.pos_y = self.pos(x,y)
        self.filename = self.choose_tile()
        
    def pos(self, ix, iy):
        adj_x = int((iy % 2) * Tile.tile_size[0]/2)
        adj_y = int(Tile.tile_size[1] * 0.75)
    
        # I subtract half a tile_size so they go till they bleed the page
        x = ix*Tile.tile_size[0]+adj_x - Tile.tile_size[0]//2
        y = iy*adj_y - Tile.tile_size[1]//2
        return x, y
        
    def choose_tile(self, neighbours = [False, False, False, False, False, False]):
        p = []
        for i in range(len(neighbours)):
            if not neighbours[i]:
                # pichs from _ or the corresponding letter
                p.append(random.choice(['_', Tile.l[i]]))
            else:
                p.append('_')
        return ''.join(p)
            
        
    def print_tile(self):
        image('tile.pdf', (self.pos_x, self.pos_y))
        
    def print_self(self, print_tile_border = False):
        rf = './combined/' + self.filename + '.pdf'
        image(rf, (self.pos_x, self.pos_y))
        if print_tile_border:
            self.print_tile()
    
    def find_neighbours(self):
        neighbours = [False, False, False, False, False, False]

        for i in range(6):
            if self.filename[i] == Tile.l[i]:
                neighbours[i] = True
        return neighbours

def main():
    size('A2')

    w = round(width()/Tile.tile_size[0]) + 1
    h = round(height()/(Tile.tile_size[1]*0.75)) + 1

    print(f'{w,h}')
    
    tiles = []
    

    for iy in range(h):
        tiles.append([])
        for ix in range(w):
            tiles[iy].append(Tile(ix,iy))
            tiles[iy][ix].print_self(True)
            
        
    
main()