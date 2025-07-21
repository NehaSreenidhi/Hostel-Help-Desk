from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

class dataBase:

    def __init__(self):

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect("hostelDeskDB.db")
        self.cursor = self.conn.cursor()

        # Table for person details
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Person( 
                id TEXT PRIMARY KEY,
                pwd TEXT NOT NULL,
                designation TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        # Table for problem details
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Problem (
                name TEXT NOT NULL, 
                regdNo PRIMARY KEY  NOT NULL, 
                hostelName TEXT NOT NULL, 
                roomNo TEXT NOT NULL, 
                probDescription TEXT NOT NULL,
                problem_type TEXT NOT NULL, 
                status TEXT NOT NULL
                )
        ''')
        self.conn.commit()

    # Create person entry
    def create_person(self, id, pwd, designation):
        self.cursor.execute("INSERT INTO Person (id,pwd,designation) VALUES (?, ?, ?)", (id, pwd, designation))
        self.conn.commit()

    # Create Problem entry
    def create_problem(self, name, regdNo, hostelName, roomNo, probDescription, problem_type, status):
        self.cursor.execute("INSERT INTO Problem (regdNo,name,hostelName,roomNo,probDescription, problem_type, status) VALUES (?, ?, ?, ?, ?, ?, ?)",(regdNo, name, hostelName, roomNo, probDescription, problem_type, status))
        self.conn.commit()

    def get_person(self,id):
        self.cursor.execute("SELECT * FROM Person WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def fetch_pending_record(self):
        self.cursor.execute("SELECT * FROM Problem WHERE status = 'Pending'")
        data=self.cursor.fetchall()
        return data

    def fetch_completed_record(self):
        self.cursor.execute("SELECT * FROM Problem WHERE status = 'Completed'")
        data=self.cursor.fetchall()
        return data

    def get_problem(self):
        self.cursor.execute("SELECT * FROM Problem")
        return self.cursor.fetchall()

    def update_record(self, regdNo, status):
        sql = """
                update Problem set status = ? WHERE regdNo = ?        
            """
        self.cursor.execute(sql, (status, regdNo))
        self.conn.commit()

class main_page:
    def __init__(self, root):

        self.root = root
        self.db = dataBase()
        
        self.bg_img = Image.open('images/logo.png')
        self.bg_img = self.bg_img.resize((650,450))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.bg_lbl = Label(root, image= self.bg_img)
        self.bg_lbl.place(x = 0, y = 0)
        
        self.header = Label(root, text = "Hostel Help Desk",width=27,height=-1, fg = "white", bg = "DodgerBlue", font = ("Times New Roman", 30, 'bold'))
        self.header.place(x=1,y=1)
        self.side_header1 = Label(root, text = "Admin", fg = "white", bg = "DodgerBlue", font = ("Times New Roman", 20, 'bold'))
        self.side_header1.place(x = 80, y = 130)
        self.side_header2 = Label(root, text = "Student", fg = "white", bg = "DodgerBlue", font = ("Times New Roman", 20, 'bold'))
        self.side_header2.place(x = 480, y = 130)
        
        self.nameA = Label(root, text = "   UserID  ", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.nameA.place(x = 20, y = 225)
        self.pwdA = Label(root, text = "Password", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.pwdA.place(x = 20, y = 265)
        
        self.nameB = Label(root, text = "  UserID  ", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.nameB.place(x = 410, y = 220)
        self.pwdB = Label(root, text = "Password", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.pwdB.place(x = 410, y = 260)
        
        self.eAA = Entry(root, bd = 3)
        self.eAA.place(x = 115, y = 228)  
        self.eAB = Entry(root, bd = 3, show="*")
        self.eAB.place(x = 115, y = 268)  
        
        self.eBA = Entry(root, bd = 3)
        self.eBA.place(x = 495, y = 222)  
        self.eBB = Entry(root, bd = 3, show="*")
        self.eBB.place(x = 495, y = 262)
        
        self.login_btnA = Button(root, text = 'Login', bg = 'green3', font=('Times New Roman', 10, 'bold'), command= self.validate_admin)
        self.login_btnA.place(x= 80, y = 320)

        self.Register_btnA = Button(root, text = 'Register', bg = 'green3', font=('Times New Roman', 10, 'bold'),command= self.sign_up_admin)
        self.Register_btnA.place(x= 130, y = 320)

        self.login_btnB = Button(root, text = 'Login', bg = 'green3', font=('Times New Roman', 10, 'bold'), command= self.validate_student)
        self.login_btnB.place(x= 480, y = 320)

        self.Register_btnB = Button(root, text = 'Register', bg = 'green3', font=('Times New Roman', 10, 'bold'), command= self.sign_up_student)
        self.Register_btnB.place(x= 530, y = 320)


    def sign_up_admin(self):
        self.side_header1.destroy()
        self.side_header2.destroy()
        self.nameA.destroy()
        self.pwdA.destroy()
        self.nameB.destroy()
        self.pwdB.destroy()
        self.eAA.destroy()
        self.eAB.destroy()
        self.eBA.destroy()
        self.eBB.destroy()
        self.login_btnA.destroy()
        self.login_btnB.destroy()
        self.Register_btnA.destroy()
        self.Register_btnB.destroy()

        # sign up details
        self.sign_up_admin_label = Label(root, text = "Admin Sign Up", fg = "white", bg = "orange", font = ("Times New Roman", 14, 'bold'))
        self.sign_up_admin_label.place(x =230, y = 120)
        self.sign_up_name = Label(root, text = "   UserID  ", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.sign_up_name.place(x = 120, y = 225)
        self.sign_up_pwd = Label(root, text = "Password", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.sign_up_pwd.place(x = 120, y = 265)
        self.signup_admin_id = Entry(root, bd = 3)
        self.signup_admin_id.place(x = 300, y = 228)
        self.signup_admin_pwd = Entry(root, bd = 3, show="*")
        self.signup_admin_pwd.place(x = 300, y = 268)
        self.sign_up_Now=Button(root, text = 'Sign Up Now!!', bg = 'green3', font=('Times New Roman', 10,'bold'), command=self.store_admin)
        self.sign_up_Now.place(x= 460, y = 400)
        self.sign_up_admin_back=Button(root, text = 'Back', bg = 'green3', font=('Times New Roman', 10,'bold'),command=self.bck_sign_up_admin)
        self.sign_up_admin_back.place(x= 120, y = 400)

    def sign_up_student(self):
        self.side_header1.destroy()
        self.side_header2.destroy()
        self.nameA.destroy()
        self.pwdA.destroy()
        self.nameB.destroy()
        self.pwdB.destroy()
        self.eAA.destroy()
        self.eAB.destroy()
        self.eBA.destroy()
        self.eBB.destroy()
        self.login_btnA.destroy()
        self.login_btnB.destroy()
        self.Register_btnA.destroy()
        self.Register_btnB.destroy()

        # sign up details
        self.sign_up_student_label = Label(root, text = "Student Sign Up", fg = "white", bg = "orange", font = ("Times New Roman", 14, 'bold'))
        self.sign_up_student_label.place(x =230, y = 120)
        self.sign_up_name = Label(root, text = "   UserID  ", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.sign_up_name.place(x = 120, y = 225)
        self.sign_up_pwd = Label(root, text = "Password", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.sign_up_pwd.place(x = 120, y = 265)
        self.signup_std_id = Entry(root, bd = 3)
        self.signup_std_id.place(x = 300, y = 228)
        self.signup_std_pwd = Entry(root, bd = 3, show="*")
        self.signup_std_pwd.place(x = 300, y = 268)
        self.sign_up_Now=Button(root, text = 'Sign Up Now!!', bg = 'green3', font=('Times New Roman', 10,'bold'), command=self.store_student)
        self.sign_up_Now.place(x= 460, y = 400)
        self.sign_up_student_back=Button(root, text = 'Back', bg = 'green3', font=('Times New Roman', 10,'bold'),command=self.bck_sign_up_student)
        self.sign_up_student_back.place(x= 120, y = 400)

    def bck_sign_up_admin(self):
        self.sign_up_admin_label.destroy()
        self.sign_up_name.destroy()
        self.signup_admin_id.destroy()
        self.signup_admin_pwd.destroy()
        self.sign_up_pwd.destroy()
        self.sign_up_Now.destroy()
        self.sign_up_admin_back.destroy()
        
        main = main_page(root)

    def bck_sign_up_student(self):
        self.sign_up_student_label.destroy()
        self.sign_up_name.destroy()
        self.signup_std_id.destroy()
        self.signup_std_pwd.destroy()
        self.sign_up_pwd.destroy()
        self.sign_up_Now.destroy()
        self.sign_up_student_back.destroy()
        
        main = main_page(root)


    def admin_page(self):
        
        root = self.root
        
        self.header.destroy()
        self.side_header1.destroy()
        self.side_header2.destroy()
        self.eAA.destroy()
        self.eBB.destroy()
        self.eAB.destroy()
        self.eBA.destroy()
        self.nameA.destroy()
        self.pwdA.destroy()
        self.nameB.destroy()
        self.pwdB.destroy()
        self.login_btnA.destroy()
        self.login_btnB.destroy()
        self.Register_btnA.destroy()
        self.Register_btnB.destroy()
        
        self.label = Label(root, text = "ADMIN DETAILS",font = ('Times New Roman',20,'bold'),bg = "DodgerBlue")
        self.label.place(x=220,y=50)
        
        self.bg_img1 = Image.open('images/pending.jpg')
        self.bg_img1 = self.bg_img1.resize((125,125))
        self.bg_img1 = ImageTk.PhotoImage(self.bg_img1)
        
        self.label1 = Label(root, image = self.bg_img1,bd = '5',bg = 'black')
        self.label1.place(x=130,y=150)
        
        self.pend_but = Button(root,text = "Pending",height = 2,width = 12, command= self.pending)
        self.pend_but.place(x=147,y=315)
        
        self.bg_img2 = Image.open('images/completed.jpg')
        self.bg_img2 = self.bg_img2.resize((125,125))
        self.bg_img2 = ImageTk.PhotoImage(self.bg_img2)
        
        self.label2 = Label(root, image = self.bg_img2,bd = '5',bg = 'black')
        self.label2.place(x=380,y=150)
        
        self.comp_but = Button(root,text = "Completed",height = 2,width = 12, command= self.completed)
        self.comp_but.place(x=400,y=315)  
        
        self.bck_admin_page = Button(root, text = 'BACK', font=('Courier New', 15,'bold'), bd = 4, width= 6, command= self.back_to_homeB)
        self.bck_admin_page.place(x = 500, y = 400)
          
    def student_page(self):
        
        root = self.root
        self.header.destroy()
        self.side_header1.destroy()
        self.side_header2.destroy()
        self.eAA.destroy()
        self.eBB.destroy()
        self.eAB.destroy()
        self.eBA.destroy()
        self.nameA.destroy()
        self.pwdA.destroy()
        self.nameB.destroy()
        self.pwdB.destroy()
        self.login_btnA.destroy()
        self.login_btnB.destroy()
        self.Register_btnA.destroy()
        self.Register_btnB.destroy()
        
        self.home_title = Label(root, text= 'Student DashBoard', font = ('Times New Roman', 15, 'bold'))
        self.home_title.pack(fill = 'x')

        self.sd2 = Label(root, text = "User_name : "+self.id, fg = "black", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.sd2.pack(side = TOP, pady=2)
        
        self.icon1=Image.open("images/health.jpg")
        self.icon1=self.icon1.resize((125,125))
        self.icon1=ImageTk.PhotoImage(self.icon1)
        self.icon_lbl=Label(root,image=self.icon1,bd='5',bg='black')
        self.icon_lbl.place(x=130,y=150)
        
        self.st_butA=Button(root,text='Health Issues',height=2,width=12, font = ("Times New Roman", 12, 'bold'), command = self.health_complaints)
        self.st_butA.place(x='147',y='315')
        
        self.icon2=Image.open("images/repairs.jpg")
        self.icon2=self.icon2.resize((125,125))
        self.icon2=ImageTk.PhotoImage(self.icon2)
        self.icon_lb2=Label(root,image=self.icon2,bd='5',bg='black')
        self.icon_lb2.place(x=380,y=150)
        
        self.st_butB=Button(root,text='Repairs',height=2,width=12, font = ("Times New Roman", 12, 'bold'), command = self.repair_complaints)
        self.st_butB.place(x='400',y='315')
        
        self.bck_student_page = Button(root, text = 'BACK', font=('Courier New', 15,'bold'), bd = 4, width= 6, command= self.back_to_homeA)
        self.bck_student_page.place(x = 500, y = 405)
        
    def health_complaints(self):
        self.home_title.destroy()
        self.icon_lbl.destroy()
        self.st_butA.destroy()
        self.icon_lb2.destroy()
        self.st_butB.destroy()
        self.sd2.destroy()
        
        
        self.l1=Label(root,text="HEALTH PROBLEM DETAILS",bg="DodgerBlue2",fg="white",font=("Arial Bold",15),borderwidth=1,relief="solid")
        self.l1.pack(fill='x')
        
        self.l2=Label(root,text="Student Name:",borderwidth=1,relief="solid")
        self.l2.place(x=10,y=60,width=120)
        
        self.e1=Entry(root)
        self.e1.place(x=150,y=60,width=250)
        
        self.l3=Label(root,text="Regd No:",borderwidth=1,relief="solid")
        self.l3.place(x=10,y=100,width=120)
        
        self.e2=Entry(root)
        self.e2.place(x=150,y=100,width=150)
        
        self.l4=Label(root,text="Hostel Name:",borderwidth=1,relief="solid")
        self.l4.place(x=10,y=140,width=120)
        
        self.e3=Entry(root)
        self.e3.place(x=150,y=140,width=250)

        self.l5=Label(root,text="Room No:",borderwidth=1,relief="solid")
        self.l5.place(x=10,y=180,width=120)

        self.e4=Entry(root)
        self.e4.place(x=150,y=180,width=120)
        
        self.l6=Label(root,text="Problem Description:",borderwidth=1,relief="solid")
        self.l6.place(x=10,y=220,width=150)
        
        self.e5=Text(root)
        self.e5.place(x=10,y=240,height=120,width=450)

        
        def clicked():
            self.db.create_problem(self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get(),self.e5.get("1.0","end-1c"),"HEALTH","Pending")
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)
            self.e4.delete(0,END)
            self.e5.delete(1.0,END)
            messagebox.showinfo('Saved','Problem Details saved!')
            
        self.bn = Button(root,text = "Submit",bg = "DodgerBlue2",command = clicked)
        self.bn.place(x=225,y=350)
        
        self.bck_complaints = Button(root, text = 'BACK', font = ('Courier New', 15,'bold'), bd = 4, width = 6, command = self.back_to_student_page)
        self.bck_complaints.place(x = 500, y = 405)

    def repair_complaints(self):
        self.home_title.destroy()
        self.icon_lbl.destroy()
        self.st_butA.destroy()
        self.icon_lb2.destroy()
        self.st_butB.destroy()
        self.sd2.destroy()

        self.l1 = Label(root, text="REPAIR PROBLEM DETAILS", bg="DodgerBlue2", fg="white", font=("Arial Bold", 15),
                        borderwidth=1, relief="solid")
        self.l1.pack(fill='x')

        self.l2 = Label(root, text="Student Name:", borderwidth=1, relief="solid")
        self.l2.place(x=10, y=60, width=120)

        self.e1 = Entry(root)
        self.e1.place(x=150, y=60, width=250)

        self.l3 = Label(root, text="Regd No:", borderwidth=1, relief="solid")
        self.l3.place(x=10, y=100, width=120)

        self.e2 = Entry(root)
        self.e2.place(x=150, y=100, width=150)

        self.l4 = Label(root, text="Hostel Name:", borderwidth=1, relief="solid")
        self.l4.place(x=10, y=140, width=120)

        self.e3 = Entry(root)
        self.e3.place(x=150, y=140, width=250)

        self.l5 = Label(root, text="Room No:", borderwidth=1, relief="solid")
        self.l5.place(x=10, y=180, width=120)

        self.e4 = Entry(root)
        self.e4.place(x=150, y=180, width=120)

        self.l6 = Label(root, text="Problem Description:", borderwidth=1, relief="solid")
        self.l6.place(x=10, y=220, width=150)

        self.e5 = Text(root)
        self.e5.place(x=10, y=240, height=120, width=450)

        def clicked():
            self.db.create_problem(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(),
                                    self.e5.get("1.0", "end-1c"), "REPAIR", "Pending")
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)
            self.e4.delete(0,END)
            self.e5.delete(1.0,END)
            messagebox.showinfo('Saved', 'Problem Details saved!')

        self.bn = Button(root, text="Submit", bg="DodgerBlue2", command=clicked)
        self.bn.place(x=225, y=350)

        self.bck_complaints = Button(root, text='BACK', font=('Courier New', 15, 'bold'), bd=4, width=6,
                                        command=self.back_to_student_page)
        self.bck_complaints.place(x=500, y=405)

    
    def back_to_student_page(self):
        self.e1.destroy()
        self.e2.destroy()
        self.e3.destroy()
        self.e4.destroy()
        self.e5.destroy()
        self.l1.destroy()
        self.l2.destroy()
        self.l3.destroy()
        self.l4.destroy()
        self.l5.destroy()
        self.l6.destroy()
        self.bn.destroy()
        self.bck_complaints.destroy()
        self.student_page()
        
    def back_to_homeB(self):
        
        self.label.destroy()
        self.label1.destroy()
        self.pend_but.destroy()
        self.label2.destroy()
        self.comp_but.destroy()
        
        
        self.bck_admin_page.destroy()
        
        main = main_page(root)
            
    def back_to_homeA(self):
        
        self.home_title.destroy()
        self.sd2.destroy()
        # self.icon1.destroy()
        self.icon_lbl.destroy()
        self.st_butA.destroy()
        # self.icon2.destroy()
        self.icon_lb2.destroy()
        self.st_butB.destroy()
        
        self.bck_student_page.destroy()
        
        main = main_page(root)

    def back_to_admin_page_pending(self):
        self.bck_pending.destroy()
        self.admin_page()
        
    def back_to_admin_page_completed(self):
        self.bck_completed.destroy()
        self.admin_page()
        
    def pending(self):
        
        self.label.destroy()
        self.label1.destroy()
        self.pend_but.destroy()
        self.label2.destroy()
        self.comp_but.destroy()
        self.bck_admin_page.destroy()

        self.regd_label = Label(root, text="Regd No:", borderwidth=1, relief="solid")
        self.regd_label.place(x=10, y=40, width=80)
        self.regd_entry = Entry(root)
        self.regd_entry.place(x=150, y=40, width=250)
        self.cbn = Button(root, text='Completed', font=('Courier New', 15,'bold'),bd = 2,width =10, command=self.task_completed)
        self.cbn.place(x=450, y=25)

        self.Myframe = Frame(root)
        self.Myframe.place(x=0, y=65, width=650, height=600)

        self.pending_heading = Label(root, text="Pending complaints ", bg="DodgerBlue2", fg="white",
                                     font=("Arial Bold", 15), borderwidth=1, relief="solid")
        self.pending_heading.pack(fill='x')

        self.style = ttk.Style()
        self.style.configure("Treeview", font=("times", 12), rowheight=20, rowwidth=6)
        self.style.configure("Treeview.Heading", font=("times", 10, "bold"))
        self.table = ttk.Treeview(self.Myframe, columns=(0, 1, 2, 3, 4, 5, 6, 7))
        self.table.heading("0", text="S.No", )
        self.table.column("0", minwidth=0, width=18)
        self.table.heading("1", text="Student Name")
        self.table.column("1", minwidth=0, width=75)
        self.table.heading("2", text="Regd.No")
        self.table.column("2", minwidth=0, width=65)
        self.table.heading("3", text="Hostel Name")
        self.table.column("3", minwidth=0, width=60)
        self.table.heading("4", text="Room No")
        self.table.column("4", minwidth=0, width=30)
        self.table.heading("5", text="Problem Description")
        self.table.column("5", minwidth=0, width=90)
        self.table.heading("6", text="Issue")
        self.table.column("6", minwidth=0, width=40)
        self.table.heading("7", text="Status")
        self.table.column("7", minwidth=0, width=40)
        self.table["show"] = 'headings'
        self.table.pack(fill=X)

        self.fetchData()

    def fetchData(self):
        self.table.delete(*self.table.get_children())
        self.count = 0
        for row in self.db.fetch_pending_record():
            self.count += 1
            self.table.insert("", END, values=(self.count, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.bck_pending = Button(root, text='BACK', font=('Courier New', 15, 'bold'), bd=4, width=6,
                                  command=self.back_to_admin_page_pending)
        self.bck_pending.place(x=500, y=405)

    def task_completed(self):
        self.db.update_record(self.regd_entry.get(), "Completed")
        self.fetchData()

    def back_to_admin_page_pending(self):
        self.regd_label.destroy()
        self.regd_entry.destroy()
        self.pending_heading.destroy()
        self.cbn.destroy()
        self.table.destroy()
        self.bck_pending.destroy()
        self.admin_page()
    def clicked_completed(self):
        if(self.regd_entry.get()):
            self.db.update_prob_status(self.regd_entry.get())
        else: 
            pass
        
    def completed(self):
        
        self.label.destroy()
        self.label1.destroy()
        self.pend_but.destroy()
        self.label2.destroy()
        self.comp_but.destroy()
        self.bck_admin_page.destroy()

        self.Myframe = Frame(root)
        self.Myframe.place(x=0, y=65, width=650, height=600)

        self.completed_heading = Label(root, text="Completed complaints ", bg="DodgerBlue2", fg="white",
                                       font=("Arial Bold", 15), borderwidth=1, relief="solid")
        self.completed_heading.pack(fill='x')

        self.style = ttk.Style()
        self.style.configure("Treeview", font=("times", 12), rowheight=20, rowwidth=6)
        self.style.configure("Treeview.Heading", font=("times", 10, "bold"))
        self.table = ttk.Treeview(self.Myframe, columns=(0, 1, 2, 3, 4, 5, 6, 7))
        self.table.heading("0", text="S.No", )
        self.table.column("0", minwidth=0, width=18)
        self.table.heading("1", text="Student Name:")
        self.table.column("1", minwidth=0, width=75)
        self.table.heading("2", text="Regd.No")
        self.table.column("2", minwidth=0, width=65)
        self.table.heading("3", text="Hostel Name")
        self.table.column("3", minwidth=0, width=60)
        self.table.heading("4", text="Room No")
        self.table.column("4", minwidth=0, width=30)
        self.table.heading("5", text="Problem Description")
        self.table.column("5", minwidth=0, width=90)
        self.table.heading("6", text="Issue")
        self.table.column("6", minwidth=0, width=40)
        self.table.heading("7", text="Status")
        self.table.column("7", minwidth=0, width=40)
        self.table["show"] = 'headings'
        # self.table.bind("<ButtonRelease-1>",self.getregd)
        self.table.pack(fill=X)

        self.fetchCompletedData()

    def back_to_admin_page_completed(self):
        self.table.destroy()
        self.completed_heading.destroy()
        self.bck_completed.destroy()
        self.admin_page()

    def fetchCompletedData(self):
        self.table.delete(*self.table.get_children())
        self.count = 0
        for row in self.db.fetch_completed_record():
            self.count += 1
            self.table.insert("", END, values=(self.count, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        self.bck_completed = Button(root, text='BACK', font=('Courier New', 15, 'bold'), bd=4, width=6,
                                    command=self.back_to_admin_page_completed)
        self.bck_completed.place(x=500, y=405)


    def validate_admin(self):
        id = self.eAA.get()
        pwd = self.eAB.get()
        # validating
        t = self.db.get_person(id)
        if (t):
            if(t[2] == 'admin'):
                if( t[1] == pwd ):
                    messagebox.showinfo('Admin Signed ', 'Admin Signed In')
                    self.admin_page()
                else:
                    messagebox.showinfo('Wrong Password', 'Admin not Signed In')
            else:
                messagebox.showerror('Invalid admin', 'Student cannot sign into admin')
        else:
            messagebox.showinfo('Wrong entry ', 'Admin not Signed In')

    def validate_student(self):
        self.id = self.eBA.get()
        pwd = self.eBB.get()
        # validating
        t = self.db.get_person(self.id)
        if( t ):
            if(t[2] == 'student'):
                if ( t[1] == pwd ):
                    messagebox.showinfo('Student Signed ', 'Student Signed In')
                    self.student_page()
                else:
                    messagebox.showinfo('Wrong Password ', 'Student not Signed In')
            else:
                messagebox.showerror('Invalid student', 'Admin cannot sign into student')
        else:
            messagebox.showinfo('Wrong entry ', 'Student not Signed In')


    def store_admin(self):
        a_id = self.signup_admin_id.get()
        a_pwd = self.signup_admin_pwd.get()
        self.db.create_person(a_id, a_pwd, "admin")
        self.signup_admin_id.delete(0,END)
        self.signup_admin_pwd.delete(0,END)
        messagebox.showinfo('Signed Up', 'Successfully signed in')

    def store_student(self):
        s_id = self.signup_std_id.get()
        s_pwd = self.signup_std_pwd.get()
        self.db.create_person(s_id, s_pwd, "student")
        self.signup_std_id.delete(0,END)
        self.signup_std_pwd.delete(0,END)
        messagebox.showinfo('Signed Up', 'Successfully signed in')

        
root = Tk()
root.geometry("650x450+500+100")
root.configure(bg = 'grey')
root.title("Hostel Help Desk")

main = main_page(root)
root.mainloop()
