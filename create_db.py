#***************************************************************************
#Create New Company Database and add required tables
#
#succeeds: welcome screen
#preceeds: Login screen
#
#functions missing: GUI, Username & Password Protection & Encryption
#***************************************************************************
 
import sqlite3
import tkinter
from sqlite3 import Error
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import os
import csv
 
#Define Company Name == DB
#***************************************************************************
class define_company():
    def __init__(self):
        self.root = tkinter.Tk()
         
    def newco(self):
        self.root.destroy()
        self.root = tkinter.Tk()
        self.root.title("Name Your Company")
         
        self.label = ttk.Label(self.root,text="Company Name")
        self.label.grid(row=0)
         
        self.company = ttk.Entry(self.root)
        self.company.grid(row=0, column=1)
         
        self.button = ttk.Button(self.root, text="Submit", command=self.return_company)
        self.button.grid(row=3, column=1, sticky=W, pady=4)
         
        self.button = ttk.Button(self.root, text="Return to Start", command=self.start_menu)
        self.button.grid(row=3, column=2, sticky=W, pady=4)
        self.root.mainloop()
     
    def return_company(newco):
        company = newco.company.get()
        return company
 
    def quit(self):
        self.root.destroy()
        path = get_dirname() + str("/")
        company = self.newco()
        company.company.get()
        create_connection(str(path) + str(company) + str(".db"))
         
    def start_menu(self):
        self.root.destroy()
        self.root = tkinter.Tk()
        self.root.title("Start")
         
        self.namebutton = ttk.Button(self.root, text="New Company", command=self.newco)
        self.donebutton = ttk.Button(self.root, text="Done", command=self.quit)
         
        self.namebutton.grid(column=0, row=0, sticky="nsew")
        self.donebutton.grid(column=0, row=1, sticky="nsew")
        self.root.mainloop()
     
    def run(self):
        self.start_menu()
         
 
 
#Create Database
#***************************************************************************
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
         
 
#Choose Directory where database will be saved
#***************************************************************************
def get_dirname():
    Tk().withdraw()
    print("Initializing Dialogue...\nPlease select a directory.")
    dirname = askdirectory(initialdir=os.getcwd(),title='Please select a directory')
    if len(dirname) > 0:
        return dirname
    else: 
        dirname = os.getcwd()
        print ("\nNo directory selected - initializing with %s \n" % os.getcwd())
        return dirname
 
 
print()
#Choose Directory where database will be saved
#***************************************************************************
    company = define_company().run()
if __name__ == '__main__':
    # path = get_dirname() + str("/")
    # create_connection(str(path) + str(company) + str(".db"))
 
conn = sqlite3.connect(str(path) + str(company) +str(".db"))
c = conn.cursor()
