#Just importing functions
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

#Starting out the tkinter stuff
rps = Tk()
rps.geometry("1000x800")
rps["background"]="#B9B2DC"
rps.title("Rock Paper Scissors")

#Dictionary of values for Computer
c_value = {
    0:"rock",
    1:"paper",
    2:"scissors"
}

#________________Importing images________________
rock_img = PhotoImage(file="Rock.png")
paper_img = PhotoImage(file="Paper.png")
#DONE____add in the next line later
scissors_img = PhotoImage(file="Scissors.png")
rock_txt = PhotoImage(file="Rock_text.png")
paper_txt = PhotoImage(file="Paper_text.png")
scissors_txt = PhotoImage(file="Scissors_text.png")
#______Cancelled______
#playagain = PhotoImage(file="Play_Again_text.png")

#______Cancelled______
'''#________________Disabling buttons after match________________
def disable():
    rock_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")'''
    
##________________Declaring win/lose conditions________________
#had to place this individually in each condition as it doesnt change when u hit lay againif its outisde
# c_choice = c_value[random.randint(0,2)]

def p_rock():
    c_choice = c_value[random.randint(0,2)]
    
    if c_choice == "rock":
        pc_choice.config(image=rock_img)
        result = "Draw???? Well That was anticlimatic :|"
        
    elif c_choice == "paper":
        pc_choice.config(image=paper_img)
        result = "HAHAHAHAHAHAHHAHA LOSER!!!! :)"
    else:
        pc_choice.config(image=scissors_img)
        result = "AYOOOOOOOOOOOO You Won!!! :("
        
    result_box.config(text=result)
    your_choice.config(image=rock_img)
#disable()
        
def p_paper():
    c_choice = c_value[random.randint(0,2)]
    
    if c_choice == "rock":
        result = "AYOOOOOOOOOOOO You Won!!! :("
        pc_choice.config(image=rock_img)
    elif c_choice == "paper":
        pc_choice.config(image=paper_img)
        result = "Draw???? Well That was anticlimatic :|"
    else:
        pc_choice.config(image=scissors_img)
        result = "HAHAHAHAHAAHHAHA LOSER!!!! :)"
    
    result_box.config(text=result) 
    your_choice.config(image=paper_img)  
#disable()
        
def p_scissors():
    c_choice = c_value[random.randint(0,2)]
    
    if c_choice == "rock":
        pc_choice.config(image=rock_img)
        result = "HAHAHAHAHAHAHAHA LOSER!!!! :)"
    elif c_choice == "paper":
        pc_choice.config(image=paper_img)
        result = "AYOOOOOOOOOOOO You Won!!! :("
    else:
        pc_choice.config(image=scissors_img)
        result = "Draw???? Well That was anticlimatic :|"
        
    result_box.config(text=result)
    your_choice.config(image=scissors_img)
#disable()
        
#Replay button
def reset():
    rock_btn.config(state="active")
    paper_btn.config(state="active")
    scissors_btn.config(state="active")
    result_box.config(text="")
    pc_choice.config(image="")
    your_choice.config(image="")
##Trying out stuff
#Just edit out this def function later
'''def itworks():
    msg = messagebox.showinfo('Yoooo', 'It Works!!!!')'''

##________________CREATING BUTTONS/LABELS________________
#Player buttons
rock_btn = Button(rps, image=rock_img, command=p_rock, borderwidth=0, highlightthickness=0)
rock_btn.place(x=100,y=450)
rock_text = Button(rps, image=rock_txt, command=p_rock, borderwidth=0, highlightthickness=0)
rock_text.place(x=100, y=675)
#
paper_btn = Button(rps, image=paper_img, command=p_paper, borderwidth=0, highlightthickness=0)
paper_btn.place(x=400, y=450)
paper_text = Button(rps, image=paper_txt, command=p_paper, borderwidth=0, highlightthickness=0)
paper_text.place(x=400, y=675)
#
scissors_btn = Button(rps, image=scissors_img, command=p_scissors, borderwidth=0, highlightthickness=0)
scissors_btn.place(x=700,y=450)
scissors_text = Button(rps, image=scissors_txt, command=p_scissors, borderwidth=0, highlightthickness=0)
scissors_text.place(x=700, y=675)

#Choices Made
pc_text = Label(text="Computer's Choice", font=("Helvatica bold", 25), bg="#B9B2DC")
pc_text.place(x=700, y=20)
pc_choice = Label(borderwidth=0, highlightthickness=0, bg="#B9B2DC")
pc_choice.place(x=700, y=100)

vs_text = Label(text="V.S", font=("Helvatica bold", 50), bg="#B9B2DC")
vs_text.place(x=475, y=150)

you_text = Label(text="Your Choice", font=("Helvatica bold", 25), bg="#B9B2DC")
you_text.place(x=125, y=20)
your_choice = Label(borderwidth=0, highlightthickness=0, bg="#B9B2DC")
your_choice.place(x=100, y=100)

#Win/Lose Text box
result_box = Label(font=("Helvatica bold", 50), bg="#B9B2DC")
result_box.place(x=100, y=350)
#______Cancelled______
#Play again button
#Add image for this shit
'''play_again = Button(image=playagain, command=reset, borderwidth=0, highlightthickness=0)
play_again.place(x=300, y=750)'''

#________________DISPLAYING SCORES________________
#use cget and work with that somehow


##OUTLINE
#______DONE______Computer option written on the top along with the pic of the chosen option.
#______DONE______A "vs" screen in middle with Your and Computer option pics displayed
#(Maybe try animation delay before the upper one)
#______DONE______The win/lose message under that
#Get and display scores
#______Cancelled______Reset button under that

rps.mainloop()