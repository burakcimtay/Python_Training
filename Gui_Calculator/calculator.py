import tkinter as tk

calculation=""

def add(symbol):
    global calculation
    calculation += str(symbol)
    text.delete(1.0, "end")
    text.insert(1.0, calculation)
    

def evaluate():
    global calculation
    try:
        result = str(eval(calculation))
        calculation=""
        text.delete(1.0, "end")
        text.insert(1.0, result)
    
    except:
        clear()
        text.insert(1.0, "Error")

def clear():
    global calculation
    calculation=""
    text.delete(1.0, "end")
    pass

root=tk.Tk()
root.geometry("320x280")

text= tk.Text(root, height=2, width=17, font=("Arial", 24))
text.grid(columnspan=5)

btn_1=tk.Button(root, text="1", command=lambda: add("1"), width=5, font=("Arial", 14))
btn_1.grid(row=4, column=1)

btn_2=tk.Button(root, text="2", command=lambda: add("2"), width=5, font=("Arial", 14))
btn_2.grid(row=4, column=2)

btn_3=tk.Button(root, text="3", command=lambda: add("3"), width=5, font=("Arial", 14))
btn_3.grid(row=4, column=3)

btn_4=tk.Button(root, text="4", command=lambda: add("4"), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5=tk.Button(root, text="5", command=lambda: add("5"), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6=tk.Button(root, text="6", command=lambda: add("6"), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7=tk.Button(root, text="7", command=lambda: add("7"), width=5, font=("Arial", 14))
btn_7.grid(row=2, column=1)

btn_8=tk.Button(root, text="8", command=lambda: add("8"), width=5, font=("Arial", 14))
btn_8.grid(row=2, column=2)

btn_9=tk.Button(root, text="9", command=lambda: add("9"), width=5, font=("Arial", 14))
btn_9.grid(row=2, column=3)

btn_0=tk.Button(root, text="0", command=lambda: add("0"), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_plus=tk.Button(root, text="+", command=lambda: add("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=5, column=4)

btn_minus=tk.Button(root, text="-", command=lambda: add("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=4, column=4)

btn_div=tk.Button(root, text="/", command=lambda: add("/"), width=5, font=("Arial", 14))
btn_div.grid(row=2, column=4)

btn_mul=tk.Button(root, text="*", command=lambda: add("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=3, column=4)

btn_brcopen=tk.Button(root, text="(", command=lambda: add("("), width=5, font=("Arial", 14))
btn_brcopen.grid(row=5, column=1)

btn_brccls=tk.Button(root, text=")", command=lambda: add(")"), width=5, font=("Arial", 14))
btn_brccls.grid(row=5, column=3)

btn_eq=tk.Button(root, text="=", command=evaluate, width=5, font=("Arial", 14))
btn_eq.grid(row=6, column=3)

btn_clr=tk.Button(root, text="C", command=clear, width=5, font=("Arial", 14))
btn_clr.grid(row=6, column=1)

root.mainloop()