'''import Tkinter as tk
root = tk.Tk()
root.title("Test")

def varue():
    print var.get()

def gth():
    print '...'
    print var.get()

var = tk.IntVar()

group1 = tk.LabelFrame(root, text="Group1", padx=5, pady=5, )
group1.grid(row=0, column=0)

bbb = tk.Button(root, width=4,height=2, command = gth()).grid(row=1, column=2)
ccc = tk.Checkbutton(root, text="Expand").grid(row=1, column=3)
ddd = tk.Label(root, text = 'Value =' + str(var.get())).grid(row=1, column=4)


group2 = tk.LabelFrame(root, text="goup 2", padx=5, pady=5, )
group2.grid(row=10, column=0)

aaa = tk.Scale(root,variable = var, sliderlength = 250/9 + 10, length = 250,\
 orient='horizontal', from_ = 1, to = 10, command = varue()).grid(row=1, column=5)


root.mainloop()'''

import Tkinter as tk


def sclget(waaa):
    '''get scale and make it global'''
    waa = waaa
    global waa

def togame():
    gme = tk.Tk()

    global gme
    gme.title("gme")
    botn = tk.Button(gme,width=4,height=2, command = main1).grid(row=3, column=0)

def main1():
    print waa
    gme.destroy()
    main()

def mian():
    togame()
    root.destroy()


def main():
    root = tk.Tk()
    global root
    root.title("rooooooot")
    sca = tk.Scale(root, sliderlength = 250/9 + 10, length = 250,\
 orient='horizontal', from_ = 1, to = 10, command = sclget)
    sca.grid(row=1, column=0)
    sca.set(waa)

    bot = tk.Button(root, text = 'Start', command = mian).grid(row=3, column=0)



root = tk.Tk()

root.title("root")
sca = tk.Scale(root, sliderlength = 250/9 + 10, length = 250,\
 orient='horizontal', from_ = 1, to = 10, command = sclget)
sca.grid(row=1, column=0)


bot = tk.Button(root, text = 'Start', command = mian).grid(row=3, column=0)


#group = tk.LabelFrame(root, text="Example", padx=5, pady=5)
#group.grid(row=1, column=0)




root.mainloop()