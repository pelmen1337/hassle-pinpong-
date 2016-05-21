x=100
y=100
bx=100
by=100
bxs=0
bys=0
def setup():
    size(600,400)
def draw():
    global x,bx,by,bxs,bys,y
    fill(230,128,0)
    rect(0,0,600,400) #pole
    fill(160,17,203)
    rect(y,0,100,10) #verhniya racketa
    ellipse(bx,by,10,10)
    rect(x,380,100,10) #nijnia raketka
    if keyPressed:
        if key=="a": #nijnia vlevo
            x=x-5
        if key=="d": #nijnia v pravo
            x=x+5
        if key=="p": #restart
            bxs=-2
            bys=2
        if key=="j": #verhniavlevo
            y=y-5
        if key=="l": #verhnia v pravo
            y=y+5
    if by>=400 or by<=0: #game over
        bxs=0
        bys=0
        bx=width/2
        by=height/2
    bx+=bxs
    by+=bys  #skorost ball
    if bx<=0: #livaia stenka
        bxs=-bxs
    if bx>=600:
        bxs=-bxs
    if by>=375 and bx>=x and bx<=x+100 and by<=385: #nijnia raketka
        bys=-bys
