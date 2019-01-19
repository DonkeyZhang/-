#-*-coding:utf-8-*-
from functools import  partial
import  tkinter

def hello():
    lb1.config(text='hello world!')
def say_hi(word):
    def greet():
        lb1.config(text='hello %s' % word)
    return greet

def welcome():
    lb1.config(text='hello tedu!')
root = tkinter.Tk()
lb1 = tkinter.Label(root, text='hello world!', font='Arial 20 bold ')

Mybutton=partial(tkinter.Button, root, fg='white', bg='blue')
b1=Mybutton(text='Button 1',command=say_hi('china'))
b2=Mybutton(text='Button 2',command=say_hi('Tedu'))
b3=Mybutton(text='Button 3')
b4=Mybutton(text='quit', command=root.quit)

for item in (lb1,b1, b2 ,b3 ,b4):
    item.pack()

root.mainloop()