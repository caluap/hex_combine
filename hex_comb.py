suffixes = ['0', '1', '2', '3', '4', '5', '6', '7']

def gera(ar, suffix = '0'):
    
    newDrawing()
    size(97,112)
    
    
    s = ['_','_','_','_','_','_']
    l = ['a','b','c','d','e','f']
    
    # loads base hexagon
    # image("parts/hexagon.pdf", (0,0))
    
    # places ticks
    for i in range(len(ar)):
        if ar[i]:
            s[i] = l[i]
            tick_fn = 'parts/' + suffix + l[i] + '.pdf'
            image(tick_fn, (0,0))
    filename = 'combined/' + suffix + ''.join(s) + '.pdf'
    saveImage(filename)


def main():
    for suffix in suffixes:
        for a in True, False:
            for b in True, False:
                for c in True, False:
                    for d in True, False:
                        for e in True, False:
                            for f in True, False:
                                gera([a,b,c,d,e,f], suffix)


main()                        