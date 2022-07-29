import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Name",
    # foreground="white",  # Set the text color to white
    # background="black",  # Set the background color to blackp
    # width=30,
    # height=10p
)

# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )

entry = tk.Entry(
    # fg="yellow",
                 # bg="blue",
                 width=30)

label.pack()
# button.pack()
entry.pack()

# window.mainloop()

name = entry.get()
name

print(name)


# def leaveteams():
#     time.sleep(5)
#     pg.moveTo(3570, 615, 2)
#     pg.click(3570, 615)
#     time.sleep(2)
#     pg.moveTo(343, 552, 2)
#     pg.moveTo(200, 652, 1)
#     time.sleep(1)
