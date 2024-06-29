#Just importing functions
import os
from tkinter import Tk, PhotoImage, Button, Label
from tkinter import messagebox
import random

#Starting out the tkinter stuff
rps = Tk()
rps.geometry("1000x925")
rps["background"]="#B9B2DC"
rps.title("Rock Paper Scissors")

#Dictionary of values for Computer
c_value = {
    0:"rock",
    1:"paper",
    2:"scissors"}

#________________Importing images and Declaring Values________________
rock_img = PhotoImage(file=f"{os.getcwd()}/pics/Rock.png")
paper_img = PhotoImage(file=f"{os.getcwd()}/pics/Paper.png")
#DONE____add in the next line later
scissors_img = PhotoImage(file=f"{os.getcwd()}/pics/Scissors.png")
rock_txt = PhotoImage(file=f"{os.getcwd()}/pics/Rock_text.png")
paper_txt = PhotoImage(file=f"{os.getcwd()}/pics/Paper_text.png")
scissors_txt = PhotoImage(file=f"{os.getcwd()}/pics/Scissors_text.png")
play_again = PhotoImage(file=f"{os.getcwd()}/pics/Play_Again_text.png")

Win = "AYOOOOOOOOOOOO You Won!!! :("
Draw = "Draw???? Well That was anticlimatic :|"
Lose = "HAHAHAHAHAHAHAHA LOSER!!!! :)"


player_score = 0
pc_score = 0
#______Cancelled______
#playagain = PhotoImage(file="Play_Again_text.png")

#______Cancelled______
#________________Disabling buttons after match________________
'''def disable():
    rock_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")
    pc_score = 0
    player_score = 0'''
    
##________________Declaring win/lose conditions________________
#had to place this individually in each condition as it doesnt change when u play again if its outisde
# c_choice = c_value[random.randint(0,2)]

def p_rock():
    global pc_score, player_score
    c_choice = c_value[random.randint(0,2)]
    
    if c_choice == "rock":
        pc_choice.config(image=rock_img)
        result = Draw
        
    elif c_choice == "paper":
        pc_choice.config(image=paper_img)
        result = Lose
        pc_score += 1
    else:
        pc_choice.config(image=scissors_img)
        result = Win
        player_score += 1
        
    result_box.config(text=result)
    your_choice.config(image=rock_img)
    player_score_box.config(text=f"Player Score: {player_score}")
    pc_score_box.config(text=f"Computer Score: {pc_score}")
#disable()
        
def p_paper():
    global pc_score, player_score
    c_choice = c_value[random.randint(0,2)]
    
    if c_choice == "rock":
        result = Win
        player_score += 1
        pc_choice.config(image=rock_img)
    elif c_choice == "paper":
        pc_choice.config(image=paper_img)
        result = Draw
    else:
        pc_choice.config(image=scissors_img)
        result = Lose
        pc_score += 1
    
    result_box.config(text=result) 
    your_choice.config(image=paper_img)
    player_score_box.config(text=f"Player Score: {player_score}")
    pc_score_box.config(text=f"Computer Score: {pc_score}")  
#disable()
        
def p_scissors():
    global pc_score, player_score
    c_choice = c_value[random.randint(0,2)]
    
    if c_choice == "rock":
        pc_choice.config(image=rock_img)
        result = Lose
        pc_score += 1
    elif c_choice == "paper":
        pc_choice.config(image=paper_img)
        result = Win
        player_score += 1
    else:
        pc_choice.config(image=scissors_img)
        result = Draw
        
    result_box.config(text=result)
    your_choice.config(image=scissors_img)
    player_score_box.config(text=f"Player Score: {player_score}")
    pc_score_box.config(text=f"Computer Score: {pc_score}")
#disable()
        
#Replay button
def reset():
    global pc_score, player_score
    rock_btn.config(state="active")
    paper_btn.config(state="active")
    scissors_btn.config(state="active")
    result_box.config(text="")
    pc_choice.config(image="")
    your_choice.config(image="")
    pc_score = 0
    player_score = 0
    player_score_box.config(text=f"Player Score: {player_score}")
    pc_score_box.config(text=f"Computer Score: {pc_score}")
    
##Trying out stuff
#Just edit out this def function later
def itworks():
    msg = messagebox.showinfo('Yoooo', 'It Works!!!!')
    
# def end_game():
#     global pc_score, player_score
#     if pc_score>player_score:
#         end = messagebox.showinfo("You Lost :(")

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
#
play_again_btn = Button(rps, image=play_again, command=reset, borderwidth=0, highlightthickness=0)
play_again_btn.place(x=300, y=800)

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

#Score boxes
player_score_box = Label(text="Player Score",font=("Helvatica bold", 20), bg="#B9B2DC")
player_score_box.place(x=125, y=325)
pc_score_box = Label(text="Computer Score", font=("Helvatica bold", 20), bg="#B9B2DC")
pc_score_box.place(x=725, y=325)

#______________________CANCELLED______________________
#Play again button
#Add image for this shit
'''play_again = Button(image=playagain, command=reset, borderwidth=0, highlightthickness=0)
play_again.place(x=300, y=750)


#Found a better way to display scores
#use cget and work with that somehow
player_score = 0
pc_score = 0
def scores():
    if res == Win:
        player_score = player_score + 1
        
    elif res == Lose:
        pc_score = pc_score + 1
'''
##OUTLINE
#______DONE______Computer option written on the top along with the pic of the chosen option.
#______DONE______A "vs" screen in middle with Your and Computer option pics displayed
#(Maybe try animation delay before the upper one)
#______DONE______The win/lose message under that
#______DONE______Get and display scores
#______Cancelled______Reset button under that
#(Restared wrt scores) Reset button under that

rps.mainloop()
