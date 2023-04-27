from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import pymysql
import csv

# Add your own database name and password here to reflect in the code
#mypass = "root"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password = "",database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library Management System")
root.minsize(width=400,height=400)
root.geometry("900x800")
#Disable the resizable Property
root.resizable(False, False)
# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("li.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)
Canvas1.config(bg="black",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#800080",bd=5)
headingFrame1.place(relx=0.06,rely=0.008,relwidth=0.85,relheight=0.06)

headingLabel = Label(headingFrame1, text="PAWAN €£ YADUVANSHI ", bg='teal', fg='black', font=('Curlz MT',30))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

headingFrame1 = Frame(root,bg="#800080",bd=5)
headingFrame1.place(relx=0.15,rely=0.14,relwidth=0.65,relheight=0.1)

headingLabel = Label(headingFrame1, text="Welcome to \n APG SHIMLA UNIVERSITY Library", bg='teal', fg='black', font=('Courier',24))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

headingFrame1 = Frame(root,bg="#800080",bd=5)
headingFrame1.place(relx=0.24,rely=0.91,relwidth=0.75,relheight=0.08)

headingLabel = Label(headingFrame1, text="Developed by:- PAWAN YADAV. \n all rights reserved © 2022-2023 PAWAN YADUVANSHI.", bg='grey', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Add Books Window.
def bookRegister():

    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(status)

    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    if bookInfo1.get() == "" and bookInfo2.get() == "" and bookInfo3.get() == "" and bookInfo4.get() == "" and status.get() == "":

        print("Error")
        tkMessageBox.showerror("error", "there is issue with some information")

    else:
        result = tkMessageBox.askquestion("Submit",
                                      "You are about to enter following details\n" + bid + "\n" + title + "\n" + author + "\n" + status + "\n" )
        bookInfo1.delete(0, END)
        bookInfo2.delete(0, END)
        bookInfo3.delete(0, END)
        bookInfo4.delete(0, END)
    if (result == "yes"):
        print("here")
        with open("library.csv", 'a') as csvfile:
            csvfile.write('{0}, {1}, {2}, {3}\n'.format(bid, title, author, status))

        csvfile.close()
    else:
        bookInfo1.set("")
        bookInfo2.set("")
        bookInfo3.set("")
        bookInfo4.set("")
        status.set("")

def addBook():

    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root

    root.destroy()
    root = Tk()
    root.title("Library Management System")
    root.minsize(width=400, height=400)
    root.geometry("500x400")
    # Disable the resizable Property
    root.resizable(False, False)

    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "booktable" # Book Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="teal")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root, bg="#800080", bd=5)
    headingFrame1.place(relx=0.2, rely=0.008, relwidth=0.65, relheight=0.09)

    headingLabel = Label(headingFrame1, text="PAWAN  YADUVANSHI ", bg='teal', fg='black', font=('Curlz MT', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    headingFrame1 = Frame(root, bg="#FF0000", bd=5)
    headingFrame1.place(relx=0.25, rely=0.11, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books",bg='navy blue', fg='magenta', font=('Courier',24))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='purple')
    labelFrame.place(relx=0.12,rely=0.35,relwidth=0.8,relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame,text="Book-ID: ", bg='olive', fg='white', font=('Courier',12))
    lb1.place(relx=0.03,rely=0.2, relheight=0.12)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.50,rely=0.2, relwidth=0.4, relheight=0.12)

    # Title
    lb2 = Label(labelFrame,text="Title: ", bg='olive', fg='white', font=('Courier',12))
    lb2.place(relx=0.03,rely=0.35, relheight=0.12)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.50,rely=0.35, relwidth=0.4, relheight=0.12)

    # Book Author
    lb3 = Label(labelFrame,text="Author: ", bg='olive', fg='white', font=('Courier',12))
    lb3.place(relx=0.03,rely=0.50, relheight=0.12)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.50,rely=0.50, relwidth=0.4, relheight=0.12)

    # Book Status
    lb4 = Label(labelFrame,text="Status(avail/issued): ", bg='olive', fg='white', font=('Courier',10))
    lb4.place(relx=0.03,rely=0.65, relheight=0.12)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.50,rely=0.65, relwidth=0.4, relheight=0.12)

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.38,rely=0.8, relwidth=0.18,relheight=0.08)

