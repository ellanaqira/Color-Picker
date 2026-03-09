from tkinter import *
from tkinter import messagebox as mb
from customtkinter import *
from CTkColorPicker import *
from main_frame import Main_frame
from aset import Aset
from colorsys import *
import colorsys as cls
import pyperclip as pc

class Main_element:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_frame = Main_frame()
        self.aset = Aset()

        self.bar_size = 15

# Color picker logo
    def title_image(self):
        logo_img = Label(self.main_frame.frame_title,
                          image=self.aset.icon_img,
                          bg="#C5C5C5")
        logo_img.grid(row=0, column=0)

# Command to open color chooser window
    def open_color(self):
        self.pick_color = AskColor()
        self.hex_value = self.pick_color.get()

        try:
            # Running function to print out the color value to entry bar
            self.hex_output()
            self.rgb_output()
            self.cmyk_output()
            self.hsl_output()
            self.hsv_ouput()
            self.change_color1()

        except AttributeError:
            # Print out the output when you close color chooser window before choose a color
            print("no color choosen")

# Button to open color chooser window
    def color_button(self):
        self.color_btn = CTkButton(self.main_frame.frame_color,
                                   text="Choose a Color",
                                   # Function to open color chooser window
                                   command=self.open_color)
        self.color_btn.grid(row=0, column=0)

# Instruction label to tell user to put color chooser window in available frame, for a neat appearance only
    def insruction(self):
        label_instruction = Label(self.main_frame.frame_color,
                                  text="""
_________( Quick Instructions )_________
* For a neat appearance, you can put
   the Choose Color window here.
* The color you select from here will
   appear in Color Box 1.
* The color you enter into the Color
   Input bar will appear in Color Box 2.""",
                                  justify='left',
                                  bg='#CFCFCF')
        label_instruction.grid(row=1, column=0)

#output manu class
    class output_menu:
        def __init__(self, frame, text, copy_icon, config):
            self.frame = frame
            self.text = text
            self.copy_icon = copy_icon
            
            self.row_title = config.get('row title', 0)
            self.column_title = config.get('column title', 0)
            self.row_output_bar = config.get('row output bar', 0)
            self.column_btn = config.get('column button', 0)
            self.bar_size = config.get('bar size', 0)
    
        def output_title(self):
            self.title =  Label(self.frame,
                        text=self.text)
            self.title.grid(row=self.row_title, column=self.column_title, pady=(9,0), padx=(0,0))

        def output_bar(self):
            self.outputbar = Entry(self.frame,
                            bg="#e8e8e8",
                            width=self.bar_size)
            self.outputbar.grid(row=self.row_output_bar, column=self.column_title, padx=(0,0), pady=(0,0))

        def copy_command(self):
          value = self.outputbar.get()
          pc.copy(value)

        def copy_button(self):
          copy_btn = Button(self.frame,
                            image=self.copy_icon,
                            command=self.copy_command)
          copy_btn.grid(row=self.row_output_bar, column=self.column_btn, padx=(0,10))

        def write_output(self,message):
            self.outputbar.insert(END,f"{message}")

#hex menu
    def hex(self):
        self.config = {'row title' : 0,
                       'column title' : 0,
                       'row output bar' : 1,
                       'column button' : 1,
                       'bar size' : self.bar_size}
        self.hex_menu = self.output_menu(self.main_frame.frame_output, 'HEX', self.aset.copy_icon, self.config)
        self.hex_menu.output_title()
        self.hex_menu.output_bar()
        self.hex_menu.copy_button()
        self.hex_menu.outputbar.insert(0,"#000000")

#print hex value to output bar
    def hex_output(self):
        if self.hex_value == None:
                return None
        else:
            self.hex_menu.outputbar.delete(0, END)
            self.hex_menu.write_output(self.hex_value)

            print(f'\n{self.hex_value}')

#RGB menu
    def rgb(self):
        self.config = {'row title' : 0,
                       'column title' : 2,
                       'row output bar' : 1,
                       'column button' : 3,
                       'bar size' : self.bar_size}
        self.rgb_menu = self.output_menu(self.main_frame.frame_output, 'RGB', self.aset.copy_icon, self.config)
        self.rgb_menu.output_title()
        self.rgb_menu.output_bar()
        self.rgb_menu.copy_button()
        self.rgb_menu.outputbar.insert(0, "0, 0, 0")

