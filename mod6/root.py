import tkinter

root = tkinter.Tk()
# root2 = tkinter.Tk()
root.geometry('250x250')
root.title('ТЕСТ')
root.resizable(False,False)

te = 0
def test():
    global te
    te += 1
    ent['text'] = te
# lbl = tkinter.Label(master=root, text='Проверка', font=("Arial", 16,'bold'), bg='green', fg='red', width=10, height=10, anchor='s', relief='groove', bd=10, justify='center')
# lbl.pack()
    
def test2():
    test = ent2.get()
    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write(f'{test} \n')
    print(f'{test} \n')

ent = tkinter.Label(master=root, width=30)
ent.pack(pady=10)
btn = tkinter.Button(text='Довавить +1', command=test)
btn.pack()


ent2 = tkinter.Entry(root, width=30)
ent2.pack(pady=10)
btn2 = tkinter.Button(text='Довавить +1', command=test2)
btn2.pack()
tkinter.mainloop()