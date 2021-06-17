from tkinter import *
root=Tk()
root.title("Shivam")
root.geometry("555x444")
Label(root,text="Shivam Bus Service",font="23").grid(row=0,column=3)

def hello():
    print("hii")
    print(f"{nvalue.get(),phvalue.get(),gvalue.get(),evalue.get(),pavalue.get(),foodvalue.get()}")
    with open("record.txt","a") as f:
        f.write(f"{nvalue.get(),phvalue.get(),gvalue.get(),evalue.get(),pavalue.get(),foodvalue.get()}\n")

name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
payment=Label(root,text="Payment")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)

nvalue=StringVar()
phvalue=StringVar()
gvalue=StringVar()
evalue=StringVar()
pavalue=StringVar()
foodvalue=IntVar()


nameentry=Entry(root,textvariable=nvalue)
phoneentry=Entry(root,textvariable=phvalue)
genderentry=Entry(root,textvariable=gvalue)
emergencyentry=Entry(root,textvariable=evalue)
paymententry=Entry(root,textvariable=pavalue)


nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

foodservice=Checkbutton(text="I need food ",variable=foodvalue).grid(row=6,column=3)

Button(text="Submit",command=hello).grid(row=7,column=3)
root.mainloop()