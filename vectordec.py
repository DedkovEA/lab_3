from PIL import Image

im = Image.open('004.png')
pic = im.load()

Size = im.size

f = open('pixsvec.py', 'w')

f.write('import graph\ngraph.windowSize(' + str(Size[0]) + ',' + str(
    Size[1]) + ')\n')
f.write('graph.canvasSize(' + str(Size[0]) + ',' + str(Size[1]) + ')\n')
for i in range(Size[1]):
    x_start = 0
    for j in range(Size[0]):
        if pic[x_start, i] != pic[j, i]:
            f.write('graph.penColor(' + str(pic[x_start, j]) + ')\n')
            f.write('graph.line(' + str(x_start) + ',' + str(i) + ',' + str(
                j - 1) + ',' + str(i) + ')\n')
            x_start = j
    f.write('graph.penColor(' + str(pic[x_start, j]) + ')\n')
    f.write('graph.line(' + str(x_start) + ',' + str(i) + ',' + str(
        Size[0]) + ',' + str(i) + ')\n')

f.write('graph.run()')