#print RGB value to output bar
    def rgb_output(self):
        value = self.hex_value.lstrip('#')
        rgb_val = len(value)
        self.rgb_value = tuple(int(value[i:i + rgb_val // 3], 16) for i in range(0, rgb_val, rgb_val // 3))

        self.rgb_str_value = str(self.rgb_value).replace('(','').replace(')','')
        self.rgb_int_value = int(''.join(map(str, self.rgb_value)))

        print(self.rgb_str_value)
    
        self.rgb_menu.outputbar.delete(0, END)
        self.rgb_menu.write_output(self.rgb_str_value)

#CMYK menu
    def cmyk(self):
        self.config = {'row title' : 2,
                    'column title' : 0,
                    'row output bar' : 3,
                    'column button' : 1,
                    'bar size' : self.bar_size}
        self.cmyk_menu = self.output_menu(self.main_frame.frame_output, 'CMYK', self.aset.copy_icon, self.config)
        self.cmyk_menu.output_title()
        self.cmyk_menu.output_bar()
        self.cmyk_menu.copy_button()
        self.cmyk_menu.outputbar.insert(0, "0%, 0%, 0%, 100%")

#print CMYK value to output bar
    def cmyk_output(self):
        def rgb_to_cmyk(r, g, b):
            RGB_SCALE = 255
            CMYK_SCALE = 100
            
            if (r, g, b) == (0, 0, 0):
                # black
                return 0, 0, 0, CMYK_SCALE

            # rgb [0,255] -> cmy [0,1]
            c = 1 - int(r) / RGB_SCALE
            m = 1 - int(g) / RGB_SCALE
            y = 1 - int(b) / RGB_SCALE

            # extract out k [0, 1]
            min_cmy = min(c, m, y)
            c = (c - min_cmy) / (1 - min_cmy)
            m = (m - min_cmy) / (1 - min_cmy)
            y = (y - min_cmy) / (1 - min_cmy)
            k = min_cmy

            c_value = (int(round(c,2)*100))
            
            m_value = (int(round(m,2)*100))

            y_value = (int(round(y,2)*100))

            k_value = (int(round(k,2)*100))
            
            cmyk_value = (f'{c_value}%, {m_value}%, {y_value}%, {k_value}%')
            print(cmyk_value)

            self.cmyk_menu.outputbar.delete(0, END)
            self.cmyk_menu.write_output(cmyk_value)

        rgb_to_cmyk(self.rgb_value[0], self.rgb_value[1], self.rgb_value[2])

#HSL menu
    def hsl(self):
        self.config = {'row title' : 2,
                    'column title' : 2,
                    'row output bar' : 3,
                    'column button' : 3,
                    'bar size' : self.bar_size}
        self.hsl_menu = self.output_menu(self.main_frame.frame_output, 'HSL', self.aset.copy_icon, self.config)
        self.hsl_menu.output_title()
        self.hsl_menu.output_bar()
        self.hsl_menu.copy_button()
        self.hsl_menu.outputbar.insert(0, "0, 0%, 0%")

    def hsl_output(self):

        r, g, b = self.rgb_value[0] / 255.0, self.rgb_value[1] / 255.0, self.rgb_value[2] / 255.0
        h, l, s = cls.rgb_to_hls(r, g, b)

        h_value = round(h*360)
        s_value = round(s*100)
        l_value = round(l*100)
        hsl_value = (f"{h_value}, {s_value}%, {l_value}%")
        print (hsl_value)

        self.hsl_menu.outputbar.delete(0, END)
        self.hsl_menu.write_output(hsl_value)

#HSV menu
    def hsv(self):
        self.config = {'row title' : 4,
                    'column title' : 0,
                    'row output bar' : 5,
                    'column button' : 1,
                    'bar size' : self.bar_size}
        self.hsv_menu = self.output_menu(self.main_frame.frame_output, 'HSV', self.aset.copy_icon, self.config)
        self.hsv_menu.output_title()
        self.hsv_menu.output_bar()
        self.hsv_menu.copy_button()
        self.hsv_menu.outputbar.insert(0, "0°, 100%, 0%")

    def hsv_ouput(self):
        r, g, b = self.rgb_value[0]/255, self.rgb_value[1]/255, self.rgb_value[2]/255
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx-mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = df/mx*10
        v = mx*10

        h_value = round(h)
        s_value = int(round(s,1)*10)
        v_value = int(round(v,1)*10)

        hsv_value = (f'{h_value}, {s_value}%, {v_value}%')

        print(hsv_value)

        self.hsv_menu.outputbar.delete(0, END)
        self.hsv_menu.write_output(hsv_value)


    def colorinput_menu(self):
        #color input title
        self.title =  Label(self.main_frame.frame_output,
                    text='Color Input ( HEX )')
        self.title.grid(row=4, column=2, pady=(9,0), padx=(0,0))

        #color input bar
        self.outputbar = Entry(self.main_frame.frame_output,
                        bg="#e8e8e8",
                        width=self.bar_size)
        self.outputbar.grid(row=5, column=2, padx=(0,0))

        #color input button
        input_btn = Button(self.main_frame.frame_output,
                        width=40,
                        image=self.aset.down_icon,
                        command=self.get_color_input)
        input_btn.grid(row=6, column=2)

    # command to change bg color view 2
    def get_color_input(self):
        try:
            color_value = self.outputbar.get()
            self.view2.config(bg=color_value)
            print(color_value)

        except TclError:
            print("please enter hex color value!")
        

    #color view line title
    def colorview_title_line(self):
        self.colorview_title = Label(self.main_frame.frame_title_view,
                                    text=f"{"_"*5}[ Color Box 1 ]{"_"*12}[ Color Box 2 ]{"_"*5}")
        self.colorview_title.grid(row=0, column=0, pady=(7,0))

#color box 1
    def color_view1(self):
        self.view1 = Label(self.main_frame.frame_view,
                             bg="#FFFFFF",
                             padx=77,
                             pady=90)
        self.view1.grid(row=0, column=0)

    def change_color1(self):
        self.view1.config(bg=self.hex_value)

#color color 2
    def color_view2(self):
        self.view2 = Label(self.main_frame.frame_view,
                            bg="#FFFFFF",
                            padx=77,
                            pady=90)
        self.view2.grid(row=0, column=1)

#text box line title
    def textbox_title_line(self):
        self.textbox_title = Label(self.main_frame.frame_textbox,
                                    text=f"{"_"*15}[ Text Box ]{"_"*15}")
        self.textbox_title.grid(row=0, column=0, pady=(0,0))

#text box
    def text_box(self):
        self.scrollbar_input = Scrollbar(self.main_frame.frame_textbox,
                                                        bg="#cccccc",
                                                        orient="vertical")
        self.scrollbar_input.grid(row=1, column=1, sticky=NS)
        
        self.box = Text(self.main_frame.frame_textbox,
                   width=30,
                   height=7,
                   bd=2,
                   bg="#E7E7E7",
                   yscrollcommand=self.scrollbar_input.set)
        self.box.grid(row=1, column=0, pady=(0,0))

        self.scrollbar_input.config(command=self.box.yview)

#preview line title
    def preview_title_line(self):
        self.textbox_title = Label(self.main_frame.frame_textbox,
                                    text=f"{"_"*15}[ Preview ]{"_"*15}")
        self.textbox_title.grid(row=2, column=0, pady=(0,0))

#menu to preview color aply to a text
    def text_color(self):
        self.config = {'row title' : 0,
                    'column title' : 0,
                    'row output bar' : 1,
                    'bar size' : 12}
        self.text_color_menu = self.output_menu(self.main_frame.frame_preview_input_row1, 'Color ( HEX )', None, self.config)
        self.text_color_menu.output_title()
        self.text_color_menu.output_bar()

    def reverse_color_command(self):
        font_color = self.text_color_menu.outputbar.get()
        bg_color = self.bg_color_menu.outputbar.get()

        self.text_color_menu.outputbar.delete(0, END)
        self.bg_color_menu.outputbar.delete(0, END)

        self.text_color_menu.write_output(bg_color)
        self.bg_color_menu.write_output(font_color)

    def reverse_color_button(self):
        reverse_color_btn = Button(self.main_frame.frame_preview_input_row1,
                                   image=self.aset.reverse_icon,
                                   command=self.reverse_color_command)
        reverse_color_btn.grid(row=1, column=1)

    def bg_color(self):
        self.config = {'row title' : 0,
                    'column title' : 2,
                    'row output bar' : 1,
                    'bar size' : 12}
        self.bg_color_menu = self.output_menu(self.main_frame.frame_preview_input_row1, 'BG Color ( HEX )', None, self.config)
        self.bg_color_menu.output_title()
        self.bg_color_menu.output_bar()

    def text_size(self):
        self.config = {'row title' : 0,
                    'column title' : 0,
                    'row output bar' : 1,
                    'bar size' : 4}
        self.size_menu = self.output_menu(self.main_frame.frame_preview_input_row2, 'Size', None, self.config)
        self.size_menu.output_title()
        self.size_menu.output_bar()
        self.size_menu.outputbar.insert(0,"12")

    def font_listbox(self):
        font_title = Label(self.main_frame.frame_preview_input_row2,
                           text=" Font Style ",
                           pady=0)
        font_title.grid(row=0, column=1, pady=(9,0))

        self.font = ["calibri", "consolas",  "arial", 'Times New Roman', "Noto Sans", "DejaVu Serif", "Nimbus Mono PS", "Z003"]
        list_variable = Variable(value=self.font)

        self.font_lb = Listbox(self.main_frame.frame_preview_input_row2,
                height=1,
                width=20,
                bg="#e8e8e8",
                listvariable=list_variable,
                selectmode=SINGLE)
        self.font_lb.grid(row=1, column=1, padx=(5,0), pady=(0,0))

        self.font_sb = Scrollbar(self.main_frame.frame_preview_input_row2)
        self.font_sb.grid(row=1, column=2)
        self.font_lb.config(yscrollcommand= self.font_sb.set)
        self.font_sb.config(command=self.font_lb.yview)

    def change_text_color(self):
        textcolor_val = self.text_color_menu.outputbar.get()
        try:
            self.text_prev.config(fg=textcolor_val)
            print(f"text color = {textcolor_val}")

        except TclError:
            print("please enter hex color for the font")

    def change_bg_color(self):
        bgcolor_val = self.bg_color_menu.outputbar.get()
        try:
            self.text_prev.config(bg=bgcolor_val)
            print(f"bg color = {bgcolor_val}")

        except TclError:
            print("please enter hex color for the background")


    def change_font_size(self):
        try:
            selected_indices = str(self.font_lb.curselection())
            replace_char = str.maketrans({"(":"", ")":"", ",":""})

            index_font = selected_indices.translate(replace_char)
            self.choosen_font = self.font[int(index_font)]

            self.value_size = self.size_menu.outputbar.get()

            if int(self.value_size) <= 30:
                self.text_prev.config(font=(self.choosen_font, int(self.value_size)))
                print(f"{selected_indices} > {index_font} > {self.choosen_font}")
            else:
                mb.showerror("font size limit", "font size is limited to 30 only")

        except ValueError:
            return

    
    def text_preview_border(self):
        enter_btn = Button(self.main_frame.frame_preview_input_row3,
                        width=100,
                        image=self.aset.down_icon,
                        command=lambda:[self.change_font_size(), self.change_text_color(), self.change_bg_color()])
        enter_btn.grid(row=0, column=0, pady=(5,0))


        self.text_preview_line1 = Label(self.main_frame.frame_preview_input_row3,
                                    text=f"{"_"*45}")
        self.text_preview_line1.grid(row=1, column=0, pady=(0,10))


        self.text_prev = Label(self.main_frame.frame_preview_input_row3,
                                text="Hello Word",
                                relief="sunken",
                                font=("calibry", 12),
                                fg="#000000",
                                bg="#FFFFFF",
                                padx=10,
                                pady=5)
        self.text_prev.grid(row=2, column=0, pady=(0,0))

        self.text_preview_line2 = Label(self.main_frame.frame_preview_input_row3,
                                    text=f"{"_"*45}")
        self.text_preview_line2.grid(row=3, column=0, pady=(0,0))