"""Tkinter test coner"""

from Tkinter import *

root = Tk()
root.title("PressSweeper!")
#0 = khaw , 1 = damm
d11 = 1
def c11a():
    psd = '11'
    d11 = 1
    global d11
    print d11
    prsed(psd)
def c11b():
    psd = '11'
    d11 = 0
    global d11
    print d11
    prsed(psd)

    
    

def prsed(psd):
    if d11 == 0:
        b11 = Button(text='X', command=c11a, bg='Black', fg='White',).grid(row=1, column=1)
        #pum khaw state = 0 -- kod command ja pen dumm
    if d11 == 1:
        b11 = Button(root,text='O', command=c11b,bg='White',).grid(row=1, column=1)

    


#Label
l_nya = Label(text='BAKAAAAAAAAAAA').grid(row=0)

#Entry
#e_nya = Entry(root).grid(row=2, sticky='E'+'W')

#Button set
b11 = Button(root,text='O', bg='White', command=c11b).grid(row=1, column=1)
b12 = Button(root,text='O', bg='White').grid(row=1, column=2)
b13 = Button(root,text='O', bg='White').grid(row=1, column=3)
b14 = Button(root,text='O', bg='White').grid(row=1, column=4)
b15 = Button(root,text='O', bg='White').grid(row=1, column=5)
b16 = Button(root,text='O', bg='White').grid(row=1, column=6)

b21 = Button(root,text='O', bg='White').grid(row=2, column=1)
b22 = Button(root,text='O', bg='White').grid(row=2, column=2)
b23 = Button(root,text='O', bg='White').grid(row=2, column=3)
b24 = Button(root,text='O', bg='White').grid(row=2, column=4)
b25 = Button(root,text='O', bg='White').grid(row=2, column=5)
b26 = Button(root,text='O', bg='White').grid(row=2, column=6)

b31 = Button(root,text='O', bg='White').grid(row=3, column=1)
b32 = Button(root,text='O', bg='White').grid(row=3, column=2)
b33 = Button(root,text='O', bg='White').grid(row=3, column=3)
b34 = Button(root,text='O', bg='White').grid(row=3, column=4)
b35 = Button(root,text='O', bg='White').grid(row=3, column=5)
b36 = Button(root,text='O', bg='White').grid(row=3, column=6)








##nya = Button(root, text='NNNya').grid(row=1, column=0)
##baka_nya = Button(root, text='BAKA Desu ka?')
##baka_nya.grid(row=1, column=1)
##a_nya = Button(root, text='Nyaa').grid(row=3, column=1, sticky='E'+'W')
##b_nya = Button(root, text='Nya').grid(row=4, column=2)
##exit_nya = Button(root, text='Bye~', command=root.destroy, fg='Blue', bg='#FFFFFF')
##exit_nya.grid(row=5, column=1, sticky='W'+'E'+'N')


root.mainloop()


'''
.pack() Test

#Button set
b_exit = Button(root, text='Exit', command=root.destroy).pack(side='right')
b_start = Button(root, text='Start').pack(side='left')
b_reset = Button(root, text='Reset').pack(fill='x')

#Label
l_nya = Label(text='Nya nya nyaaaa').pack()
l_nya2 = Label(text='Nyaaaaa').pack()
'''
