import Tkinter as tk


def sclget(waaa):
    '''get scale and make it global'''
    waa = waaa
    waa = int(waa)
    global waa



def gamein():
    '''main game interface'''
    gme = tk.Tk()

    global gme
    gme.title("gme")
    print waa

    for i in range(1, waa + 1):
        for j in range(1, waa + 1):
            tmp = tk.Button(gme, width=4,height=2).grid(row=i, column=j)


    botn = tk.Button(gme,width=9,height=2,  text = 'Back', \
        command = tomain).grid(row=13, columnspan = 3, sticky = 'e')




def tomain():
    '''command Back to main m3nu'''
    print waa
    gme.destroy()
    main()

def togame():
    '''command Change to game'''
    gamein()
    root.destroy()



def main():
    '''main m3nu interface'''
    root = tk.Tk()
    global root
    root.title("rooooooot")
    sca = tk.Scale(root, sliderlength = 250/9 + 10, length = 250,\
 orient='horizontal', from_ = 3, to = 10, command = sclget)
    sca.grid(row=1, column=0)
    sca.set(waa)

    bot = tk.Button(root, width=10,height=2, text='Start', command=togame).grid(row=3, column=0)



root = tk.Tk()
global root
root.title("rooooooot")
sca = tk.Scale(root, sliderlength = 250/9 + 10, length = 250,\
 orient='horizontal', from_ = 3, to = 10, command = sclget)
sca.grid(row=1, column=0)

bot = tk.Button(root, width=10,height=2, text='Start', command=togame).grid(row=3, column=0)



#group = tk.LabelFrame(root, text="Example", padx=5, pady=5)
#group.grid(row=1, column=0)




root.mainloop()