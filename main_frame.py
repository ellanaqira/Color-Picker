from tkinter import Frame

class Main_frame:
    def __init__(self):

#colorpicker window frame
        self.frame_color = Frame(bg="#CFCFCF",
                                 relief='sunken',
                                 bd=4,
                                 padx=43,
                                 pady=220)
        self.frame_color.pack(pady=(5,5), padx=(5,0), side='left', anchor='n')


#FRAME TO COMBINE ALL TEST COLOR FRAME============================================
#combine all test color frame
        self.frame_combine_test = Frame(relief="sunken", bd=3)
        self.frame_combine_test.pack(side="right", anchor="ne", pady=(5,5), padx=(0,5), expand=True, fill="y")

#text box frame
        self.frame_textbox = Frame(self.frame_combine_test)
        self.frame_textbox.pack()

#frame for font color and background color
        self.frame_preview_input_row1 = Frame(self.frame_combine_test)
        self.frame_preview_input_row1.pack()

#frame for size font and font style
        self.frame_preview_input_row2 = Frame(self.frame_combine_test)
        self.frame_preview_input_row2.pack()

#frame for text preview
        self.frame_preview_input_row3 = Frame(self.frame_combine_test)
        self.frame_preview_input_row3.pack()

        
#FRAME TO COMBINE ALL OUTPUT FRAME============================================
        self.frame_combine_output = Frame()
        self.frame_combine_output.pack(padx=(5,5), pady=(0,0))

#title frame >> COMBINE_output FRAME
        self.frame_title = Frame(self.frame_combine_output,
                                 bg="#C5C5C5",
                                 relief='raised',
                                 bd=2,
                                 padx=80,
                                 pady=0)
        self.frame_title.pack(padx=(0,0), pady=(5,0))

#output color value frame >> COMBINE_output FRAME
        self.frame_output = Frame(self.frame_combine_output)
        self.frame_output.pack(padx=(0,5), pady=(0,0))

#color view title >> COMBINE_output FRAME
        self.frame_title_view = Frame(self.frame_combine_output)
        self.frame_title_view.pack(padx=(0,0), pady=(0,0))

#color view frame >> COMBINE_output FRAME
        self.frame_view = Frame(self.frame_combine_output)
        self.frame_view.pack(padx=(0,0), pady=(0,0))