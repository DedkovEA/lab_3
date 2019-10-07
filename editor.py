import tkinter as tk

from tkinter import filedialog
from PIL import Image, ImageTk


def change_size(*args):
    global dial
    dial = tk.Toplevel(root)
    global size_X
    global size_Y
    size_X = tk.StringVar()
    size_Y = tk.StringVar()
    text_X = tk.Entry(dial, textvariable=size_X, width=4)
    text_Y = tk.Entry(dial, textvariable=size_Y, width=4)
    ok_button = tk.Button(dial, text='Ok', command=close_changing_size)
    text_X.grid(row=0, column=1)
    text_Y.grid(row=1, column=1)
    tk.Label(dial, text='X Size').grid(row=0, column=0)
    tk.Label(dial, text='Y Size').grid(row=1, column=0)
    ok_button.grid(row=2, column=0, columnspan=2)
    dial.bind('<Return>', close_changing_size)
    text_X.focus()


def close_changing_size(*args):
    dial.destroy()
    canvas['height'] = int(size_Y.get())
    canvas['width'] = int(size_X.get())


def exec_brush_color_dial(*args):
    dial = tk.Toplevel()

    red = tk.StringVar()
    green = tk.StringVar()
    blue = tk.StringVar()

    entry_red = tk.Entry(dial, textvariable=red)
    entry_green = tk.Entry(dial, textvariable=green)
    entry_blue = tk.Entry(dial, textvariable=blue)

    ok_button = tk.Button(dial, text='Ok', command=lambda: close_brush_color_dial(red, green, blue, dial))

    tk.Label(dial, text='red').grid(row=0, column=0)
    tk.Label(dial, text='green').grid(row=1, column=0)
    tk.Label(dial, text='blue').grid(row=2, column=0)

    entry_red.grid(row=0, column=1)
    entry_green.grid(row=1, column=1)
    entry_blue.grid(row=2, column=1)

    ok_button.grid(row=3, column=0, columnspan=2)

    dial.bind('<Return>', lambda e: close_brush_color_dial(red, green, blue, dial))
    entry_red.focus()


def close_brush_color_dial(r, g, b, dial):
    global brush_color
    brush_color = '#%02x%02x%02x' % (int(r.get()), int(g.get()), int(b.get()))
    dial.destroy()


def exec_pen_color_dial(*args):
    dial = tk.Toplevel()

    red = tk.StringVar()
    green = tk.StringVar()
    blue = tk.StringVar()

    entry_red = tk.Entry(dial, textvariable=red)
    entry_green = tk.Entry(dial, textvariable=green)
    entry_blue = tk.Entry(dial, textvariable=blue)

    ok_button = tk.Button(dial, text='Ok', command=lambda: close_pen_color_dial(red, green, blue, dial))

    tk.Label(dial, text='red').grid(row=0, column=0)
    tk.Label(dial, text='green').grid(row=1, column=0)
    tk.Label(dial, text='blue').grid(row=2, column=0)

    entry_red.grid(row=0, column=1)
    entry_green.grid(row=1, column=1)
    entry_blue.grid(row=2, column=1)

    ok_button.grid(row=3, column=0, columnspan=2)

    dial.bind('<Return>', lambda e: close_pen_color_dial(red, green, blue, dial))
    entry_red.focus()


def close_pen_color_dial(r, g, b, dial):
    global pen_color
    pen_color = '#%02x%02x%02x' % (int(r.get()), int(g.get()), int(b.get()))
    dial.destroy()


def exec_pen_width_dial(*args):
    dial = tk.Toplevel()

    tk.Label(dial, text='Width').grid(row=0, column=0)

    width = tk.StringVar()
    entry_width = tk.Entry(dial, textvariable=width)

    ok_button = tk.Button(dial, text='Ok', command=lambda: close_pen_width_dial(dial, int(width.get())))

    entry_width.grid(row=0, column=1)

    ok_button.grid(row=1, column=0, columnspan=2)

    dial.bind('<Return>', lambda e: close_pen_width_dial(dial, int(width.get())))
    entry_width.focus()


def close_pen_width_dial(dial, width):
    global pen_width
    pen_width = width
    dial.destroy()


def exec_image_loading():
    image_file = filedialog.askopenfilename()
    global pil_image, image, background
    pil_image = Image.open(image_file)
    size = pil_image.size
    image = ImageTk.PhotoImage(pil_image)
    canvas.configure(width=size[0], height=size[1])
    background = canvas.create_image(0, 0, anchor="nw", image=image)


