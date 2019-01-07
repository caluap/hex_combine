def gera(ar):
    
    newDrawing()
    size(97,112)
    
    
    s = ['_','_','_','_','_','_']
    l = ['a','b','c','d','e','f']
    
    # loads base hexagon
    image("hexagon.pdf", (0,0))
    
    # places ticks
    for i in range(len(ar)):
        if ar[i]:
            s[i] = l[i]
            tick_fn = l[i] + '.pdf'
            image(tick_fn, (0,0))
    filename = 'combined/' + ''.join(s) + '.pdf'
    saveImage(filename)


def main():
    for a in True, False:
        for b in True, False:
            for c in True, False:
                for d in True, False:
                    for e in True, False:
                        for f in True, False:
                            gera([a,b,c,d,e,f])


main()                        