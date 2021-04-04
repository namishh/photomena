from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
import numpy as np
from PIL import Image, ImageTk, ImageEnhance
import cv2 as cv
import PIL

root = Tk()
root.title("Photomena™")



menu = Menu(root)
root.configure(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=lambda:load())

edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu = edit_menu)
edit_menu.add_command(label="Save", command=lambda:save())
edit_menu.add_command(label="Reset", command=lambda:reset())


filter_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Filter", menu = filter_menu)
filter_menu.add_command(label="Grayscale", command=lambda:gray_scale())
filter_menu.add_command(label="Blur", command=lambda:blur())
filter_menu.add_command(label="HSV", command=lambda:hsv())
filter_menu.add_command(label="Edge Detection", command=lambda:edge())
filter_menu.add_command(label="Chalkboard", command=lambda:chalk())
filter_menu.add_command(label="Sketch", command=lambda:sketch())

photo_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Photo", menu = photo_menu)
photo_menu.add_command(label="Sharp", command=lambda:sharp())
photo_menu.add_command(label="Bright 1", command=lambda:bright_1())
photo_menu.add_command(label="Bright 2", command=lambda:bright_2())
photo_menu.add_command(label="Bright Normal", command=lambda:bright_n())
photo_menu.add_command(label="Rotate", command=lambda:flip())






img = ''



def load():
    try:
            
        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ('Image File', '.png'), ('Image File', '.jpeg'), ('Image File', '.tif')])
        global img, image
        img = Image.open(path).convert('RGB')
        image = ImageTk.PhotoImage(img)
        my_label.configure(image=image)
    except Exception as e:
        pass


def gray_scale():
    global image, img
    try:
            
        image = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)
        image = ImageTk.PhotoImage(image=Image.fromarray(image))
        my_label.configure(image=image)
    except Exception as e:
        pass


def edge():
    global image, img
    try:

        image = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)
        image = cv.Canny(image, 250, 200)
        image = ImageTk.PhotoImage(image=Image.fromarray(image))
        my_label.configure(image=image)
    except Exception as e:
        pass


def hsv():
    global image, img
    try:
            
        image = cv.cvtColor(np.array(img), cv.COLOR_BGR2HSV)
        # img = ImageTk.PhotoImage(image=Image.fromarray(image))
        image = ImageTk.PhotoImage(image=Image.fromarray(image))
        my_label.configure(image=image)
    except Exception as e:
        pass

def reset():
    global image, img
    image = img
    image = ImageTk.PhotoImage(img)
    my_label.configure(image=image)



def blur():
    global image, img
    try:
            
        image = cv.blur(np.array(img), (5,5))
        image = ImageTk.PhotoImage(image=Image.fromarray(image)) 
        my_label.configure(image=image)
    except Exception as e:
        pass

def chalk():
    global image, img
    image = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)
    image = cv.Laplacian(image, cv.CV_64F)
    image = np.uint8(np.absolute(image))
    image = ImageTk.PhotoImage(image=Image.fromarray(image))
    my_label.configure(image=image)

def sketch():
    global image, img
    try:
            
        gray = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (3,3), 0)
        edge = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 5)
        image = cv.bitwise_and(np.array(img), np.array(img), mask=edge)
        image = ImageTk.PhotoImage(image=Image.fromarray(image))
        my_label.configure(image=image)
    except Exception as e:
        pass


def sharp():
    global image, img
    image = img
    print(image)
    enhancer = ImageEnhance.Sharpness(image)
    print(enhancer)
    image = enhancer.enhance(3)
    print(image)
    image = ImageTk.PhotoImage(image=image)
    my_label.configure(image=image)

def bright_1():
    global image, img
    image = img
    print(image)
    enhancer = ImageEnhance.Brightness(image)
    print(enhancer)
    image = enhancer.enhance(1.5)
    print(image)
    image = ImageTk.PhotoImage(image=image)
    my_label.configure(image=image)

def bright_2():
    global image, img
    image = img
    print(image)
    enhancer = ImageEnhance.Brightness(image)
    print(enhancer)
    image = enhancer.enhance(2)
    print(image)
    image = ImageTk.PhotoImage(image=image)
    my_label.configure(image=image)

def bright_n():
    global image, img
    image = img
    print(image)
    enhancer = ImageEnhance.Brightness(image)
    print(enhancer)
    image = enhancer.enhance(1.3)
    print(image)
    image = ImageTk.PhotoImage(image=image)
    my_label.configure(image=image)
    
def flip():
    global image, img
    image = img

  
    newWindow = Toplevel(root)
    horizontal = Scale(newWindow, from_=0, to=360, orient=HORIZONTAL)
    horizontal.pack()
    button2 = Button(newWindow, text='Rotate', command=lambda:get())
    button2.pack()
    def get():
        global image, img
        i = horizontal.get()
        image = image.rotate(i)
        image = ImageTk.PhotoImage(image=image)
        my_label.configure(image=image)
        newWindow.destroy()



def save():
    try:
        image._PhotoImage__photo.write("image.png")
    except Exception as e:
        pass


my_label = Label(root, image=img, text="Photomena™\nOpen Image First to start editing")
my_label.pack()


root.mainloop()
