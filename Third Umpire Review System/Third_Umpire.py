import tkinter 
import cv2 # pip install opencv-python
import PIL.Image, PIL.ImageTk # pip install pillow
from functools import partial
import threading
import time
import imutils # pip install imutils

stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag
    

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("decision_pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    
    # 2. Wait for 2 second
    time.sleep(2)

    # 3. Display out/notout image
    if decision == 'out':
        decisionImg = "out.jpg"
    else:
        decisionImg = "not_out.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

# Width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

# Tkinter gui starts here
window = tkinter.Tk()
window.title("Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
# canvas.grid()
canvas.pack()


# Buttons to control playback
btn = tkinter.Button(window, text="Give Out", width=25, height=2, bg='#206a5d', command=out)
# btn.grid(row=3,column=0, sticky='w')
btn.pack(side=tkinter.LEFT)

btn = tkinter.Button(window, text="<< Previous (fast)", width=25, height=2, bg='#A877BA', command=partial(play, -25))
# btn.grid(row=1,column=0, sticky='w')
btn.pack(side=(tkinter.LEFT))

btn = tkinter.Button(window, text="<< Previous (slow)", width=25, height=2, bg='#cdb30c', command=partial(play, -2))
# btn.grid(row=1,column=1, sticky='w')
btn.pack(side=tkinter.LEFT)

btn = tkinter.Button(window, text="Next (slow) >>", width=25, height=2, bg='#cdb30c', command=partial(play, 2))
# btn.grid(row=2,column=0, sticky='w')
btn.pack(side=tkinter.LEFT)

btn = tkinter.Button(window, text="Next (fast) >>", width=25, height=2, bg='#A877BA', command=partial(play, 25))
# btn.grid(row=2,column=1, sticky='w')
btn.pack(side=tkinter.LEFT)



btn = tkinter.Button(window, text="Give Not Out", width=25, height=2, bg='#206a5d', command=not_out)
# btn.grid(row=3,column=1, columnspan=1)
btn.pack(side=tkinter.LEFT)
window.mainloop()