from tkinter import *
from main_elemen import Main_element

class Main_window:
    def __init__(self):
        #main window
        self.main_window = Tk()
        self.window_setup()
       
        self.main_elemen = Main_element(self.main_window)
        self.main_elemen.insruction()
        self.main_elemen.title_image()
        self.main_elemen.color_button()

        self.main_elemen.hex()
        self.main_elemen.rgb()
        self.main_elemen.cmyk()
        self.main_elemen.hsl()
        self.main_elemen.hsv()
        self.main_elemen.colorinput_menu()

        self.main_elemen.colorview_title_line()
        self.main_elemen.color_view1()
        self.main_elemen.color_view2()

        self.main_elemen.textbox_title_line()
        self.main_elemen.text_box()
        self.main_elemen.preview_title_line()

        self.main_elemen.text_color()
        self.main_elemen.reverse_color_button()
        self.main_elemen.bg_color()
        self.main_elemen.text_size()
        self.main_elemen.font_listbox()

        self.main_elemen.text_preview_border()

        
    def window_setup(self):
        self.main_window.title('Colorpick')
        self.main_window.geometry('929x509')
        app_icon = PhotoImage(file='aset/icon.png')
        self.main_window.iconphoto(True, app_icon)
        self.main_window.resizable(width=False, height=False)

    def run(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = Main_window()
    app.run()