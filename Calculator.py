from tkinter import *
import pyttsx3

engine=pyttsx3.init()

root=Tk()
root.geometry("542x550")
root.title("Calculator")
root.configure(bg="black")
root.resizable(0,0)

textin=StringVar()
operator=""

label1=Label(root, text="CALCULATOR", font=("Times",30,'bold'), bg="black", fg="white")
label1.pack()

label2=Label(root, text="By: Ekansh", font=("Times",23,'bold'), bg="#04132c", fg="white")
label2.place(x=370,y=488)

e1=Entry(root,font=("Courier New",16,'bold'),textvar=textin,width=25,bd=5,bg='powder blue', justify=RIGHT)
e1.pack()
e1.insert(0,"0")
e1.config(state=DISABLED)

def clickbut(number):
	global operator
	if str(number) in "1234567890":
		engine.say(number)
		engine.runAndWait()
	if number =="-":
		engine.say("minus")
		engine.runAndWait()
	if number=="+":
		engine.say("plus")
		engine.runAndWait()
	if number=="*":
		engine.say("multiplied by")
		engine.runAndWait()
	if number=="/":
		engine.say("divided by")
		engine.runAndWait()
	if number=="=":
		engine.say("equals to")
		engine.runAndWait()	
	operator=operator+str(number)
	textin.set(operator)


def equalbut():
    global operator
    try:
        eq = str(eval(operator))
        textin.set(eq)
        operator = ""
    except ZeroDivisionError:
        textin.set("Cannot divide by zero")
        operator = ""

def clearbut():
	global operator
	textin.set("")
	operator=""
	e1.insert(0,"0")

def funcdel(number):
	global operator
	e1.config(state=NORMAL)
	length=len(e1.get())
	e1.delete(first=length-1,last=length)
	x=e1.get()
	operator=""
	operator=operator+str(x)
	textin.set(operator)
	if length==1:

		textin.set('')
		operator=""
		e1.insert(0,"0")
	e1.config(state=DISABLED)


but1=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(1), text="1", font=("Times",20,'bold'))
but1.place(x=22.5, y=105)
but2=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(2), text="2", font=("Times",20,'bold'))
but2.place(x=98.5, y=105)
but3=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(3), text="3", font=("Times",20,'bold'))
but3.place(x=174.5, y=105)
but4=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(4), text="4", font=("Times",20,'bold'))
but4.place(x=22.5, y=197)
but5=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(5), text="5", font=("Times",20,'bold'))
but5.place(x=98.5, y=197)
but6=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(6), text="6", font=("Times",20,'bold'))
but6.place(x=174.5, y=197)
but7=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(8), text="8", font=("Times",20,'bold'))
but7.place(x=98.5, y=289)
but8=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(7), text="7", font=("Times",20,'bold'))
but8.place(x=22.5, y=289)
but9=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(9), text="9", font=("Times",20,'bold'))
but9.place(x=174.5, y=289)
but10=Button(root,padx=20,pady=20, bg='red',command=lambda:clickbut(0), text="0", font=("Times",20,'bold'))
but10.place(x=22.5, y=381)
but11=Button(root,padx=16,pady=158, bg='#045c04',command=clearbut, text="CE", font=("Times",20,'bold'), fg="white")
but11.place(x=425, y=105)
but12=Button(root,padx=23,pady=20, bg='#ec8c25',command=lambda:clickbut("-"), text="-", font=("Times",20,'bold'))
but12.place(x=251, y=197)
but13=Button(root,padx=20,pady=20, bg='#ec8c25',command=lambda:clickbut("+"), text="+", font=("Times",20,'bold'))
but13.place(x=251, y=105)
but14=Button(root,padx=20,pady=20, bg='#ec8c25',command=lambda:clickbut("*"), text="×", font=("Times",20,'bold'))
but14.place(x=251, y=289)
but15=Button(root,padx=20.5,pady=20, bg='#ec8c25',command=lambda:clickbut("/"), text="÷", font=("Times",20,'bold'))
but15.place(x=249, y=381)
but16=Button(root,padx=9.5,pady=66, bg='#045c04',command=lambda:funcdel(1), text="DEL", font=("Times",20,'bold'), fg="white")
but16.place(x=328, y=105)
but17=Button(root,padx=61,pady=20, bg='#ec8c25',command=lambda:clickbut("."), text=".", font=("Times",20,'bold'))
but17.place(x=98.5, y=381)
but18=Button(root,padx=30,pady=66, bg='#045c04',command=equalbut, text="=", font=("Times",20,'bold'), fg="white")
but18.place(x=327.5, y=289)



mainloop()