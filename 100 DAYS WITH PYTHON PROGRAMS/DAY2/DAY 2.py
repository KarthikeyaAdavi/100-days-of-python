from tkinter import *
from tkinter.ttk import *
import time
root=Tk()

#Basic application definitions
root.title("BS!")
root.geometry("200x210")
photo=PhotoImage(file="BSICON.png")
root.iconphoto(False,photo)
#function to calculate bill

def Bill_calculator():
#calculation bill_per_person
    
    Bill=Bill_Amount_Entry.get()
    Head_Count=People_no_Entry.get()
    bill_per_person=round(int(Bill)/int(Head_Count),2)
    
#Cheking if the bill per person has been printed or noe
    Bill_output=Label(root,text=f"Rs.{bill_per_person}",font=('Times',24))
    exists=(Bill_output.winfo_exists())
    if exists==1:
        Bill_output.after(2000,Bill_output.destroy)
    Bill_output.pack()


#Data Collection Entries and Lables
people_no=Label(root,text="Enter the number of people:")
people_no.pack(pady=2)
People_no_Entry=Entry(root,)
People_no_Entry.pack(padx=5,pady=10)
Bill_Amount=Label(root,text="Enter the amount of the Bill:")
Bill_Amount.pack(pady=2)
Bill_Amount_Entry=Entry(root,)
Bill_Amount_Entry.pack(padx=5,pady=10)

#Button to acess function
Bill_Generate_Button=Button(root,text="Generate bill per person:",command=Bill_calculator)
Bill_Generate_Button.pack(padx=5,pady=5)

#Button to exit main loop
exit_button=Button(root,text="Exit",command=root.destroy)
exit_button.pack(pady=2)
root.mainloop()
