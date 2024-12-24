import tkinter as tk

root = tk.Tk()
root.geometry('500x400')
root.title('Tkinter Switch')


options_frame = tk.Frame(root, bg="#c3c3c3")

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)


main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=400)

def home_page():
    home_frame = tk.Frame(main_frame)
    home_frame.pack(pady=20)
    l1 = tk.Label(home_frame, text="Home\n\nPag 1")
    l1.pack()

def eliminar_frames():
    for frame in main_frame.winfo_children():
        frame.destroy()

def menu_page():
    menu_frame = tk.Frame(main_frame)
    menu_frame.pack(pady=20)
    l1 = tk.Label(menu_frame, text="Menu\n\nPag 2")
    l1.pack()

def contact_page():
    contact_frame = tk.Frame(main_frame)
    contact_frame.pack(pady=20)
    l1 = tk.Label(contact_frame, text="Contact\n\nPag 3")
    l1.pack()

def about_page():
    about_frame = tk.Frame(main_frame)
    about_frame.pack(pady=20)
    l1 = tk.Label(about_frame, text="About\n\nPag 4")
    l1.pack()

def desaparecer_ind():
    home_indicate.configure(bg='#c3c3c3')
    menu_indicate.configure(bg='#c3c3c3')
    contact_indicate.configure(bg='#c3c3c3')
    about_indicate.configure(bg='#c3c3c3')

def indicador(lb, page):
    desaparecer_ind()
    lb.configure(bg="#158aff")
    eliminar_frames()
    page()


home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicador(home_indicate, home_page))
home_btn.place(x=10, y=50)
home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3, y=50, width=5, height=40)

menu_btn = tk.Button(options_frame, text='Menu', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicador(menu_indicate, menu_page))
menu_btn.place(x=10, y=100)
menu_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
menu_indicate.place(x=3, y=100, width=5, height=40)

contact_btn = tk.Button(options_frame, text='Contact', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicador(contact_indicate, contact_page))
contact_btn.place(x=10, y=150)
contact_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
contact_indicate.place(x=3, y=150, width=5, height=40)


about_btn = tk.Button(options_frame, text='About', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicador(about_indicate, about_page))
about_btn.place(x=10, y=200)
about_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
about_indicate.place(x=3, y=200, width=5, height=40)





root.mainloop()