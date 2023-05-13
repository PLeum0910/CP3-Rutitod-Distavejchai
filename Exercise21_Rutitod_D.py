from tkinter import *
import math
fontsize = 25

def leftclickbutton(event):
    result = (float(textboxweight.get())/math.pow(float(textboxheight.get())/100,2))
    labelresult.configure(text=result)
    if result >= 30:
        text_result.configure(text="อ้วนมาก")
    elif result >= 25:
        text_result.configure(text="อ้วน")
    elif result >= 23:
        text_result.configure(text="น้ำหนักเกิน")
    elif result >= 18.6:
        text_result.configure(text="น้ำหนักปกติ")
    elif result <= 18.5:
        text_result.configure(text="ผอมเกินไป")

Mainwindow = Tk()
labelheight = Label(Mainwindow,text = "ส่วนสูง (cm)",font= ("supermarket",fontsize))
labelheight.grid(row=0,column=0)

textboxheight = Entry(Mainwindow)
textboxheight.grid(row=0,column=1)

labelweight = Label(Mainwindow,text = "น้ำหนัก (kg)",font= ("supermarket",fontsize))
labelweight.grid(row=1,column=0)

textboxweight = Entry(Mainwindow)
textboxweight.grid(row=1,column=1)

calculatebutton = Button(Mainwindow,text = "คำนวณ",font= ("supermarket",fontsize))
calculatebutton.bind('<Button-1>',leftclickbutton)
calculatebutton.grid(row=2)

labelresult = Label(Mainwindow,text= "ผลลัพธ์",font= ("supermarket",fontsize))
labelresult.grid(row=2,column=1)

text_result = Label(Mainwindow,text =" ",font= ("supermarket",fontsize))
text_result.grid(row=3,column=1)

Mainwindow.mainloop()