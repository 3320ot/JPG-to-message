def converter():
    from PIL import Image
    def Universal():
        line = int(input('Enter count of numbers in the line >>>> ')) #Numbers in line
        if (line%2)==0:
            lineY = int(line/2)
        else:
            ost=line%2
            lineY = int((line/2)-ost)
        image = str(input('Enter location of the picture >>>')) #File location
        picture = Image.open(image)
        size = (line, lineY)
        grayscale = picture.convert('L')
        picture = grayscale
        picture = picture.resize(size)
        def color(cordinate):
            col = (picture.getpixel(cordinate))
            return col

        a = ''
        for i in range (16384):
            a = a + 'o'
        b = (list(a))
        xc=0
        i=0
        yc = 0
        while i != line*lineY:
            i = i + 1
            colors = color((xc,yc))
            if colors <= 10:
                b[i]  = '8'
            elif colors >= 11 and colors <= 50:
                b[i]  = '4'
            elif colors >= 51 and colors <= 70:
                b[i]  = '5'
            elif colors >= 101 and colors <= 130:
                b[i]  = '3'
            elif colors >= 131 and colors <= 150:
                b[i]  = '9'
            elif colors >= 151 and colors <= 200:
                b[i]  = '3'
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
        for i in range (line):
            decor = decor + '='
        print('Screen: '+(str(line))+'x'+str(lineY))
        print(decor)
        print(b)
        print(decor)
    def TikTok():
        line = 10 #Numbers in line
        image = str(input('Enter location of the picture >>>')) #File location
        picture = Image.open(image)
        size = (line, line)
        picture = picture.resize(size)
        def color(cordinate):
            col = (picture.getpixel(cordinate))
            return col
        def RGB(cord_x, cord_y):
            r,g,b,al = color((cord_x, cord_y)) #4 arguments in png
            ocr = 255/9
            r = round(r/ocr)
            g = round(g/ocr)
            b = round(b/ocr)
            if r > g and r > b and r >= 8 and b == g:
                return(':heart:')
            elif g > r and g > b and g >= 8 and r == b:
                return(':green_heart:')
            elif b > r and b > g and b >= 8 and r == g:
                return(':blue_heart:')
            elif r == g and r > b:
                return(':yellow_heart:')
            elif r == b and r > g:
                return(':purple_heart:')
            elif r > g and g > b and g == 2:
                return('🤎')
            elif r > g and g > b:
                return('🧡')
            elif r == g == b and r <= 5:
                return('🖤')
            elif r == g == b and r >= 6:
                return('🤍')
            else:
                return('🤍')
        def X(iy):
            ix = 0
            firline = RGB(ix, iy)
            for ix in range(9):
                ix += 1
                firline += RGB(ix, iy)
            print(firline)
        result = 0
        X(result)
        for result in range(9):
            result+=1
            X(result)

            
    print('Select mode:')
    print('To use universall mode print "1"')
    print('To TikTok comment mode print "2"')
    mode = input('Choose >>> ')
    
    if str(mode)== '1':
        Universal()
    elif str(mode)== '2':
        TikTok()
    else:
        print('Error')
