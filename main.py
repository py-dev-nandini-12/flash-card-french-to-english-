BACKGROUND_COLOR = "#B1DDC6"

# ---------------------SETTING FLASH CARDS-----------------------------------#
from tkinter import *
import pandas
import random


current_word ={}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
# print(data)
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn =original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    # print(to_learn)


def next_card():
    global current_word,flip_timer
    gui.after_cancel(flip_timer)
    current_word =random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French",fill ="black")
    canvas.itemconfig(card_word, text =current_word["French"],fill="black")
    canvas.itemconfig(canvas_img,image =image1_front)
    flip_timer = gui.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill ="white")
    canvas.itemconfig(card_word, text=current_word["English"],fill= "white" )
    canvas.itemconfig(canvas_img, image=image_new_back)


def is_known():
    to_learn.remove(current_word)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)


#---------------------------------------SETTING GUI-----------------------#
gui = Tk()
gui.title("Flashy")
gui.config(padx=50, pady=50, bg=BACKGROUND_COLOR )

flip_timer= gui.after(3000,func= flip_card)

canvas = Canvas(width = 800,height =526)
image1_front = PhotoImage(file ="images/card_front.png")
image_new_back = PhotoImage(file= "images/card_back.png")
canvas_img =canvas.create_image(400, 263, image=image1_front)



card_title =canvas.create_text(400,150,text= "Title" ,fill ="black", font =("Ariel" ,40,"italic"))
card_word =canvas.create_text(400,263,text= "Word" ,fill="black", font =("Ariel" ,60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row= 0,column=0,columnspan=2)



image3_right = PhotoImage(file ="images/right.png")
button1 =Button(image=image3_right,highlightthickness=0,command =is_known)
button1.grid(row =1,column=0)

image4_wrong = PhotoImage(file ="images/wrong.png")
button2 =Button(image =image4_wrong,highlightthickness=0,command =next_card)
button2.grid(row=1,column=1)

next_card()

gui.mainloop()
