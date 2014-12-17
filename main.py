'''Game BrickSweeper
by Boontarika Pochchongdach 57070061
   Uemporn Rakkamnoet 57070150'''

import Tkinter as tk
from random import randrange

def swit(m, b, x, y, s):
    '''function for change each button 
    get button name(inst, obj), pikat x(int, Btn.x), pikat y(int, Btn,y),
    state(int, dct[(x, y)]) -> 
    This func don't change state'''
    b = Btn(m, x, y, s)
    if b.state == 1:
        b.btn = tk.Button(m, width=4,height=2, text=b.state, \
            command=b.stat, bg='White', fg='Black').grid(row=b.x, column=b.y)
    else:
        b.btn = tk.Button(m, width=4,height=2, text=b.state, \
            command=b.stat, bg='Black', fg='White').grid(row=b.x, column=b.y)


class Btn(object):
    def __init__(self, mas, x, y, state=0):
        self.mas = mas
        self.x = x
        self.y = y
        self.state = state
        self.btn = tk.Button(self.mas, width=4,height=2, text=self.state, \
            command=self.stat, bg='Black', fg='White').grid(row=self.x, column=self.y)
    def __str__(self):
        return '(%d,%d) %d' % (self.x, self.y, self.state)

    def stat(self):
        '''when click  will go here to change state'''
        self.state = self.state ^ 1
        print 'Press  (%d,%d) %d' % (self.x, self.y, self.state)
        dct[(self.x, self.y)] = self.state
        swit(self.mas, self.btn, self.x, self.y, self.state)
        sidebtn(self.mas, self.x, self.y, self.state)


def sidebtn(m, x, y, s):
    '''change all side button state'''
#top zone
    if x - 1 != 0:
        top = Btn(m, x - 1, y)
        dct[(x-1, y)] = dct[(x-1, y)] ^ 1
        swit(m, top, x-1, y, dct[(x-1, y)])
#right zone
    if y + 1 != sze+1:
        rgh = Btn(m, x, y + 1)
        dct[(x, y+1)] = dct[(x, y+1)] ^ 1
        swit(m, rgh, x, y+1, dct[(x, y+1)])
#bottom zone yeye
    if x + 1 != sze+1:
        tom = Btn(m, x+1, y)
        dct[(x+1, y)] = dct[(x+1, y)] ^ 1
        swit(m, tom, x+1, y, dct[(x+1, y)])
#left zone
    if y - 1 != 0:
        lft = Btn(m, x, y-1)
        dct[(x, y-1)] = dct[(x, y-1)] ^ 1
        swit(m, lft, x, y-1, dct[(x, y-1)])

#Check Zone ----------------------
    if checker == True:
        chcklst = []
        for f in range(1, sze+1):
            for g in range(1, sze+1):
                chcklst.append(dct[(f, g)])
        if 0 not in chcklst:
            print '======1 Win======'
            winwindows(1, m)
        elif 1 not in chcklst:
            print '======0 Win======'
            winwindows(0, m)





def resetaction():
    '''action reset all button to 0'''
    for i in range(1, sze+1):
        for j in range(1, sze+1):
            a = Btn(prc, i, j)
            dct[(i, j)] = 0
    print 'Reset!'

def rantonaction():
    '''random one button at pratice mode'''
    aaa = randrange(1,sze+1)
    bbb = randrange(1,sze+1)
    print 'at (%d, %d)' % (aaa, bbb)
    dct[(aaa, bbb)] = dct[(aaa, bbb)] ^ 1
    tmp = Btn(prc, aaa, bbb, dct[(aaa, bbb)])
    swit(prc, tmp, aaa, bbb, dct[(aaa, bbb)]) 
    sidebtn(prc, aaa, bbb, dct[(aaa, bbb)])


#dict for save state
dct = {}
print 'Program Starto!!!!!'



def szeget(szea):
    '''get scale and make it global'''
    sze = szea
    sze = int(sze)
    global sze

def domget(dda):
    '''get random times and make it global'''
    dom = dda
    dom = int(dom)
    global dom

def tomain():
    '''command from game mode Back to main m3nu'''
    gme.destroy()
    main()

def tomain2():
    '''command from practice mode Back to main m3nu'''
    prc.destroy()
    main()

def tomain3():
    '''command from win game mode Back to main m3nu'''
    win.destroy()
    main()

