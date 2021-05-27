from tkinter import *


def button_handler(num):
    global expression_text

    expression_text = expression_text + str(num)
    expression_label.set(expression_text)


def calculate_answer():
    global expression_text

    try:
        result = str(eval(expression_text))

        expression_label.set(result)

        expression_text = result

    except ZeroDivisionError:
        expression_label.set("Zero Division Error")

        expression_text = ""

    except SyntaxError:
        expression_label.set("Syntax Error")

        expression_text = ""


def clear_window():
    global expression_text

    expression_label.set("")

    expression_text = ""


def backspace():
    global expression_text

    temp = expression_label.get()[:-1]

    expression_label.set(temp)

    expression_text = temp


def close():
    window.destroy()


window = Tk()
window.title("Python Calculator")
window.geometry("500x550")
window.configure(background="white")

expression_text = ""

expression_label = StringVar()

label = Label(window, textvariable=expression_label, font=('Arial', 20), bg="black", fg="white", width=22, height=2, borderwidth=5, relief="raised")
label.pack()

frame = Frame(window)
frame.pack()

button_one = Button(frame, text=1, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(1))
button_one.grid(row=0, column=0)

button_two = Button(frame, text=2, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(2))
button_two.grid(row=0, column=1)

button_three = Button(frame, text=3, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(3))
button_three.grid(row=0, column=2)

button_four = Button(frame, text=4, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(4))
button_four.grid(row=1, column=0)

button_five = Button(frame, text=5, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(5))
button_five.grid(row=1, column=1)

button_six = Button(frame, text=6, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(6))
button_six.grid(row=1, column=2)

button_seven = Button(frame, text=7, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(7))
button_seven.grid(row=2, column=0)

button_eight = Button(frame, text=8, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(8))
button_eight.grid(row=2, column=1)

button_nine = Button(frame, text=9, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(9))
button_nine.grid(row=2, column=2)

button_zero = Button(frame, text=0, height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler(0))
button_zero.grid(row=3, column=0)

button_zerox2 = Button(frame, text='00', height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler('00'))
button_zerox2.grid(row=3, column=1)

button_decimal = Button(frame, text='.', height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler('.'))
button_decimal.grid(row=3, column=2)

button_plus = Button(frame, text='+', height=4, width=9, font=50, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler('+'))
button_plus.grid(row=0, column=3)

button_minus = Button(frame, text='-', height=4, width=9, font=50, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler('-'))
button_minus.grid(row=1, column=3)

button_multiply = Button(frame, text='*', height=4, width=9, font=50, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler('*'))
button_multiply.grid(row=2, column=3)

button_divide = Button(frame, text='/', height=4, width=9, font=50, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: button_handler('/'))
button_divide.grid(row=3, column=3)

button_equals = Button(frame, text='=', height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: calculate_answer())
button_equals.grid(row=4, column=0)

button_clear = Button(frame, text="CLEAR", height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: clear_window())
button_clear.grid(row=4, column=1)

button_delete = Button(frame, text="DEL", height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: backspace())
button_delete.grid(row=4, column=2)

button_off = Button(frame, text="OFF", height=4, width=9, font=35, bg="black", fg="white", activebackground="black", activeforeground="white", command=lambda: close())
button_off.grid(row=4, column=3)

window.mainloop()
