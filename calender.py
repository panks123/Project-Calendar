from tkinter import *
import calendar
import tkinter.messagebox as tmsg

# Function for showing the calendar of the given year
def showCal():
    # Create a GUI window
    new_gui = Tk()

    # Set the background colour of GUI window
    new_gui.config(background="white")

    # set the name of tkinter GUI window
    new_gui.title("CALENDER")
    new_gui.wm_iconbitmap("calendar.ico")

    # Set the configuration of GUI window
    new_gui.geometry("550x600")

    # get method returns current text as string
    fetch_year = year_field.get()
    if fetch_year=='':
        tmsg.showerror("Invalid year")
        new_gui.destroy()
    else:
        fetch_year=int(fetch_year)
    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)

    # Create a label for showing the content of the calender
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.pack(fill=BOTH,expand=True)

    # start the GUI
    new_gui.mainloop()


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background="white")

    # set the name of tkinter GUI window
    gui.title("CALENDER")
    gui.wm_iconbitmap("calendar.ico")
    # Set the configuration of GUI window
    gui.geometry("400x300")

    # Create a CALENDAR : label with specified font and size
    cal = Label(gui, text="CALENDAR",font=("times", 30, 'bold'))

    # Create a Enter Year : label
    year = Label(gui, text="Enter Year", bg="light green")

    # Create a text entry box for filling or typing the information.
    year_field = Entry(gui,font="times 16")

    # Create a Show Calendar Button and attached to showCal function
    Show = Button(gui, text="Show Calendar", fg="Black",
                  bg="Red", command=showCal)

    # Create a Exit Button and attached to exit function
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row=1, column=1,pady=20)

    year.grid(row=2, column=1,pady=10)

    year_field.grid(row=3, column=1,pady=10)

    Show.grid(row=4, column=1,pady=10)

    Exit.grid(row=6, column=1,pady=10)

    # start the GUI
    gui.mainloop()

