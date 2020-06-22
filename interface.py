from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from logic import parse_str

allowed_symbols = {
    '-': '-', '+': '+', '=': '=', 'period': '.',
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
    '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
    'slash': '/', 'minus': '-', 'plus': '+', 'asterisk': '×',
    'Delete': '←', 'backslash': '←', 'Return': '=',
    'parenleft': '(', 'parenright': ')'
}

math_symbols = ['-', '+', '×', '/', 'slash', 'minus', 'plus', 'asterisk', 'backslash']

bttn_list = [
    '(', ')', 'AC', '←',
    'x^y', 'x ^ 2', 'sqrt(x)', '+/-',
    '7', '8', '9', '×',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '.', '0', '=', '/'
]

# Listen keyboard + convert keyboard button to win_calc
def listen_keyboard(event):
    if event.keysym in allowed_symbols:
        read_keys(allowed_symbols.get(event.keysym))
    elif event.keysym == 'Escape':
        win_calc.quit()
    else:
        messagebox.Message('Wrong')
        print(event.keysym)


def read_keys(key):
    if '0' <= key <= '9':
        entry_string.insert(INSERT, key)
    elif key in {'.', 'period'}:
        entry_string.insert(INSERT, '.')
    elif key in {'+', '-', '/', '×', '(', ')'}:
        if result_string.get() == str(0):
            entry_string.insert(INSERT, ' ' + key + ' ')
        else:
            entry_string.delete(0, INSERT)
            entry_string.insert(INSERT, result_string.get())
            entry_string.insert(INSERT, ' ' + key + ' ')
    elif key in {'x^y','x ^ 2','sqrt(x)', '+/-'}:
        if key == 'x^y':
            entry_string.insert(INSERT, ' ^ ')
        elif key == 'x ^ 2':
            entry_string.insert(INSERT, ' ^ 2 ')
        elif key == '+/-':
            entry_string.insert(INSERT, '-')
        elif key == 'sqrt(x)':
            if result_string.get() == str(0):
                entry_string.insert(END, ' ^ 0.5 ')
            else:
                result = result_string.get()
                entry_string.delete(0, END)
                entry_string.insert(0, result + ' ^ 0.5')

    elif key == '←':
        entry_string.delete(len(entry_string.get()) - 1)
    elif key == 'AC':
        entry_string.delete(0, END)
        result_string.delete(0, END)
        result = 0
        result_string.insert(END, 0)
    elif key == '=':
        expr = list(map(str, entry_string.get().split()))
        result = parse_str(expr)
        result_string.delete(0, END)
        result_string.insert(END, result)




# Main windows
win_calc = Tk()
win_calc.title('Stack Calculator')
win_calc.resizable(False, False)
win_calc.iconbitmap('calculator-interface.ico')

# Result string (Default value is 0)
result_string = Entry(win_calc, width=65)
result_string.grid(column=0, row=0, columnspan=4)
result_string.bind('<Control-v>', lambda e: 'break')
result_string.insert(END, 0)

# Entry string (Default value is Empty)
entry_string = Entry(win_calc, width=65)
entry_string.bind('<Control-v>', lambda e: 'break') #disable Paste - Ctrl+V
entry_string.bind('<Button-3>', lambda e: 'break') #disable Paste - Right Click
entry_string.grid(column=0, row=1, columnspan=4)


# Button constructor. Button get value from text in button
r, c = 2, 0
i = 0
for i in bttn_list:
    cmd = lambda x=i: read_keys(x)
    ttk.Button(win_calc, text=i, width=15, command=cmd).grid(row=r, column=c)
    c += 1
    k = i
    if c > 3:
        c = 0
        r += 1

# Keyboard listener
win_calc.bind('<Key>', listen_keyboard)
win_calc.mainloop()