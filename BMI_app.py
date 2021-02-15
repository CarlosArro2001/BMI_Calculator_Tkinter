from tkinter import *
#main/root window 
root = Tk()
#setting window size & title
root.geometry("200x200")
root.title("Simple B.M.I calculator")

w_entry = Entry(root,width=10)
w_entry.grid(row=3,column=3,padx=10,pady=10,columnspan=2)
h_entry = Entry(root,width=10)
h_entry.grid(row=3,column=5,padx=10,pady=10,columnspan=2)
#function for entry weight and height and calculating the BMI 
#BMI formula = weight(kg) / height^2 (m)
def Calculate():
    weight = float(w_entry.get())
    height = float(h_entry.get())
    BMI = round(weight/height**2,2)
    BMI_label = Label(root,text="BMI : {0}".format(BMI)).grid(row=5,column=5)
#widgets
w_label = Label(root,text="Weight(in kg)").grid(row=2,column=3) 
h_label = Label(root,text="Height(in m)").grid(row=2,column=5)
r_label = Label(root,text="BMI").grid(row=4,column=3)
calc_btn = Button(root,text="Calculate",command=Calculate).grid(row=5,column=3)
root.mainloop()  