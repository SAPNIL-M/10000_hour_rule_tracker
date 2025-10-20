import tkinter as tk

click_count=0
def handle_click():
    global click_count
    click_count += 1
    lbl_count.config(text=f"clicks:{click_count}")
    print(f"Buttom clicked! count is now {click_count}")

def rst():
    global click_count
    click_count = 0
    lbl_count.config(text=f"clicks:{click_count}")


window = tk.Tk()
window.title("my first gui")
window.geometry("300x300")

lbl_count = tk.Label(master=window, text="count:0")
btn_click = tk.Button(master=window,text="click me")
rst_btn=tk.Button(master=window,text="reset button")
btn_click.config(command=handle_click)
rst_btn.config(command=rst)

rst_btn.pack(pady=20)
lbl_count.pack(pady=20)
btn_click.pack()


window.mainloop()