def line_press(*args):
    global tool
    tool = 'line'


def ellips_press(*args):
    global tool
    tool = 'ellips'


def rect_press(*args):
    global tool
    tool = 'rect'


def polygon_press(*args):
    global tool
    tool = 'polygon'


def draw_press(*args):
    global tool
    tool = 'draw'


def get_color_from_image(*args):
    global tool
    tool = 'get_color_from_image'


def on_mouse_motion(event):
    if (tool == 'line') and button_pressed:
        canvas.coords(current_object, first_x, first_y, event.x, event.y)
    elif (tool == 'rect') and button_pressed:
        canvas.coords(current_object, first_x, first_y, event.x, event.y)
    elif (tool == 'ellips') and button_pressed:
        canvas.coords(current_object, first_x, first_y, event.x, event.y)
    elif (tool == 'polygon') and button_pressed:
        canvas.coords(current_object, first_x, first_y, event.x, event.y)


def on_mouse_button1(event):
    global button_pressed, current_object, first_x, first_y, polygon_list, brush_color, pen_color, pen_width
    if (tool == 'line') and (not button_pressed):
        button_pressed = True
        canvas.dtag('last', 'last')
        first_x = event.x
        first_y = event.y
        current_object = canvas.create_line(first_x, first_y, first_x, first_y, tags=('last'))
    elif (tool == 'line') and button_pressed:
        canvas.coords(current_object, first_x, first_y, event.x, event.y)
        canvas.itemconfigure(current_object, fill=pen_color, width=pen_width)
        button_pressed = False
    elif (tool == 'rect') and (not button_pressed):
        button_pressed = True
        canvas.dtag('last', 'last')
        first_x = event.x
        first_y = event.y
        current_object = canvas.create_rectangle(first_x, first_y, first_x, first_y, tags=('last'))
    elif (tool == 'rect') and button_pressed:
        canvas.coords(current_object, first_x, first_y, event.x, event.y)
        canvas.itemconfigure(current_object, fill=brush_color, outline=pen_color, width=pen_width)
        button_pressed = False
    elif (tool == 'ellips') and (not button_pressed):
        button_pressed = True
        canvas.dtag('last', 'last')
        first_x = event.x
        first_y = event.y
        current_object = canvas.create_oval(first_x, first_y, first_x, first_y, tags=('last'))
    elif (tool == 'ellips') and button_pressed:
        canvas.coords(current_object, first_x, first_y, event.x, event.y)
        canvas.itemconfigure(current_object, fill=brush_color, outline=pen_color, width=pen_width)
        button_pressed = False
    elif (tool == 'polygon') and (not button_pressed):
        button_pressed = True
        canvas.dtag('last', 'last')
        first_x = event.x
        first_y = event.y
        polygon_list = [first_x, first_y]
        current_object = canvas.create_line(first_x, first_y, first_x, first_y, tags=('poly'))
    elif (tool == 'polygon') and button_pressed:
        first_x = event.x
        first_y = event.y
        polygon_list.append(first_x)
        polygon_list.append(first_y)
        current_object = canvas.create_line(first_x, first_y, first_x, first_y, tags=('poly'))
    elif (tool == 'draw') and (not button_pressed):
        canvas.dtag('last', 'last')
        first_x = event.x
        first_y = event.y
    elif tool == 'get_color_from_image':
        brush_color = '#%02x%02x%02x' % pil_image.load()[event.x, event.y]


def on_mouse_button2(event):
    global tool, polygon_list, button_pressed, brush_color, pen_color, pen_width
    if (tool == 'polygon') and button_pressed:
        polygon_list.append(event.x)
        polygon_list.append(event.y)
        canvas.create_polygon(polygon_list, fill=brush_color, outline=pen_color, width=pen_width, tags=('last'))
        canvas.delete('poly')
        button_pressed = False
    elif tool == 'get_color_from_image':
        pen_color = '#%02x%02x%02x' % pil_image.load()[event.x, event.y]


def on_drawing(event):
    if tool == 'draw':
        global first_x, first_y, pen_color, pen_width
        canvas.create_line(first_x, first_y, event.x, event.y, width=pen_width, fill=pen_color, tags=('last'))
        first_x, first_y = event.x, event.y


def undo(event):
    canvas.delete('last')


def store(event):
    canvas.tag_raise(background, 'last')


