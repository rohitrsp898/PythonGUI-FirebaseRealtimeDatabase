
#The is simple realtime database storage of data in firebase using python

#Made by Rohit 11-11-2020


################################################################################

################################################################################

#NOTE  if you insert any data that have same ID as any previous data it will overwrite the existing data with new, While inserting please check User ID


#Python with Firbase

# pip install requests
# pip install python-firebase      change the async filename to asyncn in firbase.py, __init__ and asyn


from firebase import firebase      #for more details visit  https://pypi.org/project/python-firebase/
from tkinter import *
from tkinter import ttk



#connection with firbase real time database
fb=firebase.FirebaseApplication("https://pythonrtdb.firebaseio.com/",None)


def clear1():

    #clear all the entry fields
    val0.delete(0, 'end')
    val1.delete(0, 'end')
    val2.delete(0, 'end')
    val3.delete(0, 'end')
    val4.delete(0, 'end')
    vals.delete(0, 'end')
    vald.delete(0, 'end')
    
    

    #set focus to User ID field
    val0.focus()

def clear2():

    #clear all the field that appeared for Updation
    
    val1up.delete(0, 'end')
    val2up.delete(0, 'end')
    val3up.delete(0, 'end')
    val4up.delete(0, 'end')

    #set focus of find field
    valf.focus()

def forget():

    #remove all the widget (Label,Entry)
    l1.grid_remove()
    l2.grid_remove()
    l3.grid_remove()
    l4.grid_remove()
    
    val1up.grid_remove()
    val2up.grid_remove()
    val3up.grid_remove()
    val4up.grid_remove()

    btnup.grid_remove()

    #set focus to User ID field
    val0.focus()




#input function trigered when press the button insert
def input_val_insert():

    

    #checking all the field have value 
    if val0.get()and val1.get() and val2.get() and val3.get() and val4.get():  

        #assigning those values to variables
        uid=val0.get()
        name=val1.get()
        lname=val2.get()
        age=val3.get()
        salary=val4.get()

        #checking that all fields vales are assigned properly or not
        if not name.isalpha()or not lname.isalpha() or not age.isdigit() or not uid.isdigit() or not salary.isdigit() :
            #if true then error message will appear
            txt1.set("Please Enter Valid Details !")
               
        else:
            #converting string age,salary to integer age and salary
            ageint=int(age)
            sal=int(salary)

            #condition for validation of User ID, Name, Last Name,age, salary.
            if(ageint>=18 and ageint<=88 and sal>=10000 and sal<=10000000):

                if(len(uid)<=6 and uid !=0 and len(name)<=10 and len(name)>=3 and len(lname)<=10 and len(lname)>=3):
                #calling the function to insert the data in firebase
                    insert(uid,name,lname,age,salary)

                else:
                    txt1.set("User ID (1-999999) and Name (3-10) characters allowed respectively !")
                
            else:
               txt1.set("Please Enter valid Age (18 or above) and Salary (10000 and above) !")
    else:
        txt1.set("Please fill all the fields !")
        


def input_val_update():

    

    #input function trigered when press the button update
    if valf.get() and val1up.get() and val2up.get() and val3up.get() and val4up.get():

        #assigning those values to variables
        uid=valf.get()
        name=val1up.get()
        lname=val2up.get()
        age=val3up.get()
        salary=val4up.get()

        #checking that all fields vales are assigned properly or not
        if not name.isalpha()or not lname.isalpha() or not age.isdigit() or not salary.isdigit() :
            txt1.set("Please Enter Valid Details !")
               
        else:
            #converting string age,salary to integer age and salary
            ageint=int(age)
            sal=int(salary)

            #condition for validation of User ID, Name, Last Name,age, salary.
            if(ageint>=18 and ageint<=88 and sal>=10000 and sal<=10000000):
                
                if(len(uid)<=6 and uid !=0 and len(name)<=10 and len(name)>=3 and len(lname)<=10 and len(lname)>=3):
                    #calling the function to update the data in firebase
                    update(uid,name,lname,age,salary)

                else:
                    txt1.set("User ID (1-999999) and Name (3-10) characters allowed respectively !")
                     
            else:
               txt1.set("Please enter valid Age>=18 and Salary>= 10,000 Rupees!")      
    else:
        txt1.set("Please fill all the fields !")
        

