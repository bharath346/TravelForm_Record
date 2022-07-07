from tkinter import *
bharath_root=Tk()
bharath_root.title("Travel_notepad")
bharath_root.geometry("743x434")
bharath_root.maxsize(600,400)

def getvals():
     print("Submitting form")
     print(f"{namevalue.get(), phonenovalue.get() ,gendervalue.get() ,addressvalue.get() ,paymentmodevalue.get() ,foodservicevalue.get()}\n")



     with open("Traveldetails.txt","a") as f:
         f.write(f"{ namevalue.get(), phonenovalue.get() ,gendervalue.get() ,addressvalue.get() ,paymentmodevalue.get() ,foodservicevalue.get()}\n")


#heading
Label(bharath_root,text="Welcome to Bharath Travels",bg="#F6E3C5",fg="black",font="comicsansms 20 bold",pady=20).grid(row=0,column=3)

#Text for form
name=Label(bharath_root,text="Name",font="comicsansms 10 bold",pady=10)
phoneno=Label(bharath_root,text="Phone no",font="comicsansms 10 bold",pady=10)
gender=Label(bharath_root,text="Gender",font="comicsansms 10 bold",pady=10)
address=Label(bharath_root,text="Address",font="comicsansms 10 bold",pady=10)
paymentmode=Label(bharath_root,text="Payment mode",font="comicsansms 10 bold",pady=10)

#pack text for our form
name.grid(row=1,column=2)
phoneno.grid(row=2,column=2)
gender.grid(row=3,column=2)
address.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#tkinter variable for storing entries
namevalue = StringVar()
phonenovalue = StringVar()
gendervalue = StringVar()
addressvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for ourform
nameentry = Entry(bharath_root,textvariable=namevalue)
phonenoentry = Entry(bharath_root,textvariable=phonenovalue)
genderentry = Entry(bharath_root,textvariable=gendervalue)
addressentry = Entry(bharath_root,textvariable=addressvalue)
paymententry = Entry(bharath_root,textvariable=paymentmodevalue)

#Packing the Entries
nameentry.grid(row=1,column=3)
phonenoentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
addressentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

#checkbox
foodservice = Checkbutton(text="Want to prebook your meals?",pady=10,variable=foodservicevalue)

#packof foodservice
foodservice.grid(row=6,column=3)

#buttom
Button(text="Submit to Bharath Travels",command=getvals,bg="#6CC4A1",fg="black").grid(row=7,column=3)




bharath_root.mainloop()