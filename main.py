from tkinter import *
import calendar

# Function to show the calender of a given year
def show_calender():
    new_window = Tk()
    new_window.config(background = "white")
    new_window.title("MY CALENDAR")
    new_window.geometry("500x500")
    get_year = int(year_input.get())
    cal_content = calendar.calendar(get_year)
    cal_year = Label(new_window, text=cal_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    new_window.mainloop()
     








# Creating main window
root = Tk()
root.config(background="pink")
root.title("My Calendar")
root.geometry("300x300")
cal = Label(root, text="CALENDAR", bg="light gray",
            font=("times", 28, 'bold'))
year = Label(root, text="Enter Year: ", bg="dark green")
year_input = Entry(root)
show_btn= Button(root, text="Show Calendar", fg="Black",
              bg="Red", command=show_calender)
exit_btn = Button(root, text="Exit", fg="Black", bg="Red", command=exit)
cal.grid(row=1, column=1, pady=10)

year.grid(row=2, column=1, pady=10)

year_input.grid(row=3, column=1, pady=10)

show_btn.grid(row=4, column=1, pady=10)

exit_btn.grid(row=6, column=1, pady=10)

# start the GUI
root.mainloop()




