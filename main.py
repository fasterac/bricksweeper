import Tkinter as tk

root = tk.Tk()


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
        if self.state == 0:
            self.btn = tk.Button(root, width=4,height=2, text=self.state, \
                command=self.stat, bg='Black', fg='White').grid(row=self.x, column=self.y)
        else:
            self.btn = tk.Button(root, width=4,height=2, text=self.state, \
                command=self.stat, bg='White', fg='Black').grid(row=self.x, column=self.y)

root.title("BrickSweeper!")


def sidebtn(x, y, s):
    '''change (only) bottom button state (this is test version)'''
    print '+ (%d,%d) %d' % (x, y, s)
    dct[(x, y)] = s

#top zone
    if x - 1 == 0:
        pass
    else:
        dct[(x-1, y)] = dct[(x-1, y)] ^ 1
        top = Btn(x-1, y, dct[(x-1, y)])

        if dct[(x-1, y)] == 1:        
            top.btn = tk.Button(width=4,height=2, text=dct[(x-1,y)], command=top.stat, \
                    bg='White', fg='Black').grid(row=x-1, column=y)
            print '^',top, '||',x-1, y, dct[(x-1, y)]
        else:
            top.btn = tk.Button(width=4,height=2, text=dct[(x-1,y)], command=top.stat, \
                bg='Black', fg='White').grid(row=x-1, column=y)
            print '^',top, '||',x-1, y, dct[(x-1, y)]

#right zone
    if y + 1 == 7:
        pass
    else:
        dct[(x, y+1)] = dct[(x, y+1)] ^ 1
        rgh = Btn(x, y+1, dct[(x, y+1)])

        if dct[(x, y+1)] == 1:        
            rgh.btn = tk.Button(width=4,height=2, text=dct[(x, y+1)], command=rgh.stat, \
                    bg='White', fg='Black').grid(row=x, column=y+1)
            print '>',rgh, '||',x, y+1, dct[(x, y+1)]
        else:
            rgh.btn = tk.Button(width=4,height=2, text=dct[(x, y+1)], command=rgh.stat, \
                bg='Black', fg='White').grid(row=x, column=y+1)
            print '>',rgh, '||',x, y+1, dct[(x, y+1)]

#bottom zone yeye
    if x + 1 == 7:
        pass
    else:
        dct[(x+1, y)] = dct[(x+1, y)] ^ 1
        tom = Btn(x+1, y, dct[(x+1, y)])

        if dct[(x+1, y)] == 1:        
            tom.btn = tk.Button(width=4,height=2, text=dct[(x+1,y)], command=tom.stat, \
                    bg='White', fg='Black').grid(row=x+1, column=y)
            print 'v',tom, '||',x+1, y, dct[(x+1, y)]
        else:
            tom.btn = tk.Button(width=4,height=2, text=dct[(x+1,y)], command=tom.stat, \
                bg='Black', fg='White').grid(row=x+1, column=y)
            print 'v',tom, '||',x+1, y, dct[(x+1, y)]

#left zone
    if y - 1 == 0:
        pass
    else:
        dct[(x, y-1)] = dct[(x, y-1)] ^ 1
        lft = Btn(x, y-1, dct[(x, y-1)])

        if dct[(x, y-1)] == 1:        
            lft.btn = tk.Button(width=4,height=2, text=dct[(x, y-1)], command=lft.stat, \
                    bg='White', fg='Black').grid(row=x, column=y-1)
            print '<',lft, '||',x, y-1, dct[(x, y-1)]
        else:
            lft.btn = tk.Button(width=4,height=2, text=dct[(x, y-1)], command=lft.stat, \
                bg='Black', fg='White').grid(row=x, column=y-1)
            print '<',lft, '||',x, y-1, dct[(x, y-1)]



print 'Program Starto!!!!!'
top = Btn(1, 2)
rgh = Btn(2, 3)
tom = Btn(3, 2)
lft = Btn(2, 1)


#dict for save state
dct = {}

#create button zone ^-^
for i in range(1, 7):
    for j in range(1, 7):
        a = Btn(i, j)
        dct[(i, j)] = 0



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
resetbutton = tk.Button(width=10,height=2, text='Reset!', command=resetaction, \
            bg='DarkRed', fg='Black').grid(row=6, column=7)    



root.mainloop()