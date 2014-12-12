'''add Pratice mode'''
import Tkinter as tk


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
        sidebtn(self.mas, self.x, self.y, self.state)
        print 'Press  (%d,%d) %d' % (self.x, self.y, self.state)
        dct[(self.x, self.y)] = self.state
        swit(self.mas, self.btn, self.x, self.y, self.state)


def sidebtn(m, x, y, s):
    '''change all side button state'''
#top zone
    if x - 1 == 0:
        pass
    else:
        top = Btn(m, x - 1, y)
        dct[(x-1, y)] = dct[(x-1, y)] ^ 1
        swit(m, top, x-1, y, dct[(x-1, y)])
#right zone
    if y + 1 == sze+1:
        pass
    else:
        rgh = Btn(m, x, y + 1)
        dct[(x, y+1)] = dct[(x, y+1)] ^ 1
        swit(m, rgh, x, y+1, dct[(x, y+1)])
#bottom zone yeye
    if x + 1 == sze+1:
        pass
    else:
        tom = Btn(m, x+1, y)
        dct[(x+1, y)] = dct[(x+1, y)] ^ 1
        swit(m, tom, x+1, y, dct[(x+1, y)])
#left zone
    if y - 1 == 0:
        pass
    else:
        lft = Btn(m, x, y-1)
        dct[(x, y-1)] = dct[(x, y-1)] ^ 1
        swit(m, lft, x, y-1, dct[(x, y-1)])



#dict for save state
dct = {}

print 'Program Starto!!!!!'








def szeget(szea):
    '''get scale and make it global'''
    sze = szea
    sze = int(sze)
    global sze


def tomain():
    '''command Back to main m3nu'''
    gme.destroy()
    main()

def tomain2():
    '''command Back to main m3nu'''
    prc.destroy()
    main()

def togame():
    '''command Change to game'''
    gamein()
    root.destroy()









def pracin():
    '''pratice mode interface'''
#create button zone ^-^
    root.destroy()
    prc = tk.Tk()
    global prc
    for i in range(1, sze + 1):
        for j in range(1, sze + 1):
            tmp = Btn(prc, i, j)
            dct[(i, j)] = 0
    backbutton = tk.Button(prc, width=9,height=2,  text = 'Back', \
        command = tomain2).grid(row=13, columnspan = 3, sticky = 'e')



def gamein():
    '''main game interface'''
    gme = tk.Tk()

    global gme
    gme.title("gme")
    print sze

    for i in range(1, sze + 1):
        for j in range(1, sze + 1):
            tmp = tk.Button(gme, width=4,height=2).grid(row=i, column=j)


    backbutton = tk.Button(gme,width=9,height=2,  text = 'Back', \
        command = tomain).grid(row=13, columnspan = 3, sticky = 'e')



def main():
    '''main m3nu interface'''
    root = tk.Tk()
    global root
    root.title("rooooooot")

    group = tk.LabelFrame(root, text="Option", padx=5, pady=5)
    group.grid(row=0, column=0)

    zsca = tk.Scale(group, sliderlength = 250/9 + 10, length = 250,\
 orient='horizontal', from_ = 3, to = 10, command = szeget, label = 'SquareSize')
    zsca.grid(row=1, columnspan = 20)
    zsca.set(sze)

    startbutton = tk.Button(root, width=10,height=2, text='Start Game', bg='green', command=togame).grid(row=3, column=0)

    particebutton = tk.Button(root, width=10,height=2, text='Pratice Mode', bg='orange', command=pracin).grid(row=4, column=0)

    def ose():
        root.destroy()    
    closebutton = tk.Button(root, width=10,height=2, text='Close! (X)', command=ose, \
            bg='DarkRed', fg='Black').grid(row=5, column=0)

sze = 6
main()

#group = tk.LabelFrame(root, text="Example", padx=5, pady=5)
#group.grid(row=1, column=0)




root.mainloop()