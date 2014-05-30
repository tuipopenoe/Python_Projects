""" Enables editing mp3 files to update information. """

from Tkinter import *
import fileinfo

class mp3edit():
    "MP3 Editing Application"

    if __name__ == "__main__":
        master = Tk()

        def callback(e):
            print e.get()

        canvas = Canvas(master, width = 400, height = 100)
        canvas.pack()

        entry = Entry(master)
        entry.pack()

        entry.focus_set()



        b = Button(master, text="Get", width=10, command=callback(entry))
        b.pack()

        mainloop()