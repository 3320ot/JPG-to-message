def converter():
    from PIL import Image

    line = int(input('Enter count of numbers in the line >>>> ')) #Numbers in line
    image = str(input('Enter location of the picture >>>')) #File location
    picture = Image.open(image) 
    size = (line, 16)
    grayscale = picture.convert('L')
    picture = grayscale
    picture = picture.resize(size)
    def color(cordinate):
        col = (picture.getpixel(cordinate))
        return col

    a = 'o'
    for i in range (line):
        a = a + 'o'
    a = a *16
    b = (list(a))

    xc=0
    i=0
    yc = 0
    while i != line*16:
        i = i + 1
        colors = color((xc,yc))
        if colors <= 10:
            b[i]  = '8'
        elif colors >= 11 and colors <= 50:
            b[i]  = '4'
        elif colors >= 51 and colors <= 70:
            b[i]  = '3'
        elif colors >= 101 and colors <= 130:
            b[i]  = '3'
        elif colors >= 131 and colors <= 150:
            b[i]  = '9'
        elif colors >= 151 and colors <= 200:
            b[i]  = '2'
        elif colors >= 71 and colors <= 100:
            b[i]  = '2'
        elif colors >= 201 and colors <= 255:
            b[i]  = '1'
        xc = xc + 1
        if xc == line:
            xc = 0
            yc = yc + 1
    
    b=str(''.join(b))
    b = b.replace('o', '')
    decor='='
    decorl='+'
    for i in range (line):
        decor = decor + '='
        decorl = decorl + '+'
    print('Screen: '+(str(line))+'x16')
    print(decor, b, decor)

