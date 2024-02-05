from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
win = Tk()
win.geometry("1280x800")
win.title("Registration Form",)

label_username=Label(text="User Name:").pack()
label_username=Entry(width=24).pack()

label_password=Label(text="Password:").pack()
label_password=Entry(width=24).pack()

label_course=Label(text="Course:").pack()
label_var= StringVar()
xyz= ttk.Combobox(win, textvariable=label_var, values=["Computing","Ethical Hacking","BsCsit"]).pack()

label_Gar=Label(text="Guardian Name:").pack()
label_Gar=Entry(width=24).pack()

label_phone=Label(text="Phone Number:").pack()
label_phone=Entry(width=24).pack()

# # label_sub=Label(win, text="Submit Button ").pack()

# def on_submit():
#     print("Submit button clicked!")
    
# label_sub=Label( text="Submit Button ").pack()

# submit_B = win.Button(win, text="Submit", command=on_submit)
# submit_B.pack(pady=10)







mainloop()