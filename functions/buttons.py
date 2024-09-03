import tkinter.ttk as ttk
import functions.calculator_functions as cf

def simple_calc_buttons(window, textbox):
    ttk.Button(window, text="AC", command=lambda: cf.clear(textbox)).grid(column=0,row=2)
    ttk.Button(window, text="(", command=lambda: cf.add_to_expression('(', textbox)).grid(column=1,row=2)
    ttk.Button(window, text= ")", command= lambda: cf.add_to_expression(')', textbox)). grid(column=2, row=2)
    ttk.Button(window, text="+", command=lambda: cf.add_to_expression('+', textbox)).grid(column=3, row=2)
    ttk.Button(window, text="7", command= lambda: cf.add_to_expression(7, textbox)).grid(column=0, row=3)
    ttk.Button(window, text="8", command=lambda: cf.add_to_expression(8, textbox)).grid(column=1, row=3)
    ttk.Button(window, text="9", command=lambda: cf.add_to_expression(9, textbox)).grid(column=2, row=3)
    ttk.Button(window, text="-", command=lambda: cf.add_to_expression('-', textbox)).grid(column=3, row=3)
    ttk.Button(window, text="4", command=lambda: cf.add_to_expression(4, textbox)).grid(column=0, row=4)
    ttk.Button(window, text="5", command=lambda: cf.add_to_expression(5, textbox)).grid(column=1, row=4)
    ttk.Button(window, text="6", command=lambda: cf.add_to_expression(6, textbox)).grid(column=2, row=4)
    ttk.Button(window, text="*", command=lambda: cf.add_to_expression('*', textbox)).grid(column=3, row=4)
    ttk.Button(window, text="1", command=lambda: cf.add_to_expression(1, textbox)).grid(column=0, row=5)
    ttk.Button(window, text="2", command=lambda: cf.add_to_expression(2, textbox)).grid(column=1, row=5)
    ttk.Button(window, text="3", command=lambda: cf.add_to_expression(3, textbox)).grid(column=2, row=5)
    ttk.Button(window, text="/", command=lambda: cf.add_to_expression('/', textbox)).grid(column=3, row=5)
    ttk.Button(window, text="0", command=lambda: cf.add_to_expression(0, textbox)).grid(column=0, row=6)
    ttk.Button(window, text="00", command=lambda: cf.add_to_expression('00', textbox)).grid(column=1, row=6)
    ttk.Button(window, text=".", command=lambda: cf.add_to_expression('.', textbox)).grid(column=2, row=6)
    ttk.Button(window, text="=", command=lambda: cf.evaluate_expression(textbox)).grid(column=3, row=6)
    return

def scientific_calc_buttons(window, textbox):
    return