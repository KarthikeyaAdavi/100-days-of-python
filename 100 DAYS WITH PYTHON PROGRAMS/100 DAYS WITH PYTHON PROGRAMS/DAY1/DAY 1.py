#Importing neccessary modules
from tkinter import *

#Basic features of the application
root=Tk()
root.title("Band Name generator!")
img = PhotoImage(file='download.png')
root.iconphoto(False, img)
root.geometry("400x300")

#Function to generate band names
def band_name_generator():
    City_name=City_name_entry.get()
    Pet_name=Pet_name_entry.get()
    Band_Name=Label(root,text=City_name+" "+Pet_name)
    Band_Name.pack()


#data collection for city name and pet name
City_Name_Label=Label(root,text="Please Enter the name of the city you were born in:")
City_name_entry=Entry(root,width=50,borderwidth=10)
Pet_Name_Label=Label(root,text="Please Enter the name of the pet you have:")
Pet_name_entry=Entry(root,width=50,borderwidth=10)
City_Name_Label.pack(pady=5)
City_name_entry.pack(padx=10,pady=20)
Pet_Name_Label.pack(pady=5)
Pet_name_entry.pack(padx=10,pady=20)

#Defining button for activation of band_name_generator function!
Gen_Button=Button(root,text="Generate Band Name!",command=band_name_generator)
Gen_Button.pack()

root.mainloop()
