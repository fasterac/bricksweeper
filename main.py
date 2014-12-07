import Tkinter as tk
from random import randrange

root = tk.Tk()



def swit(b, x, y, s):
    '''function for change button 
    get button name(inst, obj), pikat x(int, Btn.x), pikat y(int, Btn,y),
    state(int, dct[(x, y)]) -> 
    This func don't change state'''
    b = Btn(x, y, s)
    if b.state == 1:
        b.btn = tk.Button(root, width=4,height=2, text=b.state, \
            command=b.stat, bg='White', fg='Black').grid(row=b.x, column=b.y)
    else:
        b.btn = tk.Button(root, width=4,height=2, text=b.state, \
            command=b.stat, bg='Black', fg='White').grid(row=b.x, column=b.y)





class Btn(object):
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self.state = state
        self.btn = tk.Button(root, width=4,height=2, text=self.state, \
            command=self.stat, bg='Black', fg='White').grid(row=self.x, column=self.y)
    def __str__(self):
        return '(%d,%d) %d' % (self.x, self.y, self.state)

    def stat(self):
        '''when click  will go here to change state'''
        self.state = self.state ^ 1
        sidebtn(self.x, self.y, self.state)
        print 'Press  (%d,%d) %d' % (self.x, self.y, self.state)
        dct[(self.x, self.y)] = self.state
        swit(self.btn, self.x, self.y, self.state)
        '''if self.state == 1:
            self.btn = tk.Button(root, width=4,height=2, text=self.state, \
                command=self.stat, bg='White', fg='Black').grid(row=self.x, column=self.y)
        else:
            self.btn = tk.Button(root, width=4,height=2, text=self.state, \
                command=self.stat, bg='Black', fg='White').grid(row=self.x, column=self.y)'''

root.title("BrickSweeper!")


def sidebtn(x, y, s):
    '''change all side button state'''
#top zone
    if x - 1 == 0:
        pass
    else:
        dct[(x-1, y)] = dct[(x-1, y)] ^ 1
        swit(top, x-1, y, dct[(x-1, y)])
        '''top = Btn(x-1, y, dct[(x-1, y)])

        if dct[(x-1, y)] == 1:        
            top.btn = tk.Button(root, width=4,height=2, text=dct[(x-1,y)], \
                command=top.stat, bg='White', fg='Black').grid(row=x-1, column=y)
            #print '^',top, '||',x-1, y, dct[(x-1, y)]
        else:
            top.btn = tk.Button(root, width=4,height=2, text=dct[(x-1,y)], \
                command=top.stat, bg='Black', fg='White').grid(row=x-1, column=y)'''
            #print '^',top, '||',x-1, y, dct[(x-1, y)]

#right zone
    if y + 1 == 7:
        pass
    else:
        dct[(x, y+1)] = dct[(x, y+1)] ^ 1
        swit(rgh, x, y+1, dct[(x, y+1)])
        '''rgh = Btn(x, y+1, dct[(x, y+1)])

        if dct[(x, y+1)] == 1:        
            rgh.btn = tk.Button(root, width=4,height=2, text=dct[(x, y+1)], \
                command=rgh.stat, bg='White', fg='Black').grid(row=x, column=y+1)
            #print '>',rgh, '||',x, y+1, dct[(x, y+1)]
        else:
            rgh.btn = tk.Button(root, width=4,height=2, text=dct[(x, y+1)], \
                command=rgh.stat, bg='Black', fg='White').grid(row=x, column=y+1)'''
            #print '>',rgh, '||',x, y+1, dct[(x, y+1)]

#bottom zone yeye
    if x + 1 == 7:
        pass
    else:
        dct[(x+1, y)] = dct[(x+1, y)] ^ 1
        swit(tom, x+1, y, dct[(x+1, y)])
        '''tom = Btn(x+1, y, dct[(x+1, y)])

        if dct[(x+1, y)] == 1:        
            tom.btn = tk.Button(root, width=4,height=2, text=dct[(x+1,y)], \
                command=tom.stat, bg='White', fg='Black').grid(row=x+1, column=y)
            #print 'v',tom, '||',x+1, y, dct[(x+1, y)]
        else:
            tom.btn = tk.Button(root, width=4,height=2, text=dct[(x+1,y)], \
                command=tom.stat, bg='Black', fg='White').grid(row=x+1, column=y)'''
            #print 'v',tom, '||',x+1, y, dct[(x+1, y)]

