from tkinter import *
import random
import time
import sqlite3


root=Tk()
root.title("Restaurant Management System")
root.geometry("1600x800+0+0")
f1=PhotoImage(file="restaurant.gif")
root.iconphoto(False,f1)


var2=StringVar()
fries=IntVar()
burger=IntVar()
Veg=IntVar()
chicken=IntVar()
cheese=IntVar()
drinks=IntVar()
cost_of_meal=IntVar()
sgst=IntVar()
cgst=IntVar()
sub_total=IntVar()
total_cost=IntVar()

l=IntVar()
b=IntVar()
v=IntVar()
chi=IntVar()
che=IntVar()
d=IntVar()

tf=IntVar()
tb=IntVar()
tv=IntVar()
tchi=IntVar()
tche=IntVar()
td=IntVar()

l.set(100)
b.set(75)
v.set(120)
chi.set(300)
che.set(290)
d.set(45)


def ref():
    x=random.randint(10908,500876)
    rand=str(x)
    var2.set(rand)

  

    cof=float(fries.get())
    cof1=cof*100
    tf.set(cof1)
    cob=float(burger.get())
    cob1=cob*75
    tb.set(cob1)
    cov=float(Veg.get())
    cov1=cov*120
    tv.set(cov1)
    cochi=float(chicken.get())
    cochi1=cochi*300
    tchi.set(cochi1)
    coche=float(cheese.get())
    coche1=coche*290
    tche.set(coche1)
    cod=float(drinks.get())
    cod1=cod*45
    td.set(cod1)

    tcom=cof1+cob1+cov1+cochi1+coche1+cod1
    cost_of_meal.set(tcom)

    sgst1=tcom*0.09
    sgst.set(sgst1)
    cgst1=tcom*0.12
    cgst.set(cgst1)

    sub_total.set(tcom)

    total_cost1=int(tcom+sgst1+cgst1)
    total_cost.set(total_cost1)
    


#--------------------------------------for database coneection (sqlit3)-------------------------------------------------
   
    
    
def database():
    ref1=var2.get()
    #fr=fries.get()
    #bur=burger.get()
    #Ve=Veg.get()
    #ch=chicken.get()
    #ch2=cheese.get()
    #dr=drinks.get()
    c_o_m=cost_of_meal.get()
    sg=sgst.get()
    cg=cgst.get()
    su=sub_total.get()
    to=total_cost.get()

    tf1=tf.get()
    tb1=tb.get()
    tv1=tv.get()
    tchi1=tchi.get()
    tche1=tche.get()
    td1=td.get()

    conn=sqlite3.connect("restaurant_management_system.db")
    with conn:
        cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS restaurant(Reference TEXT,Fries TEXT,Burger TEXT,Veg TEXT,Chicken TEXT,Cheese TEXT,Drinks TEXT,Cost_of_meal TEXT,SGST TEXT,CGST TEXT,Sub_total TEXT,Total_cost TEXT)")
    cursor.execute("INSERT INTO restaurant(Reference,Fries,Burger,Veg,Chicken,Cheese,Drinks,Cost_of_meal,SGST,CGST,Sub_total,Total_cost) values(?,?,?,?,?,?,?,?,?,?,?,?)",(ref1,tf1,tb1,tv1,tchi1,tche1,td1,c_o_m,sg,cg,su,to))
    conn.commit()
    

#----------------------------------------------------------------------------------------------------------------------  

    
 
    
    

    

def exit1():
    root.destroy()

def reset1():
    var2.set("")
    fries.set(0)
    burger.set(0)
    Veg.set(0)
    chicken.set(0)
    cheese.set(0)
    drinks.set(0)
    cost_of_meal.set(0)
    sgst.set(0)
    cgst.set(0)
    sub_total.set(0)
    total_cost.set(0)
    tf.set(0)
    tf.set(0)
    tb.set(0)
    tv.set(0)
    tchi.set(0)
    tche.set(0)
    td.set(0)

    
    


frame=Frame(root,bg="powder blue",height=150,width=1600,relief="raised")
frame.pack(side=TOP)

frame2=Frame(root,bg="powder blue",width=1300,height=800)
frame2.pack(side=LEFT)

frame3=Frame(root,bg="white",width=200,height=400)
frame3.pack(side=RIGHT)

label_1=Label(root,text="Restaurant Management Systems",width=50,height=2,font="algerian 30 bold",fg="steel blue")
label_1.place(x=150,y=30)

localtime=time.asctime(time.localtime(time.time()))
label_2=Label(root,text=localtime,width=20,font="arial 20 bold",fg="steel blue")
label_2.place(x=600,y=140)




label_3=Label(frame2,text="Reference",height=2,width=12,font="arial 12 bold")
label_3.place(x=50,y=100)
entry_1=Entry(frame2,width=35,font="arial 15 italic",bd=5,justify="right",textvariable=var2)
entry_1.place(x=200,y=105)


label_00=Label(frame2,text="Quantity",height=2,width=12,font="arial 12 bold")
label_00.place(x=190,y=50)


label_4=Label(frame2,text="Large Fries",height=2,width=12,font="arial 12 bold")
label_4.place(x=50,y=150)
entry_2=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=fries)
entry_2.place(x=200,y=155)

