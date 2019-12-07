from numpy import complex, array
from PIL import Image
import PIL.Image
import PIL.ImageTk
import tkinter 
import colorsys

#see if the complex number is in the set
def calcular(x,y):
    c = complex(x,y)
    z0 = 0
    for i in range(1, 2000):
        if abs(z0) > 2:
            return rgbconv(i)
        z0 = z0*z0*z0 + c
    return (0,0,0)

#giving colors to the points that are not in the set 
def rgbconv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 12.5)) 
    return tuple(color.astype(int))

#Creating the image where the fractal is going to show up
img = Image.new('RGB',(1024 , 768))    
pixeles = img.load()

#rendering the fractal
for x in range(img.size[0]):
     for y in range(img.size[1]):
         pixeles[x,y] = calcular( (x-1024/2)/200, 
									(y - 768/2)/200)

img.show()
#TRY
#scrn = tkinter.Tk()
#scrn.title("Mandelbrot set")
#scrn.geometry('1024x768')
#canvas = tkinter.Canvas(scrn, width = 1024, height=512)
#canvas.pack()
#render = PIL.ImageTk.PhotoImage(image = PIL.Image.frombuffer(img))
#canvas.create_image(0,0, image=img,anchor=tkinter.NW)
#crn.mainloop()
