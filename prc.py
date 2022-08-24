from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Paper Scissors")
root.configure(background='#9b59b6')

rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))

comp_rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
comp_paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
comp_scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))

user_label = Label(root, image=scissors_img)
comp_label = Label(root, image=comp_scissors_img)

comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

playerScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')
compScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')

compScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

player_indicator = Label(root, font=50, text='Player',
                         bg='#9b59b6', fg='white').grid(row=0, column=3)
comp_indicator = Label(root, font=50, text='Computer',
                       bg='#9b59b6', fg='white').grid(row=0, column=1)


msg = Label(root, font=50, bg='#9b59b6', fg='white',
            text='')
msg.grid(row=3, column=2)

choices = ['rock', 'paper', 'scissors']


def updateMessage(x):
    msg['text'] = x


def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)


def updateCompScore():
    score = int(compScore['text'])
    score += 1
    compScore['text'] = str(score)


# Check winner
def checkWin(player, comp):
    if player == comp:
        updateMessage("It's a tie")
    elif player == 'rock':
        if comp == 'paper':
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == 'paper':
        if comp == 'scissors':
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == 'scissors':
        if comp == 'rock':
            updateMessage('You loose')
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    else:
        pass


def updateChoice(x):
    # for computer
    comp_choice = choices[randint(0, 2)]
    if comp_choice == 'rock':
        comp_label.configure(image=comp_rock_img)
    elif comp_choice == 'paper':
        comp_label.configure(image=comp_paper_img)
    else:
        comp_label.configure(image=comp_scissors_img)

    # for user
    if x == 'rock':
        user_label.configure(image=rock_img)
    elif x == 'paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)

    checkWin(x, comp_choice)


rock = Button(root, width=20, height=2, text='Rock',
              bg='red', fg='white', command=lambda: updateChoice('rock')).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text='Paper',
               bg='blue', fg='white', command=lambda: updateChoice('paper')).grid(row=2, column=2)
scissors = Button(root, width=20, height=2, text='Scissors',
                  bg='green', fg='white', command=lambda: updateChoice('scissors')).grid(row=2, column=3)

root.mainloop()