#responsible for inserting the data in Firebase
def insert(uid,name,lname,age,salary):


    #data in dictonary format
    data={}
    data["UID"]=uid
    data["First Name"]=name
    data['Last Name']=lname
    data['Age']=age
    data['Salary']=salary
    
    #passing the dictonary in put for insertion of data in firebase with User id as reference ID i.e UID is act as a primary key
    result=fb.put("/User Data",uid,data)  

    #Information will print 
    txt1.set("Data Insert Successfully !")
    
    #fetch the data from firbase and display in Treeview
    data_view()

    #clear the Entry's 
    clear1()
    
    
#responsible for updatation the data in Firebase
def update(uid,name,lname,age,salary):
    
    #### NOTE in my case update and insert i tooke same way becouse I want my own ref no if you dont want than user 'push' method insted of 'put'.

    
    #data in dictonary format
    data={}
    data["UID"]=uid
    data["First Name"]=name
    data['Last Name']=lname
    data['Age']=age
    data['Salary']=salary
    
    #passing the dictonary in put for insertion of data in firebase with User id as reference ID i.e UID is act as a primary key
    result=fb.put("/User Data",uid,data)  
    #for ID : {}".format(uid))

    #fetch the data from firbase and display in Treeview
    data_view()

    #hiding the labels and entry that appered for updation
    forget()

    #Clearing the entry's that hides
    valf.delete(0, 'end')
    clear2()
    txt1.set("Data updated Successfully for User ID : {} ".format(uid))
    
#responsible for deletion the data in Firebase
def data_del():

    #For hiding the Update Labels and Entry
    forget()
    valf.delete(0, 'end')

    if vald.get():

        #enter user ID will be deleted
        delete_User=vald.get()

        #deleting data from firebase
        delete=fb.delete("/User Data",delete_User)
        txt1.set("Data Deleted Successfully !")

        #fetch the data from firbase and display in Treeview
        #Clearing previous data that are present in Treeview
        tv.delete(*tv.get_children())

        vald.delete(0, 'end')
        data_view()
    else:
        txt1.set("Please put value !")
    
    


#responsible for Desplaying the data in Treeview from Firebase (specific Data) 
def data_one():

    #For hiding the Update Labels and Entry
    forget()
    valf.delete(0, 'end')

    try:
        
        #Clearing previous data that are present in Treeview
        tv.delete(*tv.get_children())
        
        user_uid=vals.get()         #get searched value from search entry
        if user_uid=="":
            txt1.set("User ID Search Field is Empty !")
        else:
            #get data only for Searched User ID
            user=fb.get("/User Data",user_uid)
            print(user)
            clear1()

            #fetching only dictionary values and converting them into tuple
            tup_data=tuple(user.values())    # ('23', 'R', 'P', '100000', '1')

            #insert data in Treeview with specific order
            tv.insert("","end",values=(tup_data[4],tup_data[1],tup_data[2],tup_data[0],tup_data[3]))
            
            #Display in CMD interface with Headings and Values
            #print ("{:<10} {:<12} {:<12} {:<4} {:<8}".format("UID","First Name","Last Name","Age","Salary\n"))
            #print ("{:<10} {:<12} {:<12} {:<4} {:<8}".format(user["UID"],user["First Name"],user["Last Name"],user["Age"],user["Salary"]))        

    except:
        txt1.set("Data Not Present With this User ID !")
        

