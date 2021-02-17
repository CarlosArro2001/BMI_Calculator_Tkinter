from tkinter import *
#main/root window 
root = Tk()
#setting window size & title
root.geometry("600x600")
root.title("Simple B.M.I calculator")
#adding background
C = Canvas(root,bg="purple",height=200,width=200).grid()
fileName = PhotoImage(file = "background.png")
background_label=Label(root , image=fileName)
background_label.place(x=0,y=0,relwidth=1,relheight=1) 
#entry widgets
w_entry = Entry(root,width=10)
w_entry.grid(row=4,column=3,padx=10,pady=10,columnspan=2)
h_entry = Entry(root,width=10)
h_entry.grid(row=4,column=5,padx=10,pady=10,columnspan=2)
#function for entry weight and height and calculating the BMI 
#BMI formula = weight(kg) / height^2 (m)
def Calculate():
    weight = float(w_entry.get())
    height = float(h_entry.get())
    BMI = round(weight/height**2,2)
    bg_color = ""
    result = ""
    #checking if : underweight , normal weight , overweight 
    if(BMI < 18.5):
        bg_color = "red"
        result = "Underweight" 
    if(BMI >= 18.5 and BMI <=24.9):
        bg_color = "Green"
        result = "Normal Weight"
    if(BMI >=  25.0):
        bg_color = "Red"
        result = "Overweight"  
    BMI_label = Label(root,text="BMI : {0} {1}".format(BMI,result) , bg=bg_color).grid(row=8,column=8)
#widgets
w_label = Label(root,text="Weight(in kg)").grid(row=3,column=3) 
h_label = Label(root,text="Height(in m)").grid(row=3,column=5)
r_label = Label(root,text="BMI").grid(row=6,column=3)
calc_btn = Button(root,text="Calculate",command=Calculate).grid(row=8,column=3,padx=10,pady=10)
root.mainloop()  