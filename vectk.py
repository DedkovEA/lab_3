from PIL import Image

im = Image.open('004.png')
pic = im.load()

Size = im.size

f = open('pixsvec.py', 'w')

f.write('import tkinter\nroot = tkinter.Tk()\ncanvas = tkinter.Canvas(root)\n')
f.write('canvas["width"] = ' + str(Size[0]) + '\ncanvas["height"] = ' + str(Size[1]) + '\n')
for i in range(Size[1]):
    x_start = 0
    for j in range(Size[0]):
        if pic[x_start, i] != pic[j, i]:
            f.write('canvas.create_line(' + str(x_start) + ',' + str(i) + ',' + str(j - 1) + ',' + str(
                i) + ',' + str() + 'fill = "' + ('#%02x%02x%02x' % (pic[x_start, i])) + '")\n')
            x_start = j
    f.write('canvas.create_line(' + str(x_start) + ',' + str(i) + ',' + str(j - 1) + ',' + str(
        i) + ',' + str() + 'fill = "' + ('#%02x%02x%02x' % (pic[x_start, i])) + '")\n')

f.write('canvas.pack()\ntkinter.mainloop()')
