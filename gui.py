import tkinter as tk
from PIL import ImageTk,Image


class MainGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.geometry('750x500')

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both",expand=1)


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.bg_image = ImageTk.PhotoImage(Image.open('photo.png'))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0)

        button1 = tk.Button(self, text="Go to Page One", command=lambda: master.switch_frame(PageOne))
        button1.pack()


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.bg_image = ImageTk.PhotoImage(Image.open('photo.png'))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0)

        tk.Button(self, text="Page 2",  command=lambda: master.switch_frame(PageTwo)).pack()


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.bg_image =ImageTk.PhotoImage(Image.open('photo.png'))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0)

        tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(StartPage)).pack()



app = MainGUI()
app.mainloop()