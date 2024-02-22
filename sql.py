from tkinter import *
from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,declarative_base
from tkinter import ttk
from tkinter import messagebox

engine=create_engine("sqlite:///tkoop.db",echo=True)
Base=declarative_base()
sessions=sessionmaker(bind=engine)

session=sessions()



class Employee(Base):
    __tablename__="Employee"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    salary=Column(Integer)
    lastname=Column(String)

    def __init__(self,name,age,salary,lastname):
        self.name=name
        self.age = age
        self.salary=salary
        self.lastname=lastname



Base.metadata.create_all(engine)

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWiget()

    def createWiget(self):
####################################################################################
        self.txtname=Entry(self.master)
        self.txtname.place(x=50,y=50)
        self.namelbl=Label(self.master,text="name")
        self.namelbl.place(x=10,y=50)
        self.namevar = StringVar()
        self.lastnamevar = StringVar()
        self.agevar = StringVar()
        self.salaryvar = StringVar()
####################################################################################
        self.txtlastname=Entry(self.master)
        self.txtlastname.place(x=80,y=90)
        self.lastnamelbl=Label(self.master,text="lastname")
        self.lastnamelbl.place(x=10,y=90)
####################################################################################
        self.txtage=Entry(self.master)
        self.txtage.place(x=50,y=130)
        self.agelbl=Label(self.master,text="age")
        self.agelbl.place(x=10,y=130)
####################################################################################
        self.txtsalary=Entry(self.master)
        self.txtsalary.place(x=50,y=160)
        self.salarylbl=Label(self.master,text="salary")
        self.salarylbl.place(x=10,y=160)
####################################################################################
        self.btn=Button(self.master,text="register",command=self.OnclickRegister)
        self.btn.place(x=50,y=190)
####################################################################################
        self.btn=Button(self.master,text="delete")
        self.btn.place(x=130,y=190)
####################################################################################
        self.Table=ttk.Treeview(self.master,columns=("name","age","salary","lastname"),show="headings")
        self.Table.column("name",width=80)
        self.Table.heading("name",text="name")
        self.Table.column("age",width=80)
        self.Table.heading("age",text="age")
        self.Table.column("salary",width=80)
        self.Table.heading("salary",text="Salary")
        self.Table.column("lastname",width=80)
        self.Table.heading("lastname",text="lastname")
        self.Table.bind("<Button-1>",self.getSelection)
        self.Table.pack(side="right",fill=BOTH)
####################################################################################
        self.btn = Button(self.master, text="Update",command=self.onclickupdate)
        self.btn.place(x=50, y=220)
####################################################################################

####################################################################################
    def OnclickRegister(self):
        employee1=Employee(name=self.txtname.get(),age=self.txtage.get(),salary=self.txtsalary.get(),lastname=self.txtlastname.get())
        self.Register(employee1)
        self.load_and_clear()
        messagebox.showinfo("added to database","Registered Successfully")

####################################################################################
    def load_and_clear(self):
        for item in self.Table.get_children():
            sel=str(item)
            self.Table.delete(sel)
        data=session.query(Employee).all()
        for item in data:
            self.Table.insert("","end",values=([item.name,item.age,item.salary,item.lastname]))

####################################################################################
    def Register(self,value):
        session.add(value)
        session.commit()
####################################################################################
    def onclickupdate(self):
        selected=self.Table.selection()
        if selected!=():
            select=self.Table.item(selected)["values"]
            dic={"name":select[0],"lastname":select[3],"age":int(select[2]),"salary":int(select[1])}
            index=self.update(dic)
            p = id[index]
            self.Table.item(selected, values=[p["name"], p["lastname"], p["salary"], p["age"]])
####################################################################################
    def update(self):
        index1 = id.index1()
        id[index1] = {"name": self.txtname.get(), "lastname":self.txtlastname.get(), "age": int(self.txtage.get()),
                       "salary":self.txtsalary.get()}
        return index1
####################################################################################

    def getSelection(self, e):
        sec = self.table.selection()
        if sec != ():
            id = self.table.item(sec)["values"][0]
            data = self.getElementByID(id)
            self.namevar.set(data.name)
            self.lastnamevar.set(data.lastname)
            self.agevar.set(data.age)
            self.salaryvar.set(data.salary)

####################################################################################
    def getElementByID(self, id):
        return session.query(Employee).filter(Employee.id == id).first()







if __name__ == '__main__':
     root=Tk()
     root.geometry('600x400')
     root.title("employee")
     root.resizable(False,False)
     root.configure(background="blue")
     app = Application(master=root)

     root.mainloop()