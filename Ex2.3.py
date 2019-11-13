import tkinter as tk
from random import randint
import copy
from time import sleep


class Board:
    def __init__(self, size=10, time_st=0.1):
        self.N = size
        self.time_st = time_st
        self.cells = {}
        self.POLE = {}
        self.OLDPOLE = {}
        self.GRANDPOLE = {}
        self.root = tk.Tk()
        self.root.title('Game process')
        self.cell_size = 10
        self.width = self.N * self.cell_size
        self.life = 'black'
        self.death = 'white'
        self.nums = tk.IntVar()
        self.nums.set(0)
        self.loop = tk.IntVar()
        self.loop.set(1)
        self.alive = tk.IntVar()
        self.alive.set(0)
        self.slab = tk.Label(self.root, bg='white', width=50, text='Score')
        self.slab.pack(side=tk.TOP)
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.width)
        self.canvas.pack(side=tk.LEFT)
        self.canvas.bind('<ButtonPress-1>', self.redraw)
        self.canvas.bind('<ButtonPress-3>', self.redraw)
        for i in range(self.N):
            for j in range(self.N):
                pos = (i, j)
                self.POLE[pos] = False
                x1 = self.cell_size * j
                y1 = self.cell_size * i
                x2 = self.cell_size + self.cell_size * j
                y2 = self.cell_size + self.cell_size * i
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, outline='grey', width=1, fill='white', tag=pos)
                self.canvas.itemconfig(rect, state=tk.NORMAL)
                self.cells[pos] = [rect, False]

        self.random_but = tk.Button(self.root, width=self.N, text='RANDOM', command=self.brandom)
        self.random_but.pack(fill=tk.X)

        self.run_but = tk.Button(self.root, width=self.N, text='RUN', command=self.run)
        self.run_but.pack(expand=1, fill=tk.X)

        self.root.mainloop()

    def redraw(self, event):
        jj = int(event.x / self.cell_size)
        ii = int(event.y / self.cell_size)
        pos = (ii, jj)
        if event.num == 1:
            color = self.life
            self.cells[pos][-1] = True
        elif event.num == 3:
            color = self.death
            self.cells[pos][-1] = False
        self.canvas.itemconfig(self.cells[pos][0], fill=color)

    def brandom(self):
        t = 0
        for i in range(self.N):
            for j in range(self.N):
                pos = (i, j)
                self.cells[pos][-1] = bool(randint(False, True))
                if self.cells[pos][-1]:
                    t += 1
                    color = self.life
                else:
                    color = self.death
                self.canvas.itemconfig(self.cells[pos][0], fill=color)
        self.alive.set(str(t))
        self.run_but.config(state=tk.NORMAL)
        self.slab.config(text='Generation %s. There are %s creatures' % (self.loop.get(), self.alive.get()))

    def clear(self):
        for i in range(self.N):
            for j in range(self.N):
                pos = (i, j)
                self.cells[pos][-1] = False
                self.canvas.itemconfig(self.cells[pos][0], fill=self.death)

    def dead_or_alive(self, pos):
        self.neibs = []
        for i in range(-1, 2, 1):
            posx = pos[0] + i
            for j in range(-1, 2, 1):
                posy = pos[-1] + j
                if (posx < 0 or posy < 0) or (posx > self.N - 1 or posy > self.N - 1):
                    continue
                else:
                    self.neibs.append((posx, posy))

        self.neibs.remove(pos)
        neib = 0
        for i in self.neibs:
            if self.OLDPOLE[i]:
                neib += 1
        if self.OLDPOLE[pos]:
            if neib == 2 or neib == 3:
                state = True
            else:
                state = False
        else:
            if neib == 3:
                state = True
            else:
                state = False
        return state

    def run(self):
        self.random_but.config(text='QUIT', command=lambda: self.root.destroy())
        self.run_but.config(state=tk.DISABLED)
        game = True
        while game:
            t = 0
            self.loop.set(int(self.loop.get()) + 1)
            for i in range(self.N):
                for j in range(self.N):
                    pos = (i, j)
                    self.POLE[pos] = self.cells[pos][-1]
            self.OLDPOLE = copy.deepcopy(self.POLE)

            if int(self.loop.get()) % 2 == 0:
                self.GRANDPOLE = copy.deepcopy(self.POLE)

            for i in range(self.N):
                for j in range(self.N):
                    pos = (i, j)
                    self.cells[pos][-1] = self.dead_or_alive(pos)
                    self.POLE[pos] = self.cells[pos][-1]
                    if self.cells[pos][-1]:
                        color = self.life
                        t += 1
                    else:
                        color = self.death
                    self.canvas.itemconfig(self.cells[pos][0], fill=color)

            self.alive.set(t)
            msg = 'Generation %s. There are %s creatures' % (self.loop.get(), self.alive.get())
            self.slab.config(text=msg)
            self.root.update()
            sleep(self.time_st)

            if int(self.alive.get()) == 0:
                msg = 'All cells are dead!'
                self.slab.config(text='Game Over %s' % msg)
                self.run_but.config(state=tk.NORMAL, text='RESTART', command=self.restart)
                game = False

            elif self.OLDPOLE == self.POLE:
                msg = 'in %s generations. Still alive %s cells' % (self.loop.get(), self.alive.get())
                self.slab.config(text='Game Over %s' % msg)
                self.run_but.config(state=tk.NORMAL, text='RESTART', command=self.restart)
                game = False

            elif self.GRANDPOLE == self.POLE:
                msg = 'Generation %s reaches a stable form of life for %s cells' % (self.loop.get(), self.alive.get())
                self.slab.config(text='Game Over %s' % msg)
                self.run_but.config(state=tk.NORMAL, text='RESTART', command=self.restart)
                game = False

    def restart(self):
        self.clear()
        msg = 'Select initial colony'
        self.slab.config(text='%s' % msg)
        self.random_but.config(text='RANDOM', state=tk.NORMAL, command=self.brandom)
        self.run_but.config(text='RUN LIFE', state=tk.NORMAL, command=self.run)
        self.loop.set(1)
        self.alive.set(0)


def create_board(pos):
    bsize = pos[0]
    tsize = pos[1]
    s = bsize.get()
    spd = [0.3, 0.2, 0.15, 0.1, 0.05, 0.025]
    t = spd[tsize.get()]
    Board(s, t)


def new_game():
    main = tk.Tk()
    main.title('LIFE')
    slab = tk.Label(main, text="Game of Life \n ")
    slab.pack()
    bsize = tk.IntVar()
    bsize.set(20)
    tsize = tk.IntVar()
    tsize.set(3)
    blab = tk.Label(main, text='BOARD SIZE')
    blab.pack()
    bslider = tk.Scale(main, orient='horiz', from_=10, to=100, variable=bsize)
    bslider.pack()
    tlab = tk.Label(main, text='GAME SPEED')
    tlab.pack()
    tslider = tk.Scale(main, orient='horiz', from_=1, to=5, variable=tsize)
    tslider.pack()
    pos = [bsize, tsize]
    start_but = tk.Button(main, text='START', command=lambda poss=pos: create_board(poss))
    start_but.pack(side=tk.BOTTOM)
    main.mainloop()


if __name__ == '__main__':
    new_game()
