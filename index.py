#This program displays Find the word! game.
#reference: https://www.sourcecodester.com/python/14481/guess-word-game-project-python.html

from tkinter import *

#define start_main_page function.
def start_main_page():
    
#the start_game function is a callback function for the Buttons widget.
    def start_game(args):                               
        main_window.destroy()                 
        if args == 1:                       
            from Options import Animals       #import Animals file from options folder.
            Animals.main()                    #call the main function.
        elif args == 2:
            from Options import Body_parts    #import Body_parts file from options folder.
            Body_parts.main()                 #call the main function.
        elif args == 3:
            from Options import Colour        #import Colour file from options folder.
            Colour.main()                     #call the main function.
        elif args == 4:
            from Options import Fruit         #import Fruit file from options folder.
            Fruit.main()                      #call the main function.
        elif args == 5:
            from Options import Shapes        #import Shapes file from options folder.
            Shapes.main()                     #call the main function.
        elif args == 6:
            from Options import Vegetable     #import Vegetable file from options folder.
            Vegetable.main()                  #call the main function.
        elif args == 7:
            from Options import Vehicles      #import Vehicles file from options folder.
            Vehicles.main()                   #call the main function.

#this function shows buttons to select level of your own choice.
#define option function.            
    def option():

#create a button widget.The text 'Select' should appear on the face of the button.        
        lab_img1 = Button(
            main_window,
            text="Select",
            bg='#00FF00',
            border=0,
            font=("Verdana", 12)

        )
#create a button widget.The text 'Animals' should appear on the face of the Button.
#the start_game function with argument(1) should be executed when the user clicks the
#Button.       
        sel_btn1 = Button(
            text="Animals",
            width=18,
            borderwidth=8,
            font=("Aharoni", 18),
            fg="#000000",
            bg="#f08080",
            cursor="hand2",       #mouse cursor
            command=lambda: start_game(1),    
        )
#create a button widget.The text 'Body parts' should appear on the face of the Button.
#the start_game function with argument(2) should be executed when the user clicks the
#Button.         
        sel_btn2 = Button(
            text="Body parts",
            width=18,
            borderwidth=8,
            font=("Aharoni", 18),
            fg="#000000",
            bg="#f08080",
            cursor="hand2",     #mouse cursor
            command=lambda: start_game(2),
        )
        
#create a button widget.The text 'Colour' should appear on the face of the Button.
#the start_game function with argument(3) should be executed when the user clicks the
#Button.        
        sel_btn3 = Button(
            text="Colour",
            width=18,
            borderwidth=8,
            font=("Aharoni", 18),
            fg="#000000",
            bg="#f08080",
            cursor="hand2",     #mouse cursor
            command=lambda: start_game(3),
        )
        
#create a button widget.The text 'Fruits' should appear on the face of the Button.  
#the start_game function with argument(4) should be executed when the user clicks the
#Button.
        sel_btn4 = Button(
            text="Fruits",
            width=18,
            borderwidth=8,
            font=("Aharoni", 18),
            fg="#000000",
            bg="#f08080",
            cursor="hand2",   #mouse cursor
            command=lambda: start_game(4),
        )

#create a button widget.The text 'Shapes' should appear on the face of the Button. 
#the start_game function with argument(5) should be executed when the user clicks the
#Button.
        sel_btn5 = Button(
            text="Shapes",
            width=18,
            borderwidth=8,
            font=("Aharoni", 18),
            fg="#000000",
            bg="#f08080",
            cursor="hand2",     #mouse cursor
            command=lambda: start_game(5),
        )
        
#create a button widget.The text 'Vegetable' should appear on the face of the Button. 
#the start_game function with argument(6) should be executed when the user clicks the
#Button.
        sel_btn6 = Button(
            text="Vegetable",
            width=18,
            borderwidth=8,
            font=("Aharoni", 18),
            fg="#000000",
            bg="#f08080",
            cursor="hand2",     #mouse cursor
            command=lambda: start_game(6),
        )

#create a button widget.The text 'Vehicles' should appear on the face of the Button. 
#the start_game function with argument(7) should be executed when the user clicks the
#Button.
        sel_btn7 = Button(
            text="Vehicles",
            width=18,
            borderwidth=8,
            font=("Aharoni", 18),
            fg="#000000",
            bg="#f08080",
            cursor="hand2",     #mouse cursor
            command=lambda: start_game(7),
        )

#organize widgets.        
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )


#define instruction function.                                                       
    def instruction():
         main_window.destroy()                                        
         from Options import Instructions     #import Instructions file from Options folder.
         Instructions.main()
        
           
#the show_option method is a callback function for the Start Button widget.        
    def show_option():
        start_btn.destroy()
        instruction_btn.destroy()
        lab_img.destroy()
        option()
       
#the show_instruction method is a callback function for the How to play Button widget.
    def show_instruction():
        instruction_btn.destroy()
        start_btn.destroy()
        instruction()

#open a main window.
    main_window = Tk()                                            
    
#window layout.
    main_window.geometry("500x500") 
    main_window.resizable(0, 0)
    main_window.title("Find the Word!")
    main_window.configure(background="#20B2AA") 
   
    
#inset image  
    img1 = PhotoImage(file="back.png")

#create label    
    lab_img = Label(
        main_window, 
        text="Find The Word Game!",
        bg='#20B2AA',
        font=("Times New Roman", 30)
    )
    lab_img.pack(pady=(50, 0))        
    
#create a button widget.The text 'Start' should appear on the face of the Button. 
#the show_option method should be executed when the user clicks the Button.
    start_btn = Button(
        main_window,text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#f08080",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))

#create a button widget.The text 'How to play' should appear on the face of the Button. 
#the show_instruction method should be executed when the user clicks the Button.
    instruction_btn = Button(
        main_window,text="How to play",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#f08080",
        font=("", 13),
        cursor="hand2",
        command=show_instruction,
    )
    instruction_btn .pack(pady=(50, 20))
    
#enter the main loop.
    main_window.mainloop()

#Call the stat_main_page function
start_main_page()