# Issue Book Window
# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password="", database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued"
bookTable = "booktable"

# List To store all Book IDs
allBid = []

# Issues Window.
def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, inf3, quitBtn, root, Canvas1, status

    bid = inf1.get()
    issueto = inf2.get()
    enrollmentno = inf3.get()



    extractBid = "select bid from " + bookTable

    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from " + bookTable + " where bid = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "insert into " + issueTable + " values ('" + bid + "','" + issueto + "','" + enrollmentno + "')"
    show = "select * from " + issueTable

    updateStatus = "update " + bookTable + " set status = 'issued' where bid = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")

        else:
            allBid.clear()
            messagebox.showinfo('Message', "Book Already Issued")

            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    print(bid)
    print(issueto)
    print(enrollmentno)

    allBid.clear()

def issueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, inf3, quitBtn, root, Canvas1, status

    root.destroy()
    root = Tk()
    root.title("Library Management System")
    root.minsize(width=400, height=400)
    root.geometry("500x400")
    # Disable the resizable Property
    root.resizable(False, False)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="purple")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#800080", bd=5)
    headingFrame1.place(relx=0.2, rely=0.008, relwidth=0.65, relheight=0.09)

    headingLabel = Label(headingFrame1, text="PAWAN  YADUVANSHI ", bg='teal', fg='black', font=('Curlz MT', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    headingFrame1 = Frame(root, bg="#FF0000", bd=5)
    headingFrame1.place(relx=0.25, rely=0.11, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='navy blue', fg='magenta', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book-ID:- ", bg='olive', fg='white', font=('Courier', 12))
    lb1.place(relx=0.03, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.48, rely=0.2, relwidth=0.5, relheight=0.12)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Issued-To:- ", bg='olive', fg='white', font=('Courier', 12))
    lb2.place(relx=0.03, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.48, rely=0.4, relwidth=0.5, relheight=0.12)

    # Student ID
    lb3 = Label(labelFrame, text="Enrollment-No:- ", bg='olive', fg='white', font=('Courier', 12))
    lb3.place(relx=0.03, rely=0.6)

    inf3 = Entry(labelFrame)
    inf3.place(relx=0.48, rely=0.6, relwidth=0.5, relheight=0.12)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.38, rely=0.86, relwidth=0.18, relheight=0.08)

# Delete Book Window
# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root",password="", database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued"
bookTable = "booktable"  # Book Table

# Delete Window.
def deleteBook():

    bid = bookInfo1.get()

    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

    print(bid)

    bookInfo1.delete(0, END)

def delete():

    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root.wm_iconwindow()
    root = Tk()
    root.title("Library Management System")
    root.minsize(width=400, height=400)
    root.geometry("500x400")
    # Disable the resizable Property
    root.resizable(False, False)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="olive")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#800080", bd=5)
    headingFrame1.place(relx=0.2, rely=0.008, relwidth=0.65, relheight=0.09)

    headingLabel = Label(headingFrame1, text="PAWAN  YADUVANSHI ", bg='teal', fg='black', font=('Curlz MT', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    headingFrame1 = Frame(root, bg="#FF0000", bd=5)
    headingFrame1.place(relx=0.25, rely=0.11, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book",bg='navy blue', fg='magenta', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='purple')
    labelFrame.place(relx=0.12, rely=0.4, relwidth=0.8, relheight=0.35)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book-ID: ", bg='olive', fg='white', font=('Courier',15))
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.4,rely=0.5, relwidth=0.5, relheight=0.19)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0',
                       fg='black', command=deleteBook)
    SubmitBtn.place(relx=0.38, rely=0.8, relwidth=0.18, relheight=0.08)

# Return Book Window
# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password="", database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued"  # Issue Table
bookTable = "booktable"  # Book Table

allBid = []  # List To store all Book IDs

# Return Window.
def returnn():
    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status

    bid = bookInfo1.get()

    extractBid = "select bid from " + issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from " + bookTable + " where bid = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "delete from " + issueTable + " where bid = '" + bid + "'"

    print(bid in allBid)
    print(status)
    updateStatus = "update " + bookTable + " set status = 'avail' where bid = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    allBid.clear()

def returnBook():
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

    root.destroy()
    root = Tk()
    root.title("Library Management System")
    root.minsize(width=400, height=400)
    root.geometry("500x400")
    # Disable the resizable Property
    root.resizable(False, False)

    Canvas1 = Canvas(root)

    Canvas1.config(bg="silver")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#800080", bd=5)
    headingFrame1.place(relx=0.2, rely=0.008, relwidth=0.65, relheight=0.09)

    headingLabel = Label(headingFrame1, text="PAWAN  YADUVANSHI ", bg='teal', fg='black', font=('Curlz MT', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    headingFrame1 = Frame(root, bg="#FF0000", bd=5)
    headingFrame1.place(relx=0.25, rely=0.11, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg='navy blue', fg='magenta', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='purple')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Book-ID: ", bg='olive', fg='white', font=('Courier', 15))
    lb1.place(relx=0.05, rely=0.4)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.45, rely=0.4, relwidth=0.5, relheight=0.12)

    # Submit Button
    SubmitBtn = Button(root, text="Return", bg='#d1ccc0', fg='black', command=returnn)
    SubmitBtn.place(relx=0.38, rely=0.86, relwidth=0.18, relheight=0.08)

# View Book Window
# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password="", database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "booktable"

# View Book From Database.
def View():
    global  Canvas1, con, cur, root

    root.destroy()
    root = Tk()
    root.title("Library Management System")
    root.minsize(width=400, height=400)
    root.geometry("500x400")
    root.resizable(False, False)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="maroon")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#800080", bd=5)
    headingFrame1.place(relx=0.2, rely=0.008, relwidth=0.65, relheight=0.09)

    headingLabel = Label(headingFrame1, text="PAWAN  YADUVANSHI ", bg='teal', fg='black', font=('Curlz MT', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    headingFrame1 = Frame(root, bg="#FF0000", bd=5)
    headingFrame1.place(relx=0.25, rely=0.11, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='navy blue', fg='magenta', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='purple')
    labelFrame.place(relx=0.08, rely=0.3, relwidth=0.89, relheight=0.59)
    y = 0.25

    Label(labelFrame, text="%-10s%-40s%-30s%-20s" % ('BID', 'Title', 'Author', 'Status'), bg='olive', fg='white').place(
        relx=0.05, rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------- ", bg='olive',
          fg='white').place(relx=0.05, rely=0.18)
    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-40s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                relx=0.05, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

#Main Window Button

btn_1 = Button(root,text="Book Details",bg='navy blue', fg='white', font=('Courier',18), command=addBook)
btn_1.place(relx=0.3,rely=0.4, relwidth=0.30,relheight=0.1)

btn_2 = Button(root,text="Delete Book",bg='teal', fg='white', font=('Courier',18), command=delete)
btn_2.place(relx=0.3,rely=0.5, relwidth=0.30,relheight=0.1)

btn_3 = Button(root,text="View Book ",bg='olive', fg='white', font=('Courier',18), command=View)
btn_3.place(relx=0.3,rely=0.6, relwidth=0.30,relheight=0.1)

btn_4 = Button(root,text="Issued Book ",bg='grey', fg='white', font=('Courier',18), command = issueBook)
btn_4.place(relx=0.3,rely=0.7, relwidth=0.30,relheight=0.1)

btn_5 = Button(root,text="Return Book",bg='purple', fg='white', font=('Courier',18), command = returnBook )
btn_5.place(relx=0.3,rely=0.8, relwidth=0.30,relheight=0.1)

root.mainloop()
