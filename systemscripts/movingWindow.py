#!/usr/bin/python
import Tkinter as Tk
import re

class TransparentWin (Tk.Tk) :
    ''' Transparent Tk Window Class '''
    def __init__ (self) :
        Tk.Tk.__init__(self)
        self.Drag = Drag(self)
        ''' Sets focus to the window. '''
        self.focus_force()
        ''' Removes the native window boarder. '''
        self.overrideredirect(True)
        ''' Disables resizing of the widget.  '''
        self.resizable(False, False)
        ''' Places window above all other windows in the window stack. '''
        self.wm_attributes('-topmost', True)
        ''' This changes the alpha value (How transparent the window should
            be). It ranges from 0.0 (completely transparent) to 1.0
            (completely opaque).  '''
        self.attributes('-alpha', 0.1)
        ''' The windows overall position on the screen  '''
        self.wm_geometry('+' + str(439) + '+' + str(172))
        ''' Changes the window's color. '''
        bg = '#3e4134'
        self.config(bg=bg)
        self.Frame = Tk.Frame(self, bg=bg)
        self.Frame.pack()
        ''' Exits the application when the window is right clicked. '''
        self.Frame.bind('<Button-3>', self.exit)
        ''' Changes the window's size indirectly. '''
        self.Frame.configure(width=162, height=100)

    def exit (self, event) :
        self.destroy()

    def position (self) :
        _filter = re.compile(r'(\d+)?x?(\d+)?([+-])(\d+)([+-])(\d+)')
        pos = self.winfo_geometry()
        filtered = _filter.search(pos)
        self.X = int(filtered.group(4))
        self.Y = int(filtered.group(6))
        return self.X, self.Y

class Drag:
    ''' Makes a window dragable. '''
    def __init__ (self, par, dissable=None, releasecmd=None) :
        self.Par        = par
        self.Dissable   = dissable
        self.ReleaseCMD = releasecmd
        self.Par.bind('<Button-1>', self.relative_position)
        self.Par.bind('<ButtonRelease-1>', self.drag_unbind)

    def relative_position (self, event) :
        cx, cy = self.Par.winfo_pointerxy()
        x, y = self.Par.position()
        self.OriX = x
        self.OriY = y
        self.RelX = cx - x
        self.RelY = cy - y
        self.Par.bind('<Motion>', self.drag_wid)

    def drag_wid (self, event) :
        cx, cy = self.Par.winfo_pointerxy()
        d = self.Dissable
        if d == 'x' :
            x = self.OriX
            y = cy - self.RelY
        elif d == 'y' :
            x = cx - self.RelX
            y = self.OriY
        else:
            x = cx - self.RelX
            y = cy - self.RelY
        if x < 0 :
            x = 0
        if y < 0 :
            y = 0
        self.Par.wm_geometry('+' + str(x) + '+' + str(y))

    def drag_unbind (self, event) :
        self.Par.unbind('<Motion>')
        if self.ReleaseCMD != None :
            self.ReleaseCMD()

    def dissable (self) :
        self.Par.unbind('<Button-1>')
        self.Par.unbind('<ButtonRelease-1>')
        self.Par.unbind('<Motion>')

if __name__ == '__main__' :
    TransparentWin().mainloop()
