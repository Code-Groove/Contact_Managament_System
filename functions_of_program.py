def Database():
    global connect, curr
    connect = sqlite3.connect("contactbook1.db")
    curr = connect.cursor()
    curr.execute(
        "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, GENDER TEXT, ADDRESS TEXT, CONTACT TEXT)")




def show_form():
    #basic diaply variables
    display_screen = Tk()
    display_screen.geometry("1000x450")
    display_screen.title("Contact Management System")
    global tree
    global first_name,last_name,gender,address,contact
    global search
    first_name = StringVar()
    last_name = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
    search = StringVar()
    #the frames required for the project
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LForm = Frame(display_screen, width="350",bg="#074463")
    LForm.pack(side=LEFT, fill=Y)
    lfr = Frame(display_screen, width=500,bg="#074463")
    lfr.pack(side=LEFT, fill=Y)
    mfr = Frame(display_screen, width=600)
    mfr.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Contact Management System", font=('verdana', 18), width=600,bg="gold")
    lbl_text.pack(fill=X)
    #All the labels,entries,buttons required for the structure
    Label(LForm, text="First Name  ", font=("Times New Roman", 12),bg="#15244C",fg = "gold").pack(side=TOP)
    Entry(LForm,font=("Times New Roman",10,"bold"),textvariable=first_name).pack(side=TOP, padx=10, fill=X)
    Label(LForm, text="Last Name ", font=("Times New Roman", 12),bg="#15244C",fg = "gold").pack(side=TOP)
    Entry(LForm, font=("Times New Roman", 10, "bold"),textvariable=last_name).pack(side=TOP, padx=10, fill=X)
    Label(LForm, text="Gender ", font=("Times New Roman", 12),bg="#15244C",fg = "gold").pack(side=TOP)
    gender.set("Select Gender")
    content={'Male','Female'}
    OptionMenu(LForm,gender,*content).pack(side=TOP, padx=10, fill=X)
    Label(LForm, text="Address ", font=("Times New Roman", 12),bg="#15244C",fg = "gold").pack(side=TOP)
    Entry(LForm, font=("Times New Roman", 10, "bold"),textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(LForm, text="Contact ", font=("Times New Roman", 12),bg="#15244C",fg = "gold").pack(side=TOP)
    Entry(LForm, font=("Times New Roman", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Button(LForm,text="Submit",font=("Times New Roman", 10, "bold"),command=register,bg="#15244C",fg = "gold").pack(side=TOP, padx=10,pady=5, fill=X)
    btn_view = Button(lfr, text="View All", command=show_data,bg="gold")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(lfr, text="Reset", command=Reset,bg="gold")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(lfr, text="Delete", command=Delete,bg="gold")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(lfr, text="Update", command=update_data,bg="gold")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(mfr, orient=HORIZONTAL)
    scrollbary = Scrollbar(mfr, orient=VERTICAL)
    tree = ttk.Treeview(mfr,columns=("Id", "Name", "Contact", "Email","Rollno","Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Id', text="Id", anchor=W)
    tree.heading('Name', text="FirstName", anchor=W)
    tree.heading('Contact', text="LastName", anchor=W)
    tree.heading('Email', text="Gender", anchor=W)
    tree.heading('Rollno', text="Address", anchor=W)
    tree.heading('Branch', text="Contact", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    show_data()




def update_data():
    Database()
    first_name1=first_name.get()
    last_name1=last_name.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    if first_name1=='' or last_name1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        current_it = tree.focus()
        contents = (tree.item(current_it))
        selecteditem = contents['values']
        connect.execute('UPDATE REGISTRATION SET first_name=?,last_name=?,GENDER=?,ADDRESS=?,CONTACT=? WHERE RID = ?',(first_name1,last_name1,gender1,address1,contact1, selecteditem[0]))
        connect.commit()
        tkMessageBox.showinfo("Message","Updated successfully")
        Reset()
        show_data()




def register():
    Database()
    first_name1=first_name.get()
    last_name1=last_name.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    if first_name1=='' or last_name1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        connect.execute('INSERT INTO REGISTRATION (first_name,last_name,GENDER,ADDRESS,CONTACT) \
              VALUES (?,?,?,?,?)',(first_name1,last_name1,gender1,address1,contact1));
        connect.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        show_data()




def Reset():
    tree.delete(*tree.get_children())
    show_data()
    first_name.set("")
    last_name.set("")
    gender.set("")
    address.set("")
    contact.set("")




def Delete():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            current_it = tree.focus()
            contents = (tree.item(current_it))
            selecteditem = contents['values']
            tree.delete(current_it)
            curr=connect.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            connect.commit()
            curr.close()
            



def show_data():
    Database()
    tree.delete(*tree.get_children())
    curr=connect.execute("SELECT * FROM REGISTRATION")
    fetch_all = curr.fetchall()
    for data in fetch_all:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",select)
    curr.close()
    connect.close()



def select(self):
    current_it = tree.focus()
    contents = (tree.item(current_it))
    selecteditem = contents['details']
    first_name.set(selecteditem[1])
    last_name.set(selecteditem[2])
    gender.set(selecteditem[3])
    address.set(selecteditem[4])
    contact.set(selecteditem[5])