def image_save(*args):
    image_file = filedialog.asksaveasfilename()
    im_file = open(image_file, 'w')
    im_file.write('import tkinter as tk\nroot=tk.Tk()\ncanvas=tk.Canvas(root)\nroot.title("EDA-created image")\n')
    im_file.write(
        '#This file was created automaticly by EDA simple editor.\n#See '
        'https://github.com/DedkovEA/lab_3/blob/master/editor.py for source code.\n')
    im_file.write('canvas["width"] = ' + str(canvas['width']) + '\ncanvas["height"] = ' + str(canvas['height']) + '\n')

    for i in canvas.find_all():
        if canvas.type(i) == 'line':
            im_file.write('canvas.create_line(' + str(canvas.coords(i))[1:-1] + ',fill = "' + str(
                canvas.itemcget(i, 'fill')) + '",width=' + str(canvas.itemcget(i, 'width')) + ')\n')
        elif canvas.type(i) == 'rectangle':
            im_file.write('canvas.create_rectangle(' + str(canvas.coords(i))[1:-1] + ',fill = "' + str(
                canvas.itemcget(i, 'fill')) + '",width=' + str(canvas.itemcget(i, 'width')) + ',outline = "' + str(
                canvas.itemcget(i, 'outline')) + '")\n')
        elif canvas.type(i) == 'oval':
            im_file.write('canvas.create_oval(' + str(canvas.coords(i))[1:-1] + ',fill = "' + str(
                canvas.itemcget(i, 'fill')) + '",width=' + str(canvas.itemcget(i, 'width')) + ',outline = "' + str(
                canvas.itemcget(i, 'outline')) + '")\n')

        elif canvas.type(i) == 'polygon':
            im_file.write('canvas.create_polygon(' + str(canvas.coords(i))[1:-1] + ',fill = "' + str(
                canvas.itemcget(i, 'fill')) + '",width=' + str(canvas.itemcget(i, 'width')) + ',outline = "' + str(
                canvas.itemcget(i, 'outline')) + '")\n')

    im_file.write('canvas.grid(sticky="nwes")\nroot.mainloop()')


brush_color = '#ffffff'

pen_color = '#000000'
pen_width = 1

tool = 'nothing'

first_x = 0
first_y = 0

current_object = False

button_pressed = False

polygon_list = []

root = tk.Tk()
root.title('EDA simple editor')

instruments = tk.Frame(root)
canvas = tk.Canvas(root)

button_ellips = tk.Button(instruments, text='0', command=ellips_press)
button_line = tk.Button(instruments, text='-', command=line_press)
button_rect = tk.Button(instruments, text='4', command=rect_press)
button_draw = tk.Button(instruments, text='s', command=draw_press)
button_size = tk.Button(instruments, text='sz', command=change_size)
button_polygon = tk.Button(instruments, text='pg', command=polygon_press)
button_get_color_from_image = tk.Button(instruments, text='gc', command=get_color_from_image)
button_brush_color = tk.Button(instruments, text='bc', command=exec_brush_color_dial)
button_pen_color = tk.Button(instruments, text='pc', command=exec_pen_color_dial)
button_pen_width = tk.Button(instruments, text='pw', command=exec_pen_width_dial)
button_image_load = tk.Button(instruments, text='il', command=exec_image_loading)
button_image_save = tk.Button(instruments, text='is', command=image_save)

instruments.grid(row=0, column=0)
button_size.grid(row=0, column=0)
button_ellips.grid(row=0, column=1)
button_line.grid(row=0, column=2)
button_rect.grid(row=0, column=3)
button_polygon.grid(row=0, column=4)
button_draw.grid(row=0, column=5)
button_get_color_from_image.grid(row=0, column=6)
button_brush_color.grid(row=0, column=10, sticky='e')
button_pen_color.grid(row=0, column=11, sticky='e')
button_pen_width.grid(row=0, column=12, sticky='e')
button_image_load.grid(row=0, column=13, sticky='e')
button_image_save.grid(row=0, column=15)

canvas.grid(row=1, column=0)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
instruments.columnconfigure(1, weight=1)
instruments.columnconfigure(2, weight=1)
instruments.columnconfigure(3, weight=1)
instruments.columnconfigure(0, weight=1)

canvas.bind('<Motion>', on_mouse_motion)
canvas.bind('<Button-1>', on_mouse_button1)
canvas.bind('<Button-3>', on_mouse_button2)
canvas.bind('<B1-Motion>', on_drawing)
root.bind('<Control-KeyPress-z>', undo)
root.bind('<Control-KeyPress-i>', store)

root.mainloop()