def data_find():
    
    try:
        #for Updating the values these widget will appear
        #for Updating Name
        #Unhiding the labels and Entry
        l1.grid(row=1,column=2,pady=4,padx=5)
        
        val1up.grid(row=1,column=3,pady=4,padx=5)

        #for Updating last Name
        #Unhiding the labels and Entry
        l2.grid(row=2,column=2,pady=4,padx=5)
        
        val2up.grid(row=2,column=3,pady=4,padx=5)

        #for updating Age        
        #Unhiding the labels and Entry
        l3.grid(row=3,column=2,pady=4,padx=5)
        
        val3up.grid(row=3,column=3,pady=4,padx=5)

        #For Updating Salary
        #Unhiding the labels and Entry
        l4.grid(row=4,column=2,pady=4,padx=5)
        
        val4up.grid(row=4,column=3,pady=4,padx=5)

        btnup.grid(row=0, column=2,sticky=W,pady=4,padx=5)

        #display selected data in treeview 
        tv.delete(*tv.get_children())  #clear old treeview data

        clear2()
        #selected user Id data will fetch from Firebase
        user_uid=valf.get()         
        user=fb.get("/User Data",user_uid)
        clear1()
        
        #fetching only dictionary values and converting them into tuple
        tup_data=tuple(user.values())    ## ('23', 'R', 'P', '100000', '1')

        #insert data in Treeview with specific order    
        tv.insert("","end",values=(tup_data[4],tup_data[1],tup_data[2],tup_data[0],tup_data[3]))

        #Data will reflect in entry box as well for updation
        
        val1up.insert(0,tup_data[1])
        val2up.insert(0,tup_data[2])
        val3up.insert(0,tup_data[0])
        val4up.insert(0,tup_data[3])

        #set focus to 'Name' entry box (cursor will be there)
        val1up.focus()
        txt1.set("Please Insert new Values in Data Fields !")

        #Displaying data in CMD with these headings and values
        #print ("{:<10} {:<12} {:<12} {:<4} {:<8}".format("UID","First Name","Last Name","Age","Salary\n"))
        #print ("{:<10} {:<12} {:<12} {:<4} {:<8}".format(user["UID"],user["First Name"],user["Last Name"],user["Age"],user["Salary"]))
        
    except:
        #Hiding the widgets that appeared for updation is data is not present in Firebase
        forget()
        txt1.set("Data Not Present With this User ID !")
    
    
#responsible for Desplaying the data in Treeview from Firebase (All Data)  
def data_view():

    #For hiding the Update Labels and Entry
    clear1()
    forget()
    valf.delete(0, 'end')
    txt1.set("")

    try:
        # clearing the TreeView
        tv.delete(*tv.get_children())

        #Fetching data from Firebase
        users=fb.get("/User Data",None) # return list of data with dict and None ->[None, {}, {}, None, {}]       
        #print(users)
        
        #cheking that data we get is in list formate or dict
        if type(users)is list:  #for list
            
            for user in users:

                if type(user) is dict:     #filtering the data - only dict will pass
                
                    tup_data=tuple(user.values()) # ('23', 'R', 'P', '100000', '1')
                    
                    #insert data in Treeview with specific order
                    tv.insert("","end",values=(tup_data[4],tup_data[1],tup_data[2],tup_data[0],tup_data[3]))
        else:
            #for dict
            users_lst=users.values()
            #run this when firebase have only single data
            for user in users_lst:
                
                
                tup_data=tuple(user.values())  #('23', 'R', 'P', '100000', '1')

            #insert data in Treeview with specific order
                tv.insert("","end",values=(tup_data[4],tup_data[1],tup_data[2],tup_data[0],tup_data[3]))
        
            
    except :
        txt1.set("Data is not present at this moment!")


        
       




    
#GUI creation start here 

#window creation with title and Geometory(windows size)    
win=Tk()
win.title("User Data")
win.geometry("810x660")
win.resizable(False,False)  #fixed window






#frames
frmHead=Frame(win)
frmHead.grid(row=0, column=0,pady=1,padx=50)

frm1=Frame(win)
frm1.grid(row=1, column=0,pady=1,padx=50)

frmb=Frame(win)
frmb.grid(row=2, column=0,pady=1,padx=50)

frm=Frame(win)
frm.grid(row=3, column=0,pady=5,padx=10)






#style for Treeview

style = ttk.Style()
style1 = ttk.Style()
style.configure("Treeview.Heading", font=(None, 12),foreground='#620062')
style1.configure("Treeview", font=("Comic Sans MS", 10))


#Treeview

tv=ttk.Treeview(frm,column=(1,2,3,4,5),show="headings",height="12",padding=5,selectmode='browse')  #treeview structure
tv.pack()

tv.heading(1,text="User ID")
tv.column(1,width="120")

tv.heading(2,text="First Name")
tv.column(2,width="170")

tv.heading(3,text="Last Name")
tv.column(3,width="170")

tv.heading(4,text="Age")
tv.column(4,width="80")

tv.heading(5,text="Salary in ₹")
tv.column(1,width="100")





#Heading Labels

Label(frmHead,text="-- User Data --",font=(None,"10"),fg="Blue").grid(row=0,pady=1,padx=1)
Label(frmHead,text="-----------------------------------------------------------------------------------------",font=('Lucida Console',"10"),fg="Black").grid(row=1)
Label(frmHead,text="-----------------------------------------------------------------------------------------",font=('Lucida Console',"10"),fg="Black").grid(row=3)





