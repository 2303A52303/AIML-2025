import tkinter as tk

root = tk.Tk()
root.title("Color Button Game")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

figure = canvas.create_rectangle(190, 190, 210, 210, fill="black")
def move_left():
    canvas.move(figure, -10, 0)

def move_right():
    canvas.move(figure, 10, 0)

def move_up():
    canvas.move(figure, 0, -10)

def move_down():
    canvas.move(figure, 0, 10)

btn_green = tk.Button(root, text="Green (Left)", bg="green", command=move_left)
btn_red = tk.Button(root, text="Red (Right)", bg="red", command=move_right)
btn_yellow = tk.Button(root, text="Yellow (Up)", bg="yellow", command=move_up)
btn_blue = tk.Button(root, text="Blue (Down)", bg="blue", command=move_down)

btn_green.pack(side=tk.LEFT, padx=20)
btn_red.pack(side=tk.RIGHT, padx=20)
btn_yellow.pack(side=tk.TOP, pady=20)
btn_blue.pack(side=tk.BOTTOM, pady=20)

root.mainloop()