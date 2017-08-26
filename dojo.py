from tkinter import *

root = Tk()
root.geometry('1000x500+0+0')
root.title('Dojo Python')

text_input = StringVar()

tops = Frame(root, width = 100, height = 10, bg = 'red', relief = SUNKEN)
tops.pack(side = TOP)

frame = Frame(root, width = 300, height = 10, bg = 'blue', relief = GROOVE)
frame.pack(side = TOP)

lbinfo = Label(tops, font = ('ARIAL', 30, 'bold'), text = 'Dojo Python')
lbinfo.grid(row = 0, column = 0)


def btnClick(numero):
	global operador
	operador = operador + str(numero)
	text_input.set(operador)

def btnEval(numero):
	global operador
	result =  str(eval(operador))
	text_input.set(operador)
	operador = ''

btnCalc = Button(
	frame,
	font = ('ARIAL', 10, 'bold'),
	command = lambda:btnClick(1)
).grid(row = 1, column = 0)

txtDisplay = Entry(
	frame,
	font = ('ARIAL', 12, 'bold'),
	textvariable = text_input
)

txtDisplay.grid()

root.mainloop()