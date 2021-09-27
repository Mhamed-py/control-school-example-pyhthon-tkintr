from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
import pymysql
from tkinter import messagebox


#----------------pro.interface-------------
class student:
    def __init__(self, pro):
        self.pro=pro
        self.pro.geometry('1350x690+1+1')
        self.pro.configure(background='silver')
        self.pro.title('برنامج اداره المدارس')
        self.pro.resizable(False,False)
        self.pro.iconbitmap("C:\\Users\\mostafa\\Desktop\\control schools\\i.ico")
        title=Label(self.pro,
        text='[نظام تسجيل الطلاب]', bg='#C0392B',font=('monospace',14),fg='white')
        title.pack(fill=X)
         #---------------variable-------------------
        self.address_var=StringVar()
        self.id_var= StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.phone_var=StringVar()
        self.certi_var=StringVar()
        self.gender_var=StringVar()
        self.se_by=StringVar()
        self.se_var=StringVar()
        self.dell_var=StringVar()
        
        #----------------pro.mange-------------------
        mange_frame=Frame(self.pro,bg='white')
        mange_frame.place(x=1140,y=29,width='210',height='365')
        lbl_id=Label(mange_frame,text='الرقم التسلسلي',bg='white')
        lbl_id.pack()
        ent_id=Entry(mange_frame,textvariable=self.id_var,bd='2',justify='center')
        ent_id.pack()
        #---------------student name,num---------------
        lbl_name=Label(mange_frame,text='اسم الطالب',bg='white')
        lbl_name.pack()
        ent_name=Entry(mange_frame,textvariable=self.name_var,bd='2',justify='center')
        ent_name.pack()
        #---------------student email-----------------
        lbl_email=Label(mange_frame,text='ايميل الطالب ',bg='white')
        lbl_email.pack()
        ent_email=Entry(mange_frame,textvariable=self.email_var,bd='2',justify='center')
        ent_email.pack()
        #---------------student phone-----------------
        lbl_phone=Label(mange_frame,text=' رقم الهاتف',bg='white')
        lbl_phone.pack()
        ent_phone=Entry(mange_frame,textvariable=self.phone_var,bd='2',justify='center')
        ent_phone.pack()

        lbl_achiv=Label(mange_frame,text='مؤهل الطالب ',bg='white')
        lbl_achiv.pack()
        ent_achiv=Entry(mange_frame,textvariable=self.certi_var,bd='2',justify='center')
        ent_achiv.pack()
        #---------------student gender-----------------
        lbl_gen=Label(mange_frame,text='اختر جنس الطالب',bg='white')
        lbl_gen.pack()
        sel_gen=ttk.Combobox(mange_frame,textvariable=self.gender_var,width=17)
        sel_gen['value']=("ذكر","انثي")
        sel_gen.pack()

        #---------------student adress-----------------
        lbl_address=Label(mange_frame,text='عنوان الطالب',bg='white')
        lbl_address.pack()
        ent_address=Entry(mange_frame,textvariable=self.address_var,bd='2',justify='center')
        ent_address.pack()
        #--------------- delete student-----------------
        lbl_delet=Label(mange_frame,text=' ازاله طالب بالاسم [x]',bg='white',fg='red')
        lbl_delet.pack()
        ent_delet=Entry(mange_frame,textvariable=self.dell_var,bd='2',justify='center')
        ent_delet.pack()

        #---------------  mange frame2 -----------------
        mange_frame2=Frame(self.pro,bg='white')
        mange_frame2.place(x=1140,y=399,width='210',height='600')
        #---------------- control buttons --------------
        lbl_control=Label(mange_frame2,text='لوحه التحكم',bg='#C0392B',font=15)
        lbl_control.pack(fill=X)

        b1=Button(mange_frame2,text='اضافه طالب ',bd='2',bg='#AEB6BF',command=self.add_student)
        b1.place(x=33,y=50,width=150,height=30)

        b2=Button(mange_frame2,text='حذف طالب',bd='2',bg='#AEB6BF',command=self.delete)
        b2.place(x=33,y=83,width=150,height=30)

        b3=Button(mange_frame2,text='تعديل بيانات طالب',bd='2',bg='#AEB6BF',command=self.update)
        b3.place(x=33,y=116,width=150,height=30)

        b4=Button(mange_frame2,text='افراغ الحقول',bd='2',bg='#AEB6BF',command=self.clear)
        b4.place(x=33,y=149,width=150,height=30)

        b5=Button(mange_frame2,text='!من نحن',bd='2',bg='#AEB6BF',command=self.about)
        b5.place(x=33,y=182,width=150,height=30)

        b6=Button(mange_frame2,text='اغلاق البرنامج',bd='2',bg='#AEB6BF',command=pro.quit)
        b6.place(x=33,y=215,width=150,height=30)

        #--------------- search mange frame3------------------
        
        mange_frame3=Frame(self.pro,bg='white',width='1137',height='50')
        mange_frame3.place(x=0,y=30)
        
        lbl_search=Label(mange_frame3,text='البحث عن طالب',bg='white',font=('bold',12))
        lbl_search.place(x=1050,y=7)
        combo_search=ttk.Combobox(mange_frame3,justify='right')
        combo_search['value']=('name','phone','email')
        combo_search.place(x=900,y=7)

        en_search=Entry(mange_frame3,textvariable=self.se_var,justify='right',bd='2')
        en_search.place(x=770,y=7)

        bt_search=Button(mange_frame3,text='بحث',height='1',width='6',bg='white',command=self.search)
        bt_search.place(x=710,y=3)
        #--------------- detalias--------------
        detail_frame=Frame(self.pro)
        detail_frame.place(x=0,y=81,height=610,width=1137)
        scroll_x=Scrollbar(detail_frame,orient=HORIZONTAL,bg='white')
        scroll_y=Scrollbar(detail_frame,orient=VERTICAL)
        
        #--------------- treeveiw----------------
        self.student_table=ttk.Treeview(detail_frame,columns=('address','gender','certi','email','phone','name','id'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set ) 
        self.student_table.place(x=18,y=1,height=592,width=1134)      
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table['show']='headings'
        self.student_table.heading('address',text='عنوان الطالب')
        self.student_table.heading('gender',text='الجنس')
        self.student_table.heading('certi',text='المؤهل')
        self.student_table.heading('email',text='البريد الالكتروني')
        self.student_table.heading('phone',text='رقم الهاتف')
        self.student_table.heading('name',text='اسم الطالب ')
        self.student_table.heading('id',text='الرقم التسلسلي')
        self.student_table.column('address',width=130)
        self.student_table.column('gender',width=30)
        self.student_table.column('certi',width=65)
        self.student_table.column('email',width=70)
        self.student_table.column('phone',width=65)
        self.student_table.column('name',width=100)
        self.student_table.column('id',width=20)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursore)
        
        
        
        
        
        
        
        
        
        
        
        
   #-----con+add----------
        self.fectch_all()
    def add_student(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stud')
        cur=con.cursor()
        cur.execute("insert into student value(%s,%s,%s,%s,%s,%s,%s)",(


                                                            self.address_var.get(),
                                                            self.gender_var.get(),
                                                            self.certi_var.get(),
                                                            self.email_var.get(),
                                                            self.phone_var.get(),
                                                            self.name_var.get(),
                                                            self.id_var.get(),
                                                            




                                                              ))
        con.commit()
        self.fectch_all()
        self.clear()
        con.close()

    def fectch_all(self):
        con= pymysql.connect(host='localhost',user='root',password='',database='stud')
        cur=con.cursor()
        cur.execute('select * from student')
        rows=cur.fetchall()
        if len(rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,value=row)
            con.commit()
        con.close()  


    def delete (self):
                  con= pymysql.connect(host='localhost',user='root',password='',database='stud')
                  cur=con.cursor()
                  cur.execute('delete from student where name=%s',self.dell_var.get())
                  con.commit()
                  self.fectch_all()
                  con.close()
    
    
    
    def clear(self):
                  
                  self.address_var.set('')
                  self.gender_var.set('')
                  self.certi_var.set('')
                  self.email_var.set('')
                  self.phone_var.set('')
                  self.name_var.set('')
                  self.id_var.set('')
    def get_cursore(self,ev):
        cursour_row=self.student_table.focus()
        content=self.student_table.item(cursour_row)
        row=content['values']
        self.address_var.set(row[0])
        self.gender_var.set(row[1])
        self.certi_var.set(row[2])
        self.email_var.set(row[3])
        self.phone_var.set(row[4])
        self.name_var.set(row[5])
        self.id_var.set(row[6])
    def update(self):
          con=pymysql.connect(host='localhost',user='root',password='',database='stud')
          cur=con.cursor()
          cur.execute("update student set address=%s,gender=%s,certi=%s,email=%s,phone=%s,name=%swhere id=%s",(


                                                            self.address_var.get(),
                                                            self.gender_var.get(),
                                                            self.certi_var.get(),
                                                            self.email_var.get(),
                                                            self.phone_var.get(),
                                                            self.name_var.get(),
                                                            self.id_var.get(),
                                                            




                                                              ))
          con.commit()
          self.fectch_all()
          self.clear()
          con.close()  




    def search (self):
        con= pymysql.connect(host='localhost',user='root',password='',database='stud')
        cur=con.cursor()
        cur.execute("select * from student where "+
        str(self.se_by.get())+" LIKE '%"+str(self.se_var.get())+"%'")
        
        
        
        rows=cur.fetchall()
        if len(rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,value=row)
            con.commit()
        con.close() 



    def about(self):
        messagebox.showinfo("Prepared by Mohamed Hamed ")
        messagebox.showinfo("Whatsapp","+201553791576")








pro=Tk()
ob1=student(pro)
pro.mainloop()
