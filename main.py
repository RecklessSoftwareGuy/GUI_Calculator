import tkinter
import tkinter.ttk as ttk
from functions import buttons

def gui_calculator():
    window= tkinter.Tk()
    textbox = tkinter.Text(window, height=1, width=20, font=('Arial', 18))
    textbox.grid(columnspan=5)
    window.title("Calculator")
    buttons.simple_calc_buttons(window, textbox)
    window.mainloop()

gui_calculator()