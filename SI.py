from cProfile import label
from tkinter import *
from unittest import result
window=Tk()

window.title('SI calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_SI():
    p=int(principal_entry.get())
    r=int(rate_entry.get())
    t=float(time_entry.get())
    SI=(p*r*t)/100
    SI=round(SI,1)
    
    result_label.destroy()

    
    output_message=Label(result_frame,text=",You're SI is "+str(SI),bg="lightcyan",font=("caliber",12),width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(window,text="SI calculator",fg="black",bg="lightcyan",font=("caliber",20),bd=5)
app_label.place(x=50,y=20)

principal_label=Label(window,text="enter prinicpal amount",fg="black",bg="lightcyan",font=('caliber',12))
principal_label.place(x=20,y=100)

principal_entry=Entry(window,text="",bd=2,width=15)
principal_entry.place(x=150,y=102)

rate_label=Label(window,text="enter rate",fg="black",bg="lightcyan",font=('caliber',12))
rate_label.place(x=20,y=145)

rate_entry=Entry(window,text="",bd=2,width=15)
rate_entry.place(x=150,y=144)

time_label=Label(window,text="enter time",fg="black",bg="lightcyan",font=('caliber',12))
time_label.place(x=20,y=185)

time_entry=Entry(window,text="",bd=2,width=15)
time_entry.place(x=150,y=186)

calculate_button=Button(window,text="calculate",fg="black",bg="lightcyan",bd=4,command=calculate_SI)
calculate_button.place(x=20,y=225)

result_frame=LabelFrame(window,text="result",bg="lightcyan",font=("caliber",12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=275)

result_label=Label(result_frame,text="",bg="lightcyan",font=('caliber',12),width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()