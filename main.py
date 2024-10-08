import tkinter as tk

hands_off_timer = None

def is_typing(event):
    global hands_off_timer

    if hands_off_timer:
        window.after_cancel(hands_off_timer)

    hands_off_timer = window.after(10000, not_typing)


def not_typing():
    # entry.delete(0, tk.END)
    text.delete('1.0', 'end')

def textbox_size(event): #supposed to add new height line but only adds more lines in scroll function
    textbox_content = text.get("1.0", 'end-1c')
    textbox_lines = textbox_content.splitlines()
    num_lines = len(textbox_lines)
    textbox_height = text.winfo_height() / text.winfo_fpixels("1.0")
    if num_lines > textbox_height:
        new_height = int(textbox_height + 1)
        text.config(height = new_height)
        window.update()


window = tk.Tk()
window.title("Disappearing Text")
window.config(padx=30, pady=30, bg='beige')
window.minsize(width=600, height=600)

label = tk.Label(window, text= "Type your thoughts below, but be warned!\n After 10 seconds of no typing your text will be deleted!", font=("Times", 24, 'bold italic'), fg= 'black',wraplength=600, bg='beige', highlightbackground='beige')
label.pack(pady=50)

#realized i needed a textbox not an entry to adjust initial height
# entry = tk.Entry(window, font=('Times', 24), fg='black', bg='beige', highlightbackground='beige', width=100)
# entry.pack(pady=30)

text = tk.Text(window, font=('Times', 24), height = 10, width=50, fg='black', bg='beige', highlightbackground='beige', wrap=tk.WORD)
text.pack(pady=30)

text.bind("<KeyPress>", is_typing)
text.bind("<KeyRelease>", textbox_size)
# entry.bind("<KeyPress>", is_typing)




window.mainloop()