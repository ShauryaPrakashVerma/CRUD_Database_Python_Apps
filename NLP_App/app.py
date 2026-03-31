from tkinter import *
from tkinter import messagebox
from mydb import Database
from myapi import API

class NLPApp:

    def __init__(self):
        
        # create db object of the class imported
        self.dbo = Database()
        self.apio = API()
        
        self.root = Tk()
        self.root.title("NLPApp")
        # self.root.iconbitmap("re")
        self.root.geometry("400x600")
        self.root.configure(bg = "seagreen")     
        self.login_gui()
        self.root.mainloop()
        
        
        
    def login_gui(self):
        self.clear()
        self.root.configure(background="seagreen")
        
        heading = Label(self.root, text = "NLP App", bg="seagreen", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font = ("helvetica",40,"bold"))
        
        label_email = Label(self.root, text="Enter your Email:", bg="seagreen", fg="white", font=("helvetica",12,))
        label_email.pack(pady=(20,0))
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10),ipady=2)
        
        label_password = Label(self.root, text="Enter your Password:", bg="seagreen", fg="white", font=("helvetica",12,))
        label_password.pack(pady=(30,0))
        self.password_input = Entry(self.root, width=50, border=0, show="*")
        self.password_input.pack(pady=(5,10),ipady=2)
        
        button_login = Button(self.root, text="Login", border=0, width=20,fg="seagreen",command=self.perform_login)
        button_login.pack(pady=(50,0))
        
        redirect_register = Button(self.root, text="Not a member? Register", bg="seagreen", fg="white", font=("helvetica",10), border=0, command=self.register_gui)
        redirect_register.pack(pady=(30,0))
        
    
    
    
    def register_gui(self):
        
        self.clear()
        self.root.configure(background="royalblue")
        
        heading = Label(self.root, text = "Registration", bg="royalblue", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font = ("helvetica",20,"bold"))
        
        label_name = Label(self.root, text="Enter your Name:", bg="royalblue", fg="white", font=("helvetica",12,))
        label_name.pack(pady=(10,0))
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5,10),ipady=2)
        
        label_email = Label(self.root, text="Enter your Email:", bg="royalblue", fg="white", font=("helvetica",12,))
        label_email.pack(pady=(10,0))
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10),ipady=2)
        
        label_password = Label(self.root, text="Set Password:", bg="royalblue", fg="white", font=("helvetica",12,))
        label_password.pack(pady=(10,0))
        self.password_input = Entry(self.root, width=50, border=0, show="*")
        self.password_input.pack(pady=(5,10),ipady=2)
        
        button_register = Button(self.root, text="Register", border=0, width=20,fg="royalblue",command=self.perform_registration)
        button_register.pack(pady=(50,0))
        
        redirect_login = Button(self.root, text="Already a member? Login", bg="royalblue", fg="white", font=("helvetica",10), border=0, command=self.login_gui)
        redirect_login.pack(pady=(30,0))
        
    
    def dashboard(self):
        
        self.clear()
        self.root.configure(background = "navyblue")
        
        heading = Label(self.root, text = "NLP App", bg="navyblue", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font = ("helvetica",40,"bold"))
        
        button_sentiment = Button(self.root, text="Sentiment Analysis", font=5, border=0, height=3, width=30,fg="royalblue",command=self.main_page)
        button_sentiment.pack(pady=(50,0))
        
        button_register = Button(self.root, text="NER", border=0, width=30, font=5, height=3, fg="royalblue",command=self.main_page)
        button_register.pack(pady=(50,0))
        
        button_register = Button(self.root, text="Text Classification", border=0, font=5, width=30, height=3, fg="royalblue",command=self.main_page)
        button_register.pack(pady=(50,0))
        
        redirect_logout = Button(self.root, text="Logout", bg="navyblue", fg="white", font=("helvetica",10), border=0, command=self.login_gui)
        redirect_logout.pack(pady=(70,0))
        
        
    def main_page(self):
        
        self.clear()
        
        self.root.configure(background = "navyblue")
        
        
        heading = Label(self.root, text = "NLP App", bg="navyblue", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font = ("helvetica",40,"bold"))
        
        label_text = Label(self.root, text="Enter text here:", bg="navyblue", fg="white", font=("helvetica",11,))
        label_text.pack()
        self.input_text = Text(self.root, width=40, height=10 )
        self.input_text.pack(pady=(5,0))
        
        button_analyze = Button(self.root, text="Analyze Sentiment", border=0, font=1, width=20, height=1, fg="royalblue",command=self.do_sentiment_analysis)
        button_analyze.pack(pady=(20,10))
        
        label_response = Label(self.root, text="Response", bg="navyblue", fg="white", font=("helvetica",11,))
        label_response.pack(pady=(20,0))
        self.response_text = Text(self.root, width=40, height=2 )
        self.response_text.pack(pady=(5,0))
        
        redirect_dashboard = Button(self.root, text="Go Back", bg="navyblue", fg="white", font=("helvetica",10), border=0, command=self.dashboard)
        redirect_dashboard.pack(pady=(70,0))
        
        
        
    def do_sentiment_analysis(self):
        
        text = self.input_text.get("1.0", "end-1c")
        print(text)
        response = self.apio.sentiment_response(text)
        self.response_text.insert("1.0",response)
        
    
    
    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()        
        password = self.password_input.get()
        
        response = self.dbo.add_data(name, email, password)
        if response == 1:
            messagebox.showinfo("Success","Registration Successfull")
        else:
            messagebox.showerror("Error","Email already exists!!")
       
        
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        
        response = self.dbo.search(email, password)
        if response == 1:
            messagebox.showinfo("Success","Login Successfull")
            self.dashboard()
        elif response == 0:
            messagebox.showerror("Error","Incorrect Password! Try again")
        else:
            messagebox.showerror("Error", "Email doesn't exist. Please Register")
        
    
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    
nlp = NLPApp()