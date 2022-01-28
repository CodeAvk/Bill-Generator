from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("@Avk Bill Generator")
root.resizable(False,False)
root.wm_iconbitmap("Bill.ico")

# Here is the Reset Button
def Reset():
    entry_Burgur.delete(0,END)
    entry_French_fries.delete(0,END)
    entry_Choco_mud_Pie.delete(0,END)
    entry_Buddy_Meal.delete(0,END)
    entry_Pepsi_Pet.delete(0,END)
    entry_Red_Bull.delete(0,END)
    entry_Coke.delete(0,END)

 # Here is the Total Button 
def Total():
 try:a1=int(Burgur.get())
 except:a1=0

 try:a2=int(French_fries.get())
 except:a2=0

 try:a3=int(Choco_Mud_Pie.get())
 except:a3=0

 try:a4=int(Buddy_Meal.get())
 except:a4=0

 try:a5=int(Pepsi_PET.get())
 except:a5=0

 try:a6=int(Red_Bull.get())
 except:a6=0

 try:a7=int(Coke.get())
 except:a7=0

 # defining cost of items
 c1=90*a1
 c2=50*a2
 c3=119*a3
 c4=460*a4
 c5=60*a5
 c6=160*a6
 c7=90*a7

 lbl_total=Label(f2,text="Total",font="aria  20 bold",width="16",fg="lightyellow",bg="black" )
 lbl_total.place(x=0,y=50)

 entry_total=Entry(f2,font="DS-Digital  20  bold",textvariable=Total_bill,bd=6,width=8,bg="black",fg="cyan")
 entry_total.place(x=0,y=100)

 totalcost=c1+c2+c3+c4+c5+c6+c7
 string_bill="Rs.",str(f"{totalcost}")
 Total_bill.set(string_bill)

Label(text="Bill Generator",bg="black",fg="orange",font="calibri 33  bold",width="300",height="2").pack()


# Menu Bar
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

# items inside Menu
Label(f,text="Menu",font="Gabriola 40  bold",bg="lightgreen",fg="black").place(x="80",y=0)
Label(f,text="Burgur.........Rs.90",font=("Lucida Calligraphy" ,15,  'bold'),bg="lightgreen",fg="black").place(x="20",y="80")
Label(f,text="French fries.........Rs.50",font=("Lucida Calligraphy" ,15,  'bold'),bg="lightgreen",fg="black").place(x="18",y="110")
Label(f,text="Choco-Mud-Pie.....Rs.119",font=("Lucida Calligraphy" ,15,  'bold'),bg="lightgreen",fg="black").place(x="15",y="140")
Label(f,text="Buddy Meal.......Rs.460",font=("Lucida Calligraphy" ,15,  'bold'),bg="lightgreen",fg="black").place(x="15",y="170")
Label(f,text="Pepsi PET.........Rs.60",font=("Lucida Calligraphy" ,15,  'bold'),bg="lightgreen",fg="black").place(x="20",y="200")
Label(f,text="Red Bull.........Rs.160",font=("Lucida Calligraphy" ,15,  'bold'),bg="lightgreen",fg="black").place(x="20",y="230")
Label(f,text="Coke.........Rs.90",font=("Lucida Calligraphy" ,15,  'bold'),bg="lightgreen",fg="black").place(x="20",y="260")


# Bill Interface
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",bg="lightyellow",font="calibri 20")
Bill.place(x=120,y=10)

#Entry

f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Burgur=StringVar()
French_fries=StringVar()
Choco_Mud_Pie=StringVar()
Buddy_Meal=StringVar()
Pepsi_PET=StringVar()
Red_Bull=StringVar()
Coke=StringVar()
Total_bill=StringVar()
# Labels
lbl_Burgur=Label(f1,font="aria 20 bold",text="Burgur",width=12,fg="blue4")
lbl_French_fries=Label(f1,font="aria 20 bold",text="French_fries",width=12,fg="blue4")
lbl_Choco_Mud_Pie=Label(f1,font="aria 20 bold",text="Choco_Mud_Pie",width=12,fg="blue4")
lbl_Buddy_Meal=Label(f1,font="aria 20 bold",text="Buddy_Meal",width=12,fg="blue4")
lbl_Pepsi_PET=Label(f1,font="aria 20 bold",text="Pepsi_PET",width=12,fg="blue4")
lbl_Red_Bull=Label(f1,font="aria 20 bold",text="Red_Bull",width=12,fg="blue4")
lbl_Coke=Label(f1,font="aria 20 bold",text="Coke",width=12,fg="blue4")


lbl_Burgur.grid(row=1,column=0)
lbl_French_fries.grid(row=2,column=0)
lbl_Choco_Mud_Pie.grid(row=3,column=0)
lbl_Buddy_Meal.grid(row=4,column=0)
lbl_Pepsi_PET.grid(row=5,column=0)
lbl_Red_Bull.grid(row=6,column=0)
lbl_Coke.grid(row=7,column=0)


#Entry
entry_Burgur=Entry(f1,font="DS-Digital  20  bold ",textvariable=Burgur,bd=6,width=8,bg="black",fg="cyan")
entry_French_fries=Entry(f1,font="DS-Digital  20  bold ",textvariable=French_fries,bd=6,width=8,bg="black",fg="cyan")
entry_Choco_mud_Pie=Entry(f1,font="DS-Digital  20  bold",textvariable=Choco_Mud_Pie,bd=6,width=8,bg="black",fg="cyan")
entry_Buddy_Meal=Entry(f1,font="DS-Digital  20  bold ",textvariable=Buddy_Meal,bd=6,width=8,bg="black",fg="cyan")
entry_Pepsi_Pet=Entry(f1,font="DS-Digital  20  bold",textvariable=Pepsi_PET,bd=6,width=8,bg="black",fg="cyan")
entry_Red_Bull=Entry(f1,font="DS-Digital  20  bold ",textvariable=Red_Bull,bd=6,width=8,bg="black",fg="cyan")
entry_Coke=Entry(f1,font="DS-Digital  20  bold",textvariable=Coke,bd=6,width=8,bg="black",fg="cyan")

entry_Burgur.grid(row=1,column=1)
entry_French_fries.grid(row=2,column=1)
entry_Choco_mud_Pie.grid(row=3,column=1)
entry_Buddy_Meal.grid(row=4,column=1)
entry_Pepsi_Pet.grid(row=5,column=1)
entry_Red_Bull.grid(row=6,column=1)
entry_Coke.grid(row=7,column=1)


#Button
btn_reset=Button(f1,bd=5,fg="white",bg="black",font="ariel 16 bold ",width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)
btn_total=Button(f1,bd=5,fg="black",font="ariel 16 bold",width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)
root.mainloop()