label_5=Label(frame2,text="Burger Meal",height=2,width=12,font="arial 12 bold")
label_5.place(x=50,y=200)
entry_3=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=burger)
entry_3.place(x=200,y=205)

label_6=Label(frame2,text="Veg Meal",height=2,width=12,font="arial 12 bold")
label_6.place(x=50,y=250)
entry_4=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=Veg)
entry_4.place(x=200,y=255)

label_7=Label(frame2,text="Chicken Meal",height=2,width=12,font="arial 12 bold")
label_7.place(x=50,y=300)
entry_5=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=chicken)
entry_5.place(x=200,y=305)

label_8=Label(frame2,text="Cheese Meal",height=2,width=12,font="arial 12 bold")
label_8.place(x=50,y=350)
entry_6=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=cheese)
entry_6.place(x=200,y=355)



label_100=Label(frame2,text="Quantity",height=2,width=12,font="arial 12 bold")
label_100.place(x=845,y=50)

label_30=Label(frame2,text="Drinks",height=2,width=12,font="arial 12 bold")
label_30.place(x=700,y=100)
entry_10=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=drinks)
entry_10.place(x=855,y=105)

label_40=Label(frame2,text="Cost of Meal",height=2,width=12,font="arial 12 bold")
label_40.place(x=700,y=150)
entry_20=Entry(frame2,width=35,font="arial 15 italic",bd=5,justify="right",textvariable=cost_of_meal)
entry_20.place(x=855,y=155)

label_50=Label(frame2,text="SGST",height=2,width=12,font="arial 12 bold")
label_50.place(x=700,y=200)
entry_30=Entry(frame2,width=35,font="arial 15 italic",bd=5,justify="right",textvariable=sgst)
entry_30.place(x=855,y=205)

label_6=Label(frame2,text="CGST",height=2,width=12,font="arial 12 bold")
label_6.place(x=700,y=250)
entry_4=Entry(frame2,width=35,font="arial 15 italic",bd=5,justify="right",textvariable=cgst)
entry_4.place(x=855,y=255)

label_7=Label(frame2,text="Sub Total",height=2,width=12,font="arial 12 bold")
label_7.place(x=700,y=300)
entry_5=Entry(frame2,width=35,font="arial 15 italic",bd=5,justify="right",textvariable=sub_total)
entry_5.place(x=855,y=305)

label_80=Label(frame2,text="Total Cost",height=2,width=12,font="arial 12 bold")
label_80.place(x=700,y=350)
entry_60=Entry(frame2,width=35,font="arial 15 italic",bd=5,justify="right",textvariable=total_cost)
entry_60.place(x=855,y=355)


#--------------------------Buttons--------------------------------------------------------

button_1=Button(frame2,width=15,height=2,text="Total",command=ref,bd=10,font="arial 15 bold",activeforeground="steel blue")
button_1.place(x=250,y=500)

button_2=Button(frame2,width=15,height=2,text="Reset",bd=10,font="arial 15 bold",activeforeground="steel blue",command=reset1)
button_2.place(x=500,y=500)

button_3=Button(frame2,width=15,height=2,text="Quit",bd=10,font="arial 15 bold",activeforeground="steel blue",command=exit1)
button_3.place(x=750,y=500)

button_4=Button(frame2,width=12,height=2,text="Save",bd=5,font="arial 10 bold",activeforeground="steel blue",command=database)
button_4.place(x=1150,y=580)
#-----------------------------------------------------------------------------------------

canvas=Canvas(frame3,height=1000,width=600)
photo1=PhotoImage(file="cafe.gif")
canvas.create_image(700,20,anchor=NE,image=photo1)
canvas.pack()
#-------------------------------------------------------------

label_9=Label(frame2,text="Price(per unit)",height=2,width=12,font="arial 12 bold")
label_9.place(x=335,y=50)
entry_200=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=l)
entry_200.place(x=340,y=155)
entry_300=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=b)
entry_300.place(x=340,y=205)
entry_400=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=v)
entry_400.place(x=340,y=255)
entry_500=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=chi)
entry_500.place(x=340,y=305)
entry_600=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=che)
entry_600.place(x=340,y=355)



label_10=Label(frame2,text="Total Price",height=2,width=12,font="arial 12 bold")
label_10.place(x=480,y=50)
entry_2000=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=tf)
entry_2000.place(x=490,y=155)
entry_3000=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=tb)
entry_3000.place(x=490,y=205)
entry_4000=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=tv)
entry_4000.place(x=490,y=255)
entry_5000=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=tchi)
entry_5000.place(x=490,y=305)
entry_6000=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=tche)
entry_6000.place(x=490,y=355)


label_1000=Label(frame2,text="Price(per unit)",height=2,width=12,font="arial 12 bold")
label_1000.place(x=990,y=50)
entry_70=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=d)
entry_70.place(x=1000,y=105)


label_000=Label(frame2,text="Total Price",height=2,width=12,font="arial 12 bold")
label_000.place(x=1135,y=50)
entry_700=Entry(frame2,width=8,font="arial 15 italic",bd=5,justify="right",textvariable=td)
entry_700.place(x=1145,y=105)







root.mainloop()
