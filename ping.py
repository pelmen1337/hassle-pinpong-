if by>=400:
        bxs=0
        bys=0
        bx=width/2
        by=height/2
    bx+=bxs
    by+=bys
    if bx<=0:
        bxs=-bxs
    if by<=0:
        bys=-bys
    if bx>=600:
        bxs=-bxs
    if by>=375 and bx>=x:
        bys=-bys
