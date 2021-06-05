from tkinter import *

#this funtion writes four lines of data to a file.
#define the file function.
def file():
    
#open a file named how to play.txt.    
    infile = open('Steps.txt' , 'w')
    
#wrie the steps to the file.
    infile.write("Step 1:Click on Start Button.\n")
    infile.write("Step 2:Select any option you want to play.\n")
    infile.write("Step 3:Write correct answer in Label.\n")
    infile.write("Step 4:Then press Submit Button.\n")
    infile.write("Now you are ready.Click on arrow and start the game.\n")
    infile.write("Best of luck!\n")

#close the file.    
    infile.close()

#call the file function.    
file()

#define main function.
def main():    
    def back():
        my_window.destroy()
        import index
        index.start_main_page()

    def all_steps():
        try:
            #open the file.
            infile=open('Steps.txt', 'r')

            #read the file contents.
            contents= infile.read()

            #close the file.
            infile.close()

            #create a Label widget.
            lab1=Label(
                my_window,
                text=contents,
                bg='#20B2AA',
                borderwidth=8,
                font=("Calibri", 15 )
            )
            lab1.pack(pady=(50, 0))
            
        except IOError:
            error= "File not found"

            #create a Label widget.
            lab2=Label(
                my_window,
                text=error,
                 bg='#20B2AA',
                width=18,
                borderwidth=8,
                font=("Calibri", 19)
            )
            lab2.pack(pady=(50, 0))

        
#open window
    my_window = Tk()
    my_window.geometry("500x500")
    my_window.resizable(0, 0)
    my_window.title("Find the Word!")
    my_window.configure(background="#20B2AA")

#inser image.    
    img1 = PhotoImage(file="back.png")

#create the Button widget.
    lab_img1 = Button(
        my_window,
        image=img1,
        bg=("#20B2AA"),
        border=0,
        justify='center',
        command=back,         #function call
    )
    
    lab_img1.pack(anchor='nw', pady=10, padx=10)

#create Label widget with text Instructions.
    lab = Label(
        text="Instructions",
        pady=10,
        bg='#20B2AA',
        fg="#000000",
        font=("Times New Roman", 30)
    )
    lab.pack(anchor="n")

#create Button widget with the text Follow these steps.
    steps = Button(
        text="Follow these steps",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#f08080",
        font=("", 13),
        command=all_steps,   #function called
    )
    steps.pack(pady=(20, 10))
    
#enter the main loop.
    my_window.mainloop()

    