def togame():
    '''command Change to game'''
    checker = True
    global checker
    gamein()
    root.destroy()
   
def repay():
    win.destroy()
    print 'replay'
    gamein()



def winwindows(numm, m):
    win = tk.Tk()
    m.destroy()
    global win
    win.title("End")
    if numm == 0:
    	winpnt = 'Black'
    else:
    	winpnt = 'White'
    show = tk.Label(win, text = 'Clear All Board to %s(%d), You Win!' % (winpnt, numm), \
    font = ("16") , padx = 10, pady = 15).pack(side = 'top')

    backbutton = tk.Button(win, width=12,height=2,  text ='Back To Menu', \
        command = tomain3, bg='Pink').pack(side = 'left')
    replaybutton = tk.Button(win, width=12,height=2,  text ='RePlay', \
        command = repay, bg='Green').pack(side = 'left')
    closebutton = tk.Button(win, width=12,height=2, text='Close! (X)', \
    	command= win.destroy , bg='Red', fg='Black').pack(side = 'left')


def pracin():
    '''pratice mode interface'''
#create button zone ^-^
    checker = False
    global checker
    root.destroy()
    prc = tk.Tk()
    global prc
    prc.title("Pratice")
    for i in range(1, sze + 1):
        for j in range(1, sze + 1):
            tmp = Btn(prc, i, j)
            dct[(i, j)] = 0
    backbutton = tk.Button(prc, width=8,height=2,  text ='(<) Back', \
        command = tomain2, bg='pink').grid(row=13, column = 1, columnspan = 2, sticky = 'w')

    resetbutton = tk.Button(prc, width=9,height=2, text='Reset!', command=resetaction, \
            bg='yellow', fg='Black').grid(row=1,column = 13)

    randombutton = tk.Button(prc, width=9,height=2, text='Random(1)', command = rantonaction, \
            bg='lightblue', fg='Black').grid(row=2 ,column = 13)


def gamein():
    '''main game interface'''
    gme = tk.Tk()

    global gme
    gme.title("Game")
    for v in range(1, sze + 1):
        for b in range(1, sze + 1):
            tmp = Btn(gme, v, b)

    for k in xrange(1,sze+1):
        for l in xrange(1,sze+1):
            dct[(k, l)] = 0

    for _ in xrange(dom):
        aaa = randrange(1, sze+1)
        bbb = randrange(1, sze+1)
        print 'at (%d, %d)' % (aaa, bbb)
        dct[(aaa, bbb)] = dct[(aaa, bbb)] ^ 1
        tmp = Btn(gme, aaa, bbb, dct[(aaa, bbb)])
        swit(gme, tmp, aaa, bbb, dct[(aaa, bbb)]) 
        sidebtn(gme, aaa, bbb, dct[(aaa, bbb)])

    print 'Randomed for %d round' % (dom)

    backbutton = tk.Button(gme, width=8,height=2,  text ='(<) Back', \
        command = tomain, bg='pink').grid(row=13, column = 1, columnspan = 2, sticky = 'w')


def main():
    '''main m3nu interface'''
    root = tk.Tk()
    global root
    root.title("Bricksweeper!!")

    name = tk.Label(root,text = 'BrickSweeper', font = ("Times", "24", "bold italic") )
    name.grid(row=0, column=0)
    
    group = tk.LabelFrame(root, text="Option", padx=5, pady=5)
    group.grid(row=1, column=0)

    dsca = tk.Scale(group, sliderlength = 250/20+ 10, length = 250,\
 orient='horizontal', from_ = 1, to = 50, command = domget, label = 'RandomRound')
    dsca.grid(row=2, columnspan = 20)
    dsca.set(dom)

    zsca = tk.Scale(group, sliderlength = 250/9 + 10, length = 250,\
 orient='horizontal', from_ = 3, to = 10, command = szeget, label = 'SquareSize')
    zsca.grid(row=3, columnspan = 20)
    zsca.set(sze)

    startbutton = tk.Button(root, width=10,height=2, text='Start Game', bg='green', command=togame).grid(row=4, column=0)

    particebutton = tk.Button(root, width=10,height=2, text='Pratice Mode', bg='orange', command=pracin).grid(row=5, column=0)

    closebutton = tk.Button(root, width=10,height=2, text='Close! (X)', command= root.destroy , \
            bg='Red', fg='Black').grid(row=6, column=0)

sze = 6
dom = 5
main()


root.mainloop()
