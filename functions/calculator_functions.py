expression = ''

def add_to_expression(symbol, textbox):
    global expression
    expression += str(symbol)
    textbox.delete(1.0, 'end')
    textbox.insert(1.0, expression)
    return


def evaluate_expression(textbox):
    global expression
    try:
        result= eval(expression)
        expression = str(result)
        textbox.delete(1.0, 'end')
        textbox.insert(1.0, format(result, ','))
        print("Completed Operation")
    except Exception as e:
        textbox.delete(1.0, 'end')
        textbox.insert(1.0, "Error")
        print(e)
    return

def clear(textbox):
    global expression
    textbox.delete(1.0, 'end')
    expression= ''
    return