from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import color
import mysql.connector
import customtkinter
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="bala@2471password",
    database="employeedatabasemanagement"
    )
mycursor=mydb.cursor()


root=customtkinter.CTk()
#---------------------------------------FrontpageFrame
def frontpage_frame():
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="white")
    root.state("zoomed")

    global img2
    img2 =PhotoImage(file=r"C:\Users\ADMINLT\Downloads\world2-transformed.png")
    global my_canvas
    my_canvas =Canvas( root , width=1400 , height=1080)
    my_canvas.place(x=0,y=0)
    my_canvas.create_image(700,400,image=img2,anchor="center")
    my_canvas.create_text ( 700 , 300 ,text = "WELCOME to PyWORLD Technologies" , font = ( "times",25,"underline bold" ), fill = "crimson" )
    my_canvas.create_text ( 700 , 370 ,text = "A world of tech", font = ( "times",25,"bold" ), fill = "white" )
    my_canvas.create_text ( 1150 , 650 ,text = "Copyright "+u"\u00A9"+" 2022 by Bala.All Rights Reserved.", font = ( "times",12,"bold" ), fill = "white" )

    menu_frame=customtkinter.CTkFrame(root,width=1900,height=50,fg_color="Black")
    menu_frame.place(x=0,y=0)
    
    btnADMIN=customtkinter.CTkButton(menu_frame,command=adminlogin_frame,text="Admin",width=15, text_font=("calibri", 16), text_color="white", fg_color="black")
    btnADMIN.place(x=685,y =9)
    btnEmployee=customtkinter.CTkButton(menu_frame, command=employee_page ,text="Employee",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnEmployee.place(x =780 , y = 11)
    btnservices=customtkinter.CTkButton(menu_frame ,text="Services",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnservices.place(x =890 , y = 11)
    btnaboutus=customtkinter.CTkButton(menu_frame, text="About Us",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnaboutus.place(x =990 , y = 11)
    btncareer=customtkinter.CTkButton(menu_frame ,text="Careers",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btncareer.place(x =1100 , y = 11)
    btncontactus=customtkinter.CTkButton(menu_frame,text="Contact Us",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btncontactus.place(x =1190 , y = 11)
    btnmore=customtkinter.CTkButton(menu_frame,text="More",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnmore.place(x =1300 , y = 11)
    
    root.mainloop()

#root1 = Tk()

#---------------------------------------AdminLoginFrame    
def adminlogin_frame():
    global root1
    root1=customtkinter.CTkToplevel()
    root1.title("Employee Management System")
    root1.geometry("1920x1080+0+0")
    root1.config(bg="white")
    root1.state("zoomed")
    img7 =PhotoImage(file=r"C:\Users\ADMINLT\Downloads\table2-_ceqrZStw-transformed.png")
    global my_canvas2
    my_canvas2 =Canvas( root1 , width=1000 , height=1080,bg="gold")
    my_canvas2.pack( fill = "both" , expand = True)
    my_canvas2.create_image(700,400,image=img7,anchor="center")
    my_canvas2.create_text ( 1150 , 650 ,text = " PyWORLD Technologies" , font = ( "Helvetica",25,"bold" ), fill = "maroon" )
    global menu_frame
    menu_frame=customtkinter.CTkFrame(root1,width=130,height=1900,fg_color="Black")
    menu_frame.place(x=0,y=50)
    btnEmployee=customtkinter.CTkButton(menu_frame ,text="Employee",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnEmployee.place(x =10 , y = 60)
    btnservices=customtkinter.CTkButton(menu_frame ,text="Services",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnservices.place(x =10 , y = 160)
    btnaboutus=customtkinter.CTkButton(menu_frame ,text="About Us",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnaboutus.place(x =10 , y = 260)
    btncareer=customtkinter.CTkButton(menu_frame ,text="Careers",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btncareer.place(x =10 , y = 360)
    btncontactus=customtkinter.CTkButton(menu_frame ,text="Contact Us",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btncontactus.place(x =10 , y = 460)
    btnmore=customtkinter.CTkButton(menu_frame ,text="More",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnmore.place(x =10 , y = 560)
    btnback=customtkinter.CTkButton(root1, command=root1.destroy ,text=u"\u2190",width=15, text_font=("calibri", 14), text_color="white", fg_color="black")
    btnback.place(x =10 , y = 11)
    Employeename=StringVar()
    password=StringVar()


    my_canvas2.create_text ( 710 , 200 ,text = "Admin Login" , font = ("Calibri", 25 ), fill = "black" )

    my_canvas2.create_text ( 550 , 365 ,text = "Username" , font = ("Calibri", 20 ), fill = "black" )
    txtEmployee = customtkinter.CTkEntry(root1, textvariable=Employeename, text_font=("Calibri", 16), width=230)
    txtEmployee.insert(0,"admin")
    txtEmployee.place(x=750,y=350)

    my_canvas2.create_text ( 550 , 415 ,text = "Password" , font = ("Calibri", 20 ), fill = "black" )
    txtpass = customtkinter.CTkEntry(root1, textvariable=password,show="*", text_font=("Calibri", 16,), width=230,fg="black",bg="white")
    txtpass.place(x=750,y=400)
    def showpass():
        p=txtpass.get()
        lbl=customtkinter.CTkLabel(root1,width=30,text=f"{p}",text_font=("Calibri", 13), bg_color="black", text_color="white")
        lbl.place(x=750,y=450)
    def Ladminlogin():
        username=txtEmployee.get()
        password=txtpass.get()
        if username=="" or password=="":
            messagebox.showerror("Error Input","Please give input username and password")
        elif username=="admin" and password=="logmein":
            adminpage_frame()
        elif username!="admin":
            messagebox.showerror("Error input","Incorrect username")
            txtEmployee.delete(0,END)
            txtEmployee.insert(0,"admin")
            txtpass.delete(0,END)
        else:
            txtpass.delete(0,END)
            messagebox.showerror("Error input","Incorrect password")
    btnlogin=customtkinter.CTkButton(root1, command=Ladminlogin ,text="Login",width=100, text_font=("Calibri", 16), bg_color="blue", fg_color="blue",corner_radius=5).place(x=500,y=520)
    btnshowpass=customtkinter.CTkButton(root1,command=showpass,text="Show Password",width=75, text_font=("Calibri", 10), bg_color="red", fg_color="red",corner_radius=5).place(x=800,y=520)

    root1.mainloop()
#---------------------------------------admin_page_frame
def adminpage_frame():
    my_canvas2.destroy()
    menu_frame.destroy()
    root1.title("Employee Management System")
    root1.geometry("1920x1080+0+0")
    root1.config(bg="dark Blue")
    root1.state("zoomed")

    img7 =PhotoImage(file=r"C:\Users\ADMINLT\Downloads\table3-transformed (1).png")
    my_canvas3 =Canvas( root1 , width=1000 , height=1080,bg="gold")
    my_canvas3.pack( fill = "both" , expand = True)
    my_canvas3.create_image(700,550,image=img7,anchor="center")
    my_canvas3.create_text ( 1150 , 650 ,text = " PyWORLD Technologies" , font = ( "Helvetica",25,"bold" ), fill = "maroon" )
    
    global title
    title = customtkinter.CTkLabel(root1, text="Admin", text_font=("Microsoft YaHei UI light", 15, "bold"), bg="dark blue", text_color="white")
    title.place(x=10,y=2)

    def logout():
        root1.destroy()
        adminlogin_frame()
    global btnadd
    btnadd=customtkinter.CTkButton(root1, command=entries_frame ,text="Add Employee",width=250, text_font=("Calibri", 15), fg_color="blue", text_color="white",corner_radius=10)
    btnadd.place(x=100,y=250)
    global btndelete
    btndelete=customtkinter.CTkButton(root1, command=Delete_frame ,text="Delete Employee",width=250, text_font=("Calibri", 15), fg_color="blue", text_color="white",corner_radius=10)
    btndelete.place(x=100,y=300)
    global btnupdate
    btnupdate=customtkinter.CTkButton(root1, command=update_frame ,text="Update Employee details",width=250, text_font=("Calibri", 15), fg_color="blue", text_color="white",corner_radius=10)
    btnupdate.place(x=100,y=350)
    global btnview
    btnview=customtkinter.CTkButton(root1, command=onedetailview_frame ,text="View Employee details",width=250, text_font=("Calibri", 15), fg_color="blue", text_color="white",corner_radius=10)
    btnview.place(x=100,y=400)
    global btnallview
    btnallview=customtkinter.CTkButton(root1, command=alldetails,text="All Employees details",width=250, text_font=("Calibri", 15), fg_color="blue", text_color="white",corner_radius=10)
    btnallview.place(x=100,y=450)
    btnsignout=customtkinter.CTkButton(root1, command=logout,text="Logout",width=150, text_font=("Calibri", 15), fg_color="red", text_color="white",corner_radius=10)
    btnsignout.place(x=1200,y=10)

    root1.mainloop()
#-------------------------------------entries_frame
def entries_frame():
    root2 = customtkinter.CTkToplevel()
    root2.title("Employee Management System")
    root2.geometry("1920x1080+0+0")
    root2.config(bg="dark Blue")
    root2.state("zoomed")
    img5=PhotoImage(file=r"C:\Users\ADMINLT\Downloads\world1.png")
    my_canvas1 =Canvas( root2 , width=1000 , height=1080)
    my_canvas1.pack( fill = "both" , expand = True)
    my_canvas1.create_image(680,400,image=img5,anchor="center")
    my_canvas1.create_text ( 1150 , 650 ,text = " PyWORLD Technologies" , font = ( "Helvetica",25,"bold" ), fill = "maroon" )

    name = StringVar()
    age = StringVar()
    doj = StringVar()
    gender = StringVar()
    email = StringVar()
    contact = StringVar()
    position=StringVar()
    Employee_ID=StringVar()

    title1= customtkinter.CTkLabel(root2, text="Add Employee", text_font=("Microsoft YaHei UI light", 15, "bold"), text_color="white",fg_color="dark blue", fg="white")
    title1.place(x=10,y=10)    

    lbltxtName= customtkinter.CTkLabel(root2, text="Name", text_font=("Microsoft YaHei UI light", 12), fg_color="blue", text_color="white")
    lbltxtName.place(x=100,y=150)    
    txtName = customtkinter.CTkEntry(root2, textvariable=name, text_font=("Microsoft YaHei UI light", 12), width=300,fg_color="white",text_color="black")
    txtName.place(x=300,y=150)

    lblAge = customtkinter.CTkLabel(root2, text="Age", text_font=("Microsoft YaHei UI light", 12), fg_color="red", text_color="white")
    lblAge.place(x=730,y=150)
    txtAge = customtkinter.CTkEntry(root2, textvariable=age, text_font=("Microsoft YaHei UI light", 12), width=300,fg_color="white",text_color="black")
    txtAge.place(x=930,y=150)

    lbldoj = customtkinter.CTkLabel(root2, text="D.O.J", text_font=("Microsoft YaHei UI light", 12), fg_color="blue", text_color="white")
    lbldoj.place(x=100,y=250)
    txtDoj = customtkinter.CTkEntry(root2, textvariable=doj, text_font=("Microsoft YaHei UI light", 12), width=300,fg_color="white",text_color="black")
    txtDoj.place(x=300,y=250)

    lblEmail = customtkinter.CTkLabel(root2, text="Email", text_font=("Microsoft YaHei UI light", 12), fg_color="red", text_color="white")
    lblEmail.place(x=730,y=250)
    txtEmail = customtkinter.CTkEntry(root2, textvariable=email, text_font=("Microsoft YaHei UI light", 12), width=300,fg_color="white",text_color="black")
    txtEmail.place(x=930,y=250)

    lblGender = customtkinter.CTkLabel(root2, text="Gender", text_font=("Microsoft YaHei UI light", 12), fg_color="blue", text_color="white")
    lblGender.place(x=100,y=350)
    comboGender = customtkinter.CTkComboBox(root2, text_font=("Microsoft YaHei UI light", 12),values= ("Male", "Female"), width=300, state="readonly",text_color="black",fg_color="white")
    comboGender.place(x=300,y=350)

    lblContact = customtkinter.CTkLabel(root2, text="Contact No", text_font=("Microsoft YaHei UI light", 12), fg_color="red", text_color="white")
    lblContact.place(x=730,y=350)
    txtContact = customtkinter.CTkEntry(root2, textvariable=contact, text_font=("Microsoft YaHei UI light", 12), width=300,fg_color="white",text_color="black")
    txtContact.place(x=930,y=350)

    lblEmployee_ID = customtkinter.CTkLabel(root2, text="Employee ID", text_font=("Microsoft YaHei UI light", 12), fg_color="blue", text_color="white")
    lblEmployee_ID.place(x=100,y=450)
    txtEmployee_ID =customtkinter.CTkEntry(root2, textvariable=Employee_ID, text_font=("Microsoft YaHei UI light", 12), width=300,fg_color="white",text_color="black")
    txtEmployee_ID.place(x=300,y=450)

    lblposition = customtkinter.CTkLabel(root2, text="Position", text_font=("Microsoft YaHei UI light", 12), fg_color="red", text_color="white")
    lblposition.place(x=730,y=450)
    comboposition = customtkinter.CTkComboBox(root2, text_font=("Microsoft YaHei UI light", 12),values=("Marketing Manager", "Human Resource","Administrative Assistant","Product Manager","Sales Associate","Sales Manager","Business Analyst","Book Keeper","software Engineer"),width=300, state="readonly",text_color="black",fg_color="black")
    comboposition.place(x=930,y=450)
    
    
    def clearall():
        txtName.delete(0,END)
        txtAge.delete(0,END)
        txtDoj.delete(0,END)
        comboGender.set("")
        txtEmail.delete(0,END)
        txtContact.delete(0,END)
        comboposition.set("")
        txtEmployee_ID.delete(0,END)
    def add_details():
        sql="insert into employees_details (Employee_Id,Name,Age,DOJ,Email,Gender,Contact_No,Position) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(txtEmployee_ID.get(),txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),comboposition.get())
        if txtEmployee_ID.get()=="" or txtName.get()=="" or txtAge.get()==""or txtDoj.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or comboposition.get()=="":
            messagebox.showerror("Input error","please fill all details")
            root2.destroy()
            entries_frame()
            a=StringVar()
            if txtAge.get()==StringVar():
                messagebox.showerror("Input Error","Give age in number") 
                root2.destroy()
                entries_frame()
        else:
            messagebox.askokcancel("Confirmation","Are you sure to add details?")
            mycursor.execute(sql,val)
            mydb.commit()
            root2.destroy()
            messagebox.showinfo("Success","Data added successfully.")
            print("Data Inserted succesfully")
            entries_frame()
            #displayAll()
            #clearall()
    def cancel():
        root2.destroy()
        # for i in root2.winfo_children():
        #     i.destroy()
        #adminpage_frame()
    
    btnADD=customtkinter.CTkButton(root2, command=add_details ,text="Add",width=200, text_font=("Helvetica", 12), fg_color="green", text_color="white").place(x=200,y=550)
    btnclear=customtkinter.CTkButton(root2, command=clearall ,text="clear",width=200, text_font=("Helvetica", 12), fg_color="orange", text_color="white").place(x=500,y=550)
    btncancel=customtkinter.CTkButton(root2, command=cancel ,text="cancel",width=200, text_font=("Helvetica", 12), fg_color="red", text_color="white").place(x=800,y=550)
    root2.mainloop()

#---------------------------------------delete_frame
def Delete_frame():
    root2 = Toplevel()
    root2.title("Employee Management System")
    root2.geometry("1920x1080+0+0")
    root2.config(bg="dark Blue")
    root2.state("zoomed")
    img6=PhotoImage(file=r"C:\Users\ADMINLT\Downloads\world1.png")
    my_canvas1 =Canvas( root2 , width=1000 , height=1080)
    my_canvas1.pack( fill = "both" , expand = True)
    my_canvas1.create_image(680,400,image=img6,anchor="center")
    my_canvas1.create_text ( 1150 , 650 ,text = " PyWORLD Technologies" , font = ( "Helvetica",25,"bold" ), fill = "crimson" )

    id=StringVar()
   
    title = customtkinter.CTkLabel(root2, text="Delete Employee", text_font=("Microsoft YaHei UI light", 15, "bold"), fg_color="dark blue", text_color="white")
    title.place(x=10,y=10)

    lblid = customtkinter.CTkLabel(root2, text="Enter Employee id", text_font=("Microsoft YaHei UI light", 16), fg_color="blue", text_color="white")
    lblid.place(x=400,y=300)
    txtid = customtkinter.CTkEntry(root2, textvariable=id, text_font=("Calibri", 16), width=300)
    txtid.place(x=600,y=300)

   
    def delete():
        sql1="select Employee_Id from employees_details"
        mycursor.execute(sql1)
        result=mycursor.fetchall()
        print(result)
        if txtid.get()=="":
            messagebox.showerror("Input error","Give input")
            root2.destroy()
            Delete_frame()
        elif (txtid.get(),) in result:
            msgbox=messagebox.askokcancel("confirmation","Sure you want to delete?")    
            sql="delete from employees_details where Employee_Id=%s"
            value=(txtid.get(),)
            mycursor.execute(sql,value)
            mydb.commit()
            messagebox.showinfo("Success","Data deleted successfully")
            print("deleted successfully")
            root2.destroy()
            Delete_frame()
            #displayAll()
            #txtid.delete(0,END)
        else:
            messagebox.showerror("error input","Give valid Input")
            root2.destroy()
            Delete_frame()

    btnconfirm=customtkinter.CTkButton(root2, command=delete ,text="Confirm",width=100, text_font=("Microsoft YaHei UI light", 12), fg_color="red", text_color="white").place(x=530,y=400)
    btncancel=customtkinter.CTkButton(root2, command=root2.destroy ,text="Cancel",width=100, text_font=("Microsoft YaHei UI light", 12), fg_color="green", text_color="white").place(x=720,y=400)
    
    root2.mainloop()

#---------------------------------------Update_frame
def update_frame():
    root= Toplevel()
   
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="dark Blue")
    root.state("zoomed")

    img6=PhotoImage(file=r"C:\Users\ADMINLT\Downloads\world1.png")
    my_canvas1 =Canvas( root , width=1000 , height=1080)
    my_canvas1.pack( fill = "both" , expand = True)
    my_canvas1.create_image(680,400,image=img6,anchor="center")
    my_canvas1.create_text ( 1150 , 650 ,text = " PyWORLD Technologies" , font = ( "Helvetica",25,"bold" ), fill = "maroon" )

    title1= Label(root, text="Update Employee", font=("Microsoft YaHei UI light", 15, "bold"), bg="dark blue", fg="white")
    title1.place(x=50,y=10)    

    btnposition=Button(root, command=positionupdate_frame ,text="Position",width=15, font=("Calibri", 15), bg="crimson", fg="white",bd=0)
    btnposition.place(x=600,y=300)
    btnEmail=Button(root, command=emailupdate_frame ,text="Email",width=15, font=("Calibri", 15), bg="crimson", fg="white",bd=0)
    btnEmail.place(x=600,y=350)
    btnContact=Button(root, command=contactupdate_frame,text="Contact No.",width=15, font=("Calibri", 15), bg="crimson", fg="white",bd=0)
    btnContact.place(x=600,y=400)
    btnback=customtkinter.CTkButton(root, command=root.destroy ,text=u"\u2190",width=15, text_font=("calibri", 14), text_color="white", fg_color="black")
    btnback.place(x =10 , y = 11)
    root.mainloop()
#---------------------------------------Position_update
def positionupdate_frame():
    root3=Tk()
    root3.title("Employee Management System")
    root3.geometry("1920x1080+0+0")
    root3.config(bg="dodgerblue")
    root3.state("zoomed")    
    
    position_update= Label(root3, text="Position Update", font=("Microsoft YaHei UI light", 18, "bold"), bg="dodgerblue", fg="white")
    position_update.place(x=10,y=10)

    Employee_id=StringVar()
    employee_id = Label(root3, text="Enter employee ID ", font=("Microsoft YaHei UI light", 15), bg="dodgerblue", fg="white")
    employee_id.place(x=100,y=100)
    txtemployee_id = Entry(root3, textvariable=Employee_id, font=("Microsoft YaHei UI light", 15), width=30)
    txtemployee_id.place(x=300,y=100)
    oldposition=StringVar()
    old_position = Label(root3, text="Old Position ", font=("Microsoft YaHei UI light", 15), bg="dodgerblue", fg="white")
    old_position.place(x=100,y=150)
    oldcomboposition = ttk.Combobox(root3, font=("Microsoft YaHei UI light", 15), width=28, textvariable=oldposition, state="readonly")
    oldcomboposition["values"] = ("Marketing Manager", "Human Resource","Administrative Assistant","Product Manager","Sales Associate","Sales Manager","Business Analyst","Book Keeper","software Engineer")
    oldcomboposition.place(x=300,y=150)
    newposition=StringVar()
    new_position = Label(root3, text="New Position ", font=("Microsoft YaHei UI light", 15), bg="dodgerblue", fg="white")
    new_position.place(x=100,y=200)
    newcomboposition = ttk.Combobox(root3, font=("Microsoft YaHei UI light", 15), width=28, textvariable=newposition, state="readonly")
    newcomboposition["values"] = ("Marketing Manager", "Human Resource","Administrative Assistant","Product Manager","Sales Associate","Sales Manager","Business Analyst","Book Keeper","software Engineer")
    newcomboposition.place(x=300,y=200)

    tree_frame = Frame(root3, bg="dodgerblue")
    tree_frame.place(x=0, y=350 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employees_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()
    def posupdate():
        sql1="select Employee_Id from employees_details"
        mycursor.execute(sql1)
        result=mycursor.fetchall()
        print(result)
        sql2="select Position from employees_details"
        mycursor.execute(sql2)
        result1=mycursor.fetchall()
        print(result1)
        try:
            if oldcomboposition.get()=="" or txtemployee_id.get()=="":
                messagebox.showerror("Error Input"," Give all input")
                root3.destroy()
                posupdate()
            elif (oldcomboposition.get(),) in result1 and (txtemployee_id.get(),) in result:
                sql="update employees_details set Position=%s where Position=%s and Employee_Id=%s"
                val=(newcomboposition.get(),oldcomboposition.get(),txtemployee_id.get()) 
                result2=mycursor.execute(sql,val)
                mydb.commit()
                print("Updated successfully")
                messagebox.Message("Updated successfully")
                displayAll()
        except:
            messagebox.showerror("Error Input","Please give valid Employee ID and Position")
            root3.destroy()
            posupdate()

    btnconfirm=Button(root3, command=posupdate ,text="Confirm",width=15, font=("Helvetica", 15), bg="red", fg="white",bd=3).place(x=200,y=250)
    btncancel=Button(root3, command=root3.destroy ,text="cancel",width=15, font=("Helvetica", 15), bg="red",fg="white",bd=3).place(x=400,y=250)

    root3.mainloop()
#---------------------------------------email_update
def emailupdate_frame():
    root4 = Tk()
    root4.title("Employee Management System")
    root4.geometry("1920x1080+0+0")
    root4.config(bg="dodgerblue")
    root4.state("zoomed")

    Email_frame= Frame(root4, bg="dodgerblue")
    Email_frame.pack(side=TOP, fill=X)
    Email_update= Label(Email_frame, text="Email Update", font=("Microsoft YaHei UI light", 18, "bold"), bg="dodgerblue", fg="white")
    Email_update.grid(row=0, columnspan=15, padx=10, pady=20, sticky="W")

    Employee_id=StringVar()
    employee_id = Label(Email_frame, text="Enter employee ID ", font=("Microsoft YaHei UI light", 15), bg="dodgerblue", fg="white")
    employee_id.grid(row=1, column=1, padx=10, pady=20, sticky="W")
    txtemployee_id = Entry(Email_frame, textvariable=Employee_id, font=("Microsoft YaHei UI light", 15), width=30)
    txtemployee_id.grid(row=1, column=2, padx=10, sticky="w")

    oldemail=StringVar()
    newemail=StringVar()

    old_Email = Label(Email_frame, text="Old Email ", font=("Microsoft YaHei UI light", 15), bg="dodgerblue", fg="white")
    old_Email.grid(row=2, column=1, padx=10, pady=20, sticky="W")
    txtoldemail = Entry(Email_frame, textvariable=oldemail, font=("Microsoft YaHei UI light", 15), width=30)
    txtoldemail.grid(row=2, column=2, padx=10, sticky="w")

    new_Email = Label(Email_frame, text="New Email ", font=("Microsoft YaHei UI light", 15), bg="dodgerblue", fg="white")
    new_Email.grid(row=3, column=1, padx=10, pady=20, sticky="W")
    txtnewemail = Entry(Email_frame, textvariable=newemail, font=("Microsoft YaHei UI light", 15), width=30)
    txtnewemail.grid(row=3, column=2, padx=10, sticky="w")

    tree_frame = Frame(root4, bg="dodgerblue")
    tree_frame.place(x=0, y=400 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employees_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()

    def emailupdate():
        sql1="select Employee_Id from employees_details"
        mycursor.execute(sql1)
        result=mycursor.fetchall()
        print(result)
        sql2="select Email from employees_details"
        mycursor.execute(sql2)
        result1=mycursor.fetchall()
        print(result1)
        try:
            if txtoldemail.get()=="" or txtemployee_id.get()=="" or txtnewemail.get()=="":
                messagebox.showerror("Error Input"," Give all input")
                root4.destroy()
                emailupdate()
            elif (txtoldemail.get(),) in result1 and (txtemployee_id.get(),) in result:
                sql="update employees_details set Email=%s where Email=%s and Employee_Id=%s"
                val=(txtnewemail.get(),txtoldemail.get(),txtemployee_id.get()) 
                result2=mycursor.execute(sql,val)
                mydb.commit()
                print("Updated successfully")
                messagebox.Message("Updated successfully")
                displayAll()
        except:
            messagebox.showerror("Error Input","Please give valid Employee ID and email")
            root4.destroy()
            emailupdate()

    btnclear=Button(Email_frame, command=emailupdate ,text="Confirm",width=15, font=("Helvetica", 15), bg="red", fg="white",bd=3).grid(row=4,column=1,padx=10,pady=10)
    btncancel=Button(Email_frame, command=root4.destroy ,text="cancel",width=15, font=("Helvetica", 15), bg="red",fg="white",bd=3).grid(row=4,column=2,padx=10,pady=10)

#---------------------------------------contact_update
def contactupdate_frame():
    root5 = Tk()
    root5.title("Employee Management System")
    root5.geometry("1920x1080+0+0")
    root5.config(bg="dodger blue")
    root5.state("zoomed")

    Contact_frame= Frame(root5, bg="dodger blue")
    Contact_frame.pack(side=TOP, fill=X)
    Contact_update= Label(Contact_frame, text="Contact Update", font=("Microsoft YaHei UI light", 18, "bold"), bg="dodger blue", fg="white")
    Contact_update.grid(row=0, columnspan=15, padx=10, pady=20, sticky="W")

    Employee_id=StringVar()
    employee_id = Label(Contact_frame, text="Enter employee ID ", font=("Microsoft YaHei UI light", 15), bg="dodger blue", fg="white")
    employee_id.grid(row=1, column=1, padx=10, pady=20, sticky="W")
    txtemployee_id = Entry(Contact_frame, textvariable=Employee_id, font=("Microsoft YaHei UI light", 15), width=30)
    txtemployee_id.grid(row=1, column=2, padx=10, sticky="w")

    oldContact=StringVar()
    newContact=StringVar()

    old_Contact = Label(Contact_frame, text="Old Contact No. ", font=("Microsoft YaHei UI light", 15), bg="dodger blue", fg="white")
    old_Contact.grid(row=2, column=1, padx=10, pady=20, sticky="W")
    txtoldContact = Entry(Contact_frame, textvariable=oldContact, font=("Microsoft YaHei UI light", 15), width=30)
    txtoldContact.grid(row=2, column=2, padx=10, sticky="w")

    new_Contact = Label(Contact_frame, text="New Contact No.", font=("Microsoft YaHei UI light", 15), bg="dodger blue", fg="white")
    new_Contact.grid(row=3, column=1, padx=10, pady=20, sticky="W")
    txtnewContact = Entry(Contact_frame, textvariable=newContact, font=("Microsoft YaHei UI light", 15), width=30)
    txtnewContact.grid(row=3, column=2, padx=10, sticky="w")

    tree_frame = Frame(root5, bg="dodger blue")
    tree_frame.place(x=0, y=400 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employees_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()

    def conupdate():
        sql1="select Employee_Id from employees_details"
        mycursor.execute(sql1)
        result=mycursor.fetchall()
        print(result)
        sql2="select Contact_No from employees_details"
        mycursor.execute(sql2)
        result1=mycursor.fetchall()
        print(result1)
        try:
            if txtoldContact.get()=="" or txtemployee_id.get()=="" or txtnewContact.get()=="":
                messagebox.showerror("Error Input"," Give all input")
                root5.destroy()
                conupdate()
            elif (txtoldContact.get(),) in result1 and (txtemployee_id.get(),) in result:
                sql="update employees_details set Contact_No=%s where Contact_No=%s and Employee_Id=%s"
                val=(txtnewContact.get(),txtoldContact.get(),txtemployee_id.get()) 
                result2=mycursor.execute(sql,val)
                mydb.commit()
                print("Updated successfully")
                messagebox.Message("Updated successfully")
                displayAll()
        except:
            messagebox.showerror("Error Input","Please give valid Employee ID and contact details")
            root5.destroy()
            conupdate()

    btnclear=Button(Contact_frame, command=conupdate ,text="Confirm",width=15, font=("Microsoft YaHei UI light", 15), bg="red", fg="white",bd=3).grid(row=4,column=1,padx=10,pady=10)
    btncancel=Button(Contact_frame, command=root5.destroy ,text="cancel",width=15, font=("Helvetica", 15), bg="red",fg="white",bd=3).grid(row=4,column=2,padx=10,pady=10)


#---------------------------------------onedetailview_frame

def onedetailview_frame():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="gold")
    root.state("zoomed")

    lbl_one_detail= Label(root, text="Employee details", font=("Microsoft YaHei UI light", 18, "bold"), bg="blue", fg="white")
    lbl_one_detail.place(x=0,y=0)

    onedetail_frame= Frame(root, bg="gold",width=300,height=500)
    onedetail_frame.place(x=350,y=250)

    employeeiD=StringVar() 
    password=StringVar()
    employee_iD = Label(onedetail_frame, text="Enter employee Id ", font=("Microsoft YaHei UI light", 15 ), bg="gold", fg="black")
    employee_iD.grid(row=1, column=1, padx=10, pady=20, sticky="W")
    txtemployee_iD = Entry(onedetail_frame, textvariable=employeeiD, font=("Calibri", 15), width=30)
    txtemployee_iD.grid(row=1, column=2, padx=10, sticky="w")

    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=600 , width=1400, height=100)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)

    def displayAll():
        tv.delete(*tv.get_children())
        sql="SELECT * from employees_details where Employee_Id=%s"
        val=(txtemployee_iD.get(),)
        mycursor.execute(sql,val)
        rows=mycursor.fetchall()
        if txtemployee_iD.get()=="" or rows==[]:
            messagebox.showerror("Error Input","Give valid Employee ID")
            root.destroy()
            onedetailview_frame()
        else:                
            for i in rows:
                tv.insert("", END, values=i)
    btnview=Button(onedetail_frame, command=displayAll ,text="View",width=12, font=("Microsoft YaHei UI light", 12,"bold"), bg="red", fg="white",bd=3)
    btnview.grid(row=2,column=2,padx=10,pady=10)

    
#---------------------------------------All Employees detail

def alldetails():
    root1 = Tk()
    root1.title("Employee Management System")
    root1.geometry("1920x1080+0+0")
    root1.config(bg="violet red")
    root1.state("zoomed")

    alldetails_frame= Frame(root1, bg="cyan")
    alldetails_frame.pack(side=TOP, fill=X)

    lbl_all_details= Label(alldetails_frame, text="All Employees details", font=("Calibri", 21, "bold"), bg="dark blue", fg="white")
    lbl_all_details.grid(row=0, column=0, padx=0, pady=20, sticky="W")
    root1.title("Employee Management System")
    root1.geometry("1920x1080+0+0")
    root1.config(bg="dark Blue")
    root1.state("zoomed")
    tree_frame = Frame(root1, bg="cyan")
    tree_frame.place(x=0, y=80 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employees_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()
def treeframe():
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="dark Blue")
    root.state("zoomed")
    tree_frame = Frame(root, bg="dark blue")
    tree_frame.place(x=0, y=80 , width=1400, height=800)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)
    
    def displayAll():
        tv.delete(*tv.get_children())
        mycursor.execute("SELECT * from employees_details")
        rows=mycursor.fetchall()
        for i in rows:
            tv.insert("", END, values=i)
    displayAll()

def employee_page():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("1920x1080+0+0")
    root.config(bg="grey")
    root.state("zoomed")
    btnADMIN=customtkinter.CTkButton(root,command=adminlogin_frame,text="Admin",width=15, text_font=("calibri", 16), text_color="white", fg_color="black")
    btnADMIN.place(x=685,y =9)
    btnEmployee=customtkinter.CTkButton(root, command=employee_page ,text="Employee",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnEmployee.place(x =780 , y = 11)
    btnservices=customtkinter.CTkButton(root ,text="Services",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnservices.place(x =890 , y = 11)
    btnaboutus=customtkinter.CTkButton(root, text="About Us",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnaboutus.place(x =990 , y = 11)
    btncareer=customtkinter.CTkButton(root ,text="Careers",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btncareer.place(x =1100 , y = 11)
    btncontactus=customtkinter.CTkButton(root,text="Contact Us",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btncontactus.place(x =1190 , y = 11)
    btnmore=customtkinter.CTkButton(root,text="More",width=15, text_font=("calibri", 14), text_color="white", fg_color="black",bd=0)
    btnmore.place(x =1300 , y = 11)
    lbl_one_detail= Label(root, text="Employee details", font=("Microsoft YaHei UI light", 18, "bold"), bg="blue", fg="white")
    lbl_one_detail.place(x=0,y=0)

    onedetail_frame= Frame(root, bg="grey",width=300,height=500)
    onedetail_frame.place(x=350,y=250)

    employeeiD=StringVar() 
    password=StringVar()
    employee_iD = Label(onedetail_frame, text="Enter employee Id ", font=("Microsoft YaHei UI light", 15 ), bg="grey", fg="white")
    employee_iD.grid(row=0, column=1, padx=10, pady=20, sticky="W")
    txtemployee_iD = Entry(onedetail_frame, textvariable=employeeiD, font=("Calibri", 15), width=30)
    txtemployee_iD.grid(row=0, column=2, padx=10, sticky="w")
    txtpassword = Label(onedetail_frame, text="Password", font=("Microsoft YaHei UI light", 15 ), bg="grey", fg="white")
    txtpassword.grid(row=1, column=1, padx=10, pady=20, sticky="W")
    entrypassword = Entry(onedetail_frame, textvariable=password,show="*", font=("Calibri", 15), width=30)
    entrypassword.grid(row=1, column=2, padx=10, sticky="w")


    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=600 , width=1400, height=100)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),rowheight=1000)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    global tv 
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="Employee Id")
    tv.column("1", width=2)
    tv.heading("2", text="Name")
    tv.column("2", width=2)
    tv.heading("3", text="Age")
    tv.column("3", width=2)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=2)
    tv.heading("5", text="Email")
    tv.column("5", width=2)
    tv.heading("6", text="Gender")
    tv.column("6", width=2)
    tv.heading("7", text="Contact")
    tv.column("7", width=2)
    tv.heading("8", text="Position")
    tv.column("8", width=2)
    tv['show'] = 'headings'
    tv.pack(fill=X)

    def displayAll():
        tv.delete(*tv.get_children())
        sql="SELECT * from employees_details where Employee_Id=%s"
        val=(txtemployee_iD.get(),)
        mycursor.execute(sql,val)
        rows=mycursor.fetchall()
        if txtemployee_iD.get()=="" or rows==[]:
            messagebox.showerror("Error Input","Give valid Employee ID")
            root.destroy()
            onedetailview_frame()
        else:                
            password=f"{txtemployee_iD.get()}"
            if entrypassword.get()==password:
                for i in rows:
                    tv.insert("", END, values=i)
            else:
                messagebox.showerror("Input error","Please enter correct password")
                root.destroy()
                onedetailview_frame()
  
    btnview=Button(onedetail_frame, command=displayAll ,text="View",width=12, font=("Microsoft YaHei UI light", 12,"bold"), bg="red", fg="white",bd=3)
    btnview.grid(row=2,column=2,padx=10,pady=10)


frontpage_frame()
