import tkinter as tk
from PIL import ImageTk,Image
import database as db
BUTTONHEIGHT=2
BUTTONWIDTH=30
FONT="Comic Sans MS"
BACKGROUNDIMG='photo.png'


class MainGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.geometry('750x500')
        self.title("FaceID Luncher")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both",expand=1)



class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #background image
        self.bg_image = ImageTk.PhotoImage(Image.open(BACKGROUNDIMG))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0)
        canvas=tk.Canvas(self,width=750,height=45,bg="black")
        canvas.place(x=0,y=0)

        #title
        text_canvas=canvas.create_text(320,5,anchor="nw",fill="white")
        canvas.itemconfig(text_canvas,text="Luncher",font = ((FONT),25))

        #buttons
        loginButton = tk.Button(self,height=BUTTONHEIGHT,width=BUTTONWIDTH, text="Login Page", command=lambda: master.switch_frame(LoginPage)
                            ,bg="white",fg="black", relief="solid",borderwidth=2,font = ((FONT),10))
        addUserButton = tk.Button(self,height=BUTTONHEIGHT,width=BUTTONWIDTH, text="Add User",command=lambda: master.switch_frame(RegPage)
                            ,bg="white",fg="black",relief="solid", borderwidth=2,font = ((FONT),10))
        loginButton.place(x=100,y=300)
        addUserButton.place(x=400,y=300)


class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        userLoginInput=tk.StringVar()
        userPassInput=tk.StringVar()
        #background image
        self.bg_image = ImageTk.PhotoImage(Image.open(BACKGROUNDIMG))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0)
        canvas=tk.Canvas(self,width=750,height=45,bg="black")
        canvas.place(x=0,y=0)

        #title
        text_canvas=canvas.create_text(320,5,anchor="nw",fill="white")
        canvas.itemconfig(text_canvas,text="Login Page",font = ((FONT),25))

        #buttons
        startButton = tk.Button(self,height=BUTTONHEIGHT,width=BUTTONWIDTH, text="Start Menu", command=lambda: master.switch_frame(StartPage)
                            ,bg="white",fg="black", relief="solid",borderwidth=2,font = ((FONT),10))
        addUserButton = tk.Button(self,height=BUTTONHEIGHT,width=BUTTONWIDTH, text="Add User",command=lambda: master.switch_frame(RegPage)
                            ,bg="white",fg="black",relief="solid", borderwidth=2,font = ((FONT),10))

        startButton.place(x=100,y=400)
        addUserButton.place(x=400,y=400)

        #login form
        loginText=tk.Label(self,text="Username",font = ((FONT),15))
        loginText.place(x=80,y=100,height=30,width=100)
        loginInput=tk.Entry(self,textvariable=userLoginInput)
        loginInput.place(x=200,y=100,height=30)

        passText=tk.Label(self,text="Password",font = ((FONT),15))
        passText.place(x=80,y=140,height=30,width=100)
        passInput=tk.Entry(self,textvariable=userPassInput)
        passInput.place(x=200,y=140,height=30)

        nextButton=tk.Button(self,height=BUTTONHEIGHT,width=BUTTONWIDTH, text="Next -> FaceID",command=lambda: db.login(userLoginInput.get(),userPassInput.get())
                            ,bg="white",fg="black",relief="solid", borderwidth=2,font = ((FONT),10))
        nextButton.place(x=150, y=180)


class RegPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #background image
        self.bg_image = ImageTk.PhotoImage(Image.open(BACKGROUNDIMG))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0)
        canvas=tk.Canvas(self,width=750,height=45,bg="black")
        canvas.place(x=0,y=0)

        #title
        text_canvas=canvas.create_text(320,5,anchor="nw",fill="white")
        canvas.itemconfig(text_canvas,text="Add User Page",font = ((FONT),25))

        #buttons
        loginButton = tk.Button(self,height=BUTTONHEIGHT,width=BUTTONWIDTH, text="Login", command=lambda: master.switch_frame(LoginPage)
                            ,bg="white",fg="black", relief="solid",borderwidth=2,font = ((FONT),10))
        startButton = tk.Button(self,height=BUTTONHEIGHT,width=BUTTONWIDTH, text="Start Menu",command=lambda: master.switch_frame(StartPage)
                            ,bg="white",fg="black",relief="solid", borderwidth=2,font = ((FONT),10))
        loginButton.place(x=100,y=400)
        startButton.place(x=400,y=400)



app = MainGUI()
app.mainloop()