#Information labels for error display 

txt1=StringVar()
txt1.set("")
ErrorL1=Label(frmHead,textvariable=txt1,fg="Red",font=('Lucida Console',"12")).grid(row=2,padx=5)





#Labels and Entry's for data insert

#User ID

Label(frm1,text="User ID :",font=('Lucida Console',"10")).grid(row=0,pady=4,padx=5)
val0=Entry(frm1,bd=3)
val0.grid(row=0,column=1,pady=4,padx=5)


#First Name

entry_Name = StringVar()
Label(frm1,text="First Name :",font=('Lucida Console',"10")).grid(row=1,pady=4,padx=5)
val1=Entry(frm1,bd=3)
val1.grid(row=1,column=1,pady=4,padx=5)

#Last Name

Label(frm1,text="Last Name :",font=("Lucida Console","10")).grid(row=2,pady=4,padx=5)
val2=Entry(frm1,bd=3)
val2.grid(row=2,column=1,pady=4,padx=5)

#User Age        
Label(frm1,text="User Age :",font=('Lucida Console',"10")).grid(row=3,pady=4,padx=5)
val3=Entry(frm1,bd=3)
val3.grid(row=3,column=1,pady=4,padx=5)

#User Salary
Label(frm1,text="User Salary :",font=('Lucida Console',"10")).grid(row=4,pady=4,padx=5)
val4=Entry(frm1,bd=3)
val4.grid(row=4,column=1,pady=4,padx=5)





#Labels, entry with Buttons

#Search User
Label(frmb,text="Search User ID :",font=('Lucida Console',"10")).grid(row=1,column=0,pady=4,padx=5)
vals=Entry(frmb,bd=3)
vals.grid(row=1,column=1,pady=4,padx=5)

btns=Button(frmb,text="Search",font=('Lucida Console',"10"),command=data_one,width=10)
btns.grid(row=1, column=2,sticky=W,pady=4,padx=5)


#Delete User 
Label(frmb,text="Delete User ID :",font=('Lucida Console',"10")).grid(row=2,column=0,pady=4,padx=5)
vald=Entry(frmb,bd=3)
vald.grid(row=2,column=1,pady=4,padx=5)

btndel=Button(frmb,text="Delete",font=('Lucida Console',"10"),command=data_del,width=10)
btndel.grid(row=2, column=2,sticky=W,pady=4,padx=5)


#Find User for update
Label(frm1,text="For Update User ID  :",font=('Lucida Console',"10")).grid(row=0,column=2,pady=4,padx=5)
valf=Entry(frm1,bd=3)
valf.grid(row=0,column=3,pady=4,padx=5)

btnf=Button(frm1,text="Update",font=('Lucida Console',"10"),command=data_find,width=10)
btnf.grid(row=0, column=4,sticky=W,pady=4,padx=5)





#Insert, view and Upadte Data

#insert
btn=Button(frmb,text="Insert",font=('Lucida Console',"10"),command=input_val_insert,width=10)
btn.grid(row=0, column=0,sticky=W,pady=5,padx=5)

#view
btn1=Button(frmb,text="Refresh",font=('Lucida Console',"10"),command=data_view,width=10)
btn1.grid(row=0, column=1,sticky=W,pady=4,padx=5)

#update
btnup=Button(frmb,text="Commit",font=('Lucida Console',"10"),command=input_val_update,width=10)
btnup.grid_forget()





#for Updating the values these widget will appear, for now they are hidden
#for Updating Name
l1=Label(frm1,text="Update First Name :",font=('Lucida Console',"10"))
l1.grid_forget()
val1up=Entry(frm1,bd=3)
val1up.grid_forget()  # for hiding the widget in grid 

#for Updating last Name
l2=Label(frm1,text="Update Last Name :",font=("Lucida Console","10"))
l2.grid_forget()
val2up=Entry(frm1,bd=3)
val2up.grid_forget()

#for updating Age        
l3=Label(frm1,text="Update User Age :",font=('Lucida Console',"10"))
l3.grid_forget()
val3up=Entry(frm1,bd=3)
val3up.grid_forget()

#For Updating Salary
l4=Label(frm1,text="Update User Salary :",font=('Lucida Console',"10"))
l4.grid_forget()
val4up=Entry(frm1,bd=3)
val4up.grid_forget()



data_view()

#mainloop
win.mainloop()
    
    
    
    