#left zone
    if y - 1 == 0:
        pass
    else:
        dct[(x, y-1)] = dct[(x, y-1)] ^ 1
        swit(lft, x, y-1, dct[(x, y-1)])
        '''lft = Btn(x, y-1, dct[(x, y-1)])

        if dct[(x, y-1)] == 1:        
            lft.btn = tk.Button(root, width=4,height=2, text=dct[(x, y-1)], \
                command=lft.stat, bg='White', fg='Black').grid(row=x, column=y-1)
            #print '<',lft, '||',x, y-1, dct[(x, y-1)]
        else:
            lft.btn = tk.Button(root, width=4,height=2, text=dct[(x, y-1)], \
                command=lft.stat, bg='Black', fg='White').grid(row=x, column=y-1)'''
            #print '<',lft, '||',x, y-1, dct[(x, y-1)]




print 'Program Starto!!!!!'
top = Btn(1, 2)
rgh = Btn(2, 3)
tom = Btn(3, 2)
lft = Btn(2, 1)
tmp = Btn(2, 2)



#dict for save state
dct = {}

#create button zone ^-^
for i in range(1, 7):
    for j in range(1, 7):
        a = Btn(i, j)
        dct[(i, j)] = 0







def debug():
    '''reprint button from dict ....mai bug leaw'''
    print 'de"BUG"ging.. (reprint)'
    for t in range(1, 7):
        for r in range(1, 7):
            swit(tmp, t, r, dct[(t, r)])

debugbutton = tk.Button(root, width=4,height=1, text='De\n"BUG"', command=debug,\
    bg='Purple', fg='Black').grid(row=8, column=1)








#Random path =_+
def ranton():
    '''random any button 1 time'''
    aaa = randrange(1,7)
    bbb = randrange(1,7)
    print 'at (%d, %d)' % (aaa, bbb)
    dct[(aaa, bbb)] = dct[(aaa, bbb)] ^ 1
    tmp = Btn(aaa, bbb, dct[(aaa, bbb)])
    if dct[(aaa, bbb)] == 0:
        tmp.btn = tk.Button(root, width=4,height=2, text=tmp.state, \
            command=tmp.stat, bg='Black', fg='White').grid(row=aaa, column=bbb)
    else:
        tmp.btn = tk.Button(root, width=4,height=2, text=tmp.state, \
            command=tmp.stat, bg='White', fg='Black').grid(row=aaa, column=bbb)  
    sidebtn(aaa, bbb, dct[(aaa, bbb)])

randombutton = tk.Button(root, width=10,height=2, text='Random', command=ranton,\
    bg='Yellow', fg='Black').grid(row=6, column=7)









#printbutton
def pntdct():
    '''print for check state ......yiemgood!!'''
    for q in range(1, 7):
        print ''
        for w in range(1, 7):
            print dct[(q, w)],
    print '\n'

checkstatebutton = tk.Button(width=10,height=2, text='CheckState', command=pntdct, \
            bg='DarkGreen', fg='White').grid(row=7, column=7)








#reset!!!!! to 0
def resetaction():
    for i in range(1, 7):
        for j in range(1, 7):
            a = Btn(i, j)
            dct[(i, j)] = 0
    print 'Reset!'
resetbutton = tk.Button(width=10,height=2, text='Reset!', command=resetaction, \
            bg='Red', fg='Black').grid(row=4, column=7)





def shuff():
    for i in range(5):
        print 'randoming',i ,
        ranton()


shuffelbutton = tk.Button(width=10,height=2, text='Shuffel!', command=shuff, \
            bg='Orange', fg='Black').grid(row=5, column=7)











def ose():
    '''close windows ...pid nannnn muakkkk'''
    print 'Closing Game Please Wait......\n\
    >>>  If you press too many times. It may take several minutes.  <<<'
    
    denk = tk.Tk()
    text = tk.Label(denk, text='Closing Game Please Wait......').pack()

    root.destroy()
    denk.destroy()
    denk.mainloop()
    

closebutton = tk.Button(root, width=10,height=2, text='Close! (X)', command=ose, \
            bg='DarkRed', fg='Black').grid(row=1, column=7)



def setbut():
    '''unavalible now'''
    top = Btn(1, 2)
    rgh = Btn(2, 3)
    tom = Btn(3, 2)
    lft = Btn(2, 1)
    tmp = Btn(2, 2)
setbutton = tk.Button(root, width=4,height=1, text='Set', command=setbut, \
            bg='LightBlue', fg='Black').grid(row=8, column=2)



root.mainloop()