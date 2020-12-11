from tkinter import *


def button_clicked():
    text1 = int(miles_entry.get()) * 1.60934
    km_label.config(text=str(text1))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=5, pady=50)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_label.grid(column=0, row=1)

km_label = Label(text="0", font=("Arial", 24, "bold"))
km_label.grid(column=1, row=1)

km_label1 = Label(text="Km", font=("Arial", 24, "bold"))
km_label1.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)


window.mainloop()
