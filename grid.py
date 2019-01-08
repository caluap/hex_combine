import random
from pprint import pprint

class Tile:
    tile_size = 97, 112
    l = ['a','b','c','d','e','f']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos_x, self.pos_y = self.pos(x,y)
        self.is_set = False
                
    def pos(self, ix, iy):
        adj_x = int((iy % 2) * Tile.tile_size[0]/2)
        adj_y = int(Tile.tile_size[1] * 0.75)
    
        # I subtract half a tile_size so they go till they bleed the page
        x = ix*Tile.tile_size[0]+adj_x - Tile.tile_size[0]//2
        y = iy*adj_y - Tile.tile_size[1]//2
        return x, y
        
    def set_tile(self, neighbours = [-1, -1, -1, -1, -1, -1]):
        if not self.is_set:
            p = []
            for i in range(len(neighbours)):
                if neighbours[i] == -1:
                    # there is no neighbour, so we can decide randomly
                    p.append(random.choice(['_', Tile.l[i]]))
                elif neighbours[i] == 0: 
                    # neighbour sends no connection
                    p.append('_')
                else:
                    # neighbour sends connection
                    p.append(Tile.l[i])
            self.tile_name =  ''.join(p)
            self.is_set = True
            
    def has_conn(self, which):
        i = Tile.l.index(which)
        if self.tile_name[i] == '_':
            # no connection
            return 0
        else:
            # yes connection
            return 1
        
    def print_tile(self):
        image('tile.pdf', (self.pos_x, self.pos_y))
        
    def print_self(self, print_tile_border = False):
        rf = './combined/' + self.tile_name + '.pdf'
        image(rf, (self.pos_x, self.pos_y))
        if print_tile_border:
            self.print_tile()

def main():
    size('A2')

    w = round(width()/Tile.tile_size[0]) + 1
    h = round(height()/(Tile.tile_size[1]*0.75)) + 1

    print(f'{w,h}')
    
    tiles = []
    
    indices = []
    for iy in range(h):
        tiles.append([])
        for ix in range(w):
            tiles[iy].append(Tile(ix,iy))
            indices.append((ix, iy))

    random.shuffle(indices)
    

    for i in range(len(indices)//5):
        ix, iy = indices[i]

        # d, c, e, b, f, a
        # 3, 2, 4, 1, 5, 0
        order = [3, 2, 4, 1, 5, 0]
        intersection = ['a', 'f', 'b', 'e', 'c', 'd']
        neighbours = [0, 0, 0, 0, 0, 0]
        
        if iy % 2 == 0:
            d_x = 0
        else: 
            d_x = 1

        i_n = 0
        
        for aux_y in range(iy-1, iy+2):
            if aux_y == iy:
                min_x = ix - 1
                max_x = ix + 1
            else:
                min_x = ix - 1 - d_x
                max_x = ix - d_x
                
            for aux_x in [min_x, max_x]:
                if aux_x >= 0 and aux_x < w and aux_y >= 0 and aux_y < h:
                    if tiles[aux_y][aux_x].is_set:
                        neighbours[order[i_n]] = tiles[aux_y][aux_x].has_conn(intersection[i_n])
                    else:
                        neighbours[order[i_n]] = -1
                else:
                    # border of the screen, so we can be random
                    neighbours[order[i_n]] = -1
                i_n += 1
        
        tiles[iy][ix].set_tile(neighbours)
        tiles[iy][ix].print_self(False)
    
main()