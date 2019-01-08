import random
from pprint import pprint

offset = 0
debug = False

def pos(ix, iy):
    adj_x = int((iy % 2) * Tile.tile_size[0]/2)
    adj_y = int(Tile.tile_size[1] * 0.75)

    # I subtract half a tile_size so they go till they bleed the page
    x = ix*Tile.tile_size[0]+adj_x - Tile.tile_size[0]//2
    y = iy*adj_y - Tile.tile_size[1]//2
    return x+offset, y+offset
    
class Tile:
    tile_size = 97, 112
    l = ['a','b','c','d','e','f']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos_x, self.pos_y = pos(x,y)
        self.is_set = False

        
    def set_tile(self, neighbours = [-1, -1, -1, -1, -1, -1]):
        # I can't set a tile that is already set
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
        
    def print_edge(self):
        image('tile.pdf', (self.pos_x, self.pos_y))
        
    def print_self(self, print_tile_edge = False, print_piece = True):
        rf = './combined/' + self.tile_name + '.pdf'
        if print_piece:
            image(rf, (self.pos_x, self.pos_y))
        if print_tile_edge:
            self.print_edge()

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
    
    # creates all tiles
    for i in range(len(indices)):
        ix, iy = indices[i]

        # it'll check the current tile's neighbours by row, bottom to top,
        # and by column, left to right, in an order different than the
        # clockwise one I established, so I need to convert it.
        order = [3, 2, 4, 1, 5, 0]
        # Also: I need to convert the current tile's edge I'm checking with
        # its neighbour corresponding edge
        intersection = ['a', 'f', 'b', 'e', 'c', 'd']
        
        # -1 --> There is no neighbour yet here
        #  0 --> There is a neighbour, but it's not sending a connection
        # +1 --> There is a neighbour and he's sending a connection
        neighbours = [0, 0, 0, 0, 0, 0]
        
        # accounts for the fact that odd rows are further
        # to the right than even rows
        if iy % 2 == 0:
            d_x = 0
        else: 
            d_x = 1

        i_n = 0
        
        for aux_y in [iy-1, iy, iy+1]:
            
            # there are 3 rows and 2 columns to check, but the offset differs in the
            # middle row, where I'm not checking adjacent tiles
            if aux_y == iy:
                min_x = ix - 1
                max_x = ix + 1
            else:
                min_x = ix - 1 + d_x
                max_x = ix + d_x
                
            for aux_x in [min_x, max_x]:
                if aux_x >= 0 and aux_x < w and aux_y >= 0 and aux_y < h:
                    # does this tile exist?
                    if tiles[aux_y][aux_x].is_set:

                        h_c = tiles[aux_y][aux_x].has_conn(intersection[i_n])
                        neighbours[order[i_n]] = tiles[aux_y][aux_x].has_conn(intersection[i_n])
                    else:
                        neighbours[order[i_n]] = -1
                else:
                    # this edge is off the screen, so we can chose randomly whether 
                    # or not to create a connection
                    neighbours[order[i_n]] = -1
                    
                if debug:
                    print(f'{i} / {ix},{iy} / {aux_x},{aux_y} / resultado : {neighbours[order[i_n]]}')
                i_n += 1
        
        tiles[iy][ix].set_tile(neighbours)
        tiles[iy][ix].print_self(debug)

        if debug:
            txt = FormattedString(align='center')
            s = f'{i}/{aux_x}/{aux_y}\n{neighbours}'
            txt.append(s, font="Helvetica", fontSize=10, fill=(1,0,0))
            tx, ty = pos(ix, iy)
            # rect(tx, ty, Tile.tile_size[0], Tile.tile_size[1])
            textBox(txt, (tx, ty+20, Tile.tile_size[0], 40))

        

    
main()