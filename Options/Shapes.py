from tkinter import *
from random import *
from tkinter import messagebox
import time

#make a list of jumbled words.
SHAPES_WORD = ['CCLIER', 'IDANDOM', 'RHATE', 'AOTNOCG', 'USQRAE', 'TARS', 'RITLANEG', ]

#make a list of correct words.
SHAPES_ANSWER = ['CIRCLE', 'DIAMOND', 'HEART', 'OCTAGON', 'SQUARE', 'STAR', 'TRIANGLE', ]

ran_num = randrange(0, (len(SHAPES_WORD)))
jumbled_rand_word = SHAPES_WORD[ran_num]

points = 0     #initialise point

#define function.
def main():

    #this function takes user back to main window. 
    def back():
        my_window.destroy()
        import index
        index.start_main_page()

#this function change the word randomly.
    def change():
        global ran_num
        ran_num = randrange(0, (len(SHAPES_WORD)))
        word.configure(text=SHAPES_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

#this function check answer and give score.
    def check():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == SHAPES_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(SHAPES_WORD)))
            word.configure(text=SHAPES_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

#this function give hint to user if score is equal or greater than 5.
    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=SHAPES_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

#open window
    my_window = Tk()
    my_window.geometry("500x500")
    my_window.resizable(0, 0)
    my_window.title("Find the Word!")
    my_window.configure(background="#20B2AA")
    img1 = PhotoImage(file="back.png")

#create the Button widget.
    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#20B2AA',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

#create Label for Score.
    score = Label(
        text="Score:- 0",
        pady=10,
        bg="#20B2AA",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

#create Label widget.
    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#20B2AA",
        fg="#000000",
        font="Titillium  50 bold"
    )
    word.pack()

#create Entry widget.
    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

#create a Button widget.The text Submit should appear on the face of the Button.
    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#f08080",
        command=check,
    )
    submit.pack(pady=(10, 20))

#create a Button widget.The text Change the word should appear on the face of the Button.
    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#f08080",
        font=("", 13),
        command=change,
    )
    change.pack()

#create a Button widget.The text Answer should appear on the face of the Button.
    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#f08080",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

#create Label widget.
    ans_lab = Label(
        text="",
        bg="#20B2AA",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

#enter the main loop.
    my_window.mainloop()
