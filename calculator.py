from tkinter import *

window = Tk()
window.title('Калькулятор')
window.geometry('400x400')
window['bg'] = '#b2ec5d'


def input_into_entry(symbol):
    entry.insert(END, symbol)


def clear():
    entry.delete(0, END)


def count_result():
    text = entry.get()
    result = 0
    if '+' in text:
        splitted_text = text.split('+')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first + second
    if '-' in text:
        splitted_text = text.split('-')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first - second
    if '/' in text:
        splitted_text = text.split('/')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first / second
    if '*' in text:
        splitted_text = text.split('*')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first * second
    clear()
    entry.insert(0, result)


entry = Entry(window, width=13, font=('', 20))
entry.place(x=100, y=50)

btn1 = Button(window, bg='white', fg='black', text='1', command=lambda: input_into_entry('1'))
btn1.place(x=100, y=100, width=50, height=50)

btn2 = Button(window, bg='white', fg='black', text='2', command=lambda: input_into_entry('2'))
btn2.place(x=150, y=100, width=50, height=50)

btn3 = Button(window, bg='white', fg='black', text='3', command=lambda: input_into_entry('3'))
btn3.place(x=200, y=100, width=50, height=50)

btn4 = Button(window, bg='white', fg='black', text='+', command=lambda: input_into_entry('+'))
btn4.place(x=250, y=100, width=50, height=50)

btn5 = Button(window, bg='white', fg='black', text='4', command=lambda: input_into_entry('4'))
btn5.place(x=100, y=150, width=50, height=50)

btn6 = Button(window, bg='white', fg='black', text='5', command=lambda: input_into_entry('5'))
btn6.place(x=150, y=150, width=50, height=50)

btn7 = Button(window, bg='white', fg='black', text='6', command=lambda: input_into_entry('6'))
btn7.place(x=200, y=150, width=50, height=50)

btn8 = Button(window, bg='white', fg='black', text='-', command=lambda: input_into_entry('-'))
btn8.place(x=250, y=150, width=50, height=50)

btn9 = Button(window, bg='white', fg='black', text='7', command=lambda: input_into_entry('7'))
btn9.place(x=100, y=200, width=50, height=50)

btn10 = Button(window, bg='white', fg='black', text='8', command=lambda: input_into_entry('8'))
btn10.place(x=150, y=200, width=50, height=50)

btn11 = Button(window, bg='white', fg='black', text='9', command=lambda: input_into_entry('9'))
btn11.place(x=200, y=200, width=50, height=50)

btn12 = Button(window, bg='white', fg='black', text='÷', command=lambda: input_into_entry('/'))
btn12.place(x=250, y=200, width=50, height=50)

btn13 = Button(window, bg='white', fg='black', text='.', command=lambda: input_into_entry('.'))
btn13.place(x=100, y=250, width=50, height=50)

btn17 = Button(window, bg='white', fg='black', text='0', command=lambda: input_into_entry('0'))
btn17.place(x=150, y=250, width=50, height=50)

btn15 = Button(window, bg='white', fg='black', text='=', command=count_result)
btn15.place(x=200, y=250, width=50, height=50)

btn16 = Button(window, bg='white', fg='black', text='x', command=lambda: input_into_entry('*'))
btn16.place(x=250, y=250, width=50, height=50)

btn14 = Button(window, bg='white', fg='black', text='C', command=clear)
btn14.place(x=150, y=300, width=50, height=50)

window.mainloop()
