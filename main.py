import random
#B1DDC6
BACKGROUND_COLOR= "#B1DDC6"

from tkinter import *
import pandas as pd
try:
   data=pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original=pd.read_csv("data/french_words.csv")
    value=original.to_dict(orient="records")

else:
   value=data.to_dict(orient="records")
current_card={}
def nextcard():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(value)
    french=current_card["French"]
    english=current_card["English"]
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=french,fill="black")
    canvas.itemconfig(background,image=front_photo)
    flip_timer=window.after(3000,func=flipcard)

def flipcard():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=current_card["English"])
    canvas.itemconfig(background,image=card_back)

def is_know():
    value.remove(current_card)
    data=pd.DataFrame(value)
    data.to_csv("data/word_to_learn.csv",index=False)
    nextcard()




window=Tk()
window.title("flashy")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flipcard)
canvas=Canvas(height=526,width=800,highlightthickness=0)


card_back=PhotoImage(file="images/card_back.png")
card_back1=canvas.create_image(400,263,image=card_back)

front_photo=PhotoImage(file="images/card_front.png")
background=canvas.create_image(400,263,image=front_photo)

canvas.config(bg=BACKGROUND_COLOR)
title=canvas.create_text(450, 200, text="" ,font=("Ariel",40,"italic"))
word=canvas.create_text(450, 260, text="",font=("Ariel",60,"normal"))
canvas.grid(row=0,column=0,columnspan=2)
right=PhotoImage(file="images/right.png")
write=Button(image=right, width=100,height=100,highlightthickness=0,bg=BACKGROUND_COLOR,command=is_know)
write.grid(row=1,column=1)
wrong=PhotoImage(file="images/wrong.png")
wrong_b=Button(image=wrong,width=100,height=100,highlightthickness=0,bg=BACKGROUND_COLOR,command=nextcard)
wrong_b.grid(row=1,column=0)
nextcard()


window.mainloop()