import Tkinter as tk

root = tk.Tk()


class Btn(object):
    def __init__(self, x, y, state=0):
    	self.x = x
    	self.y = y
    	self.state = state
    	self.btn = tk.Button(width=2,height=1, text=self.state, command=self.stat, \
    		bg='Black', fg='White').grid(row=self.x, column=self.y)
    def __str__(self):
    	return '(%d,%d) %d' % (self.x, self.y, self.state)

    def stat(self):
    	'''when click  will go here to change state'''
    	self.state = self.state ^ 1
    	if self.state == 0:
    		self.btn = tk.Button(width=2,height=1, text=self.state, command=self.stat, \
    			bg='Black', fg='White').grid(row=self.x, column=self.y)
    	else:
    		self.btn = tk.Button(width=2,height=1, text=self.state, command=self.stat, \
    			bg='White', fg='Black').grid(row=self.x, column=self.y)

root.title("BrickSweeper!")

a = Btn(1, 1)
for i in range(1, 7):
	for j in range(1, 7):
		a = Btn(i, j)

root.mainloop()