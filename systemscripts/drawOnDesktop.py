#!/usr/bin/python
import wx
print wx.version()

class FancyFrame(wx.Frame):
    def __init__(self, width, height):
        wx.Frame.__init__(self, None,
                          style = wx.STAY_ON_TOP |
                          wx.FRAME_NO_TASKBAR |
                          wx.FRAME_SHAPED,
                          size=(width, height))
        self.SetTransparent(180)
        b = wx.EmptyBitmap(width, height)
        dc = wx.MemoryDC()
        dc.SelectObject(b)
        dc.SetBackground(wx.Brush('black'))
        dc.Clear()
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.SetPen(wx.Pen('red', 4))
        dc.DrawRectangle(10, 10, width-20, height-20)
        dc.SelectObject(wx.NullBitmap)
        b.SetMaskColour('black')
        self.SetShape(wx.RegionFromBitmap(b))

        self.Bind(wx.EVT_KEY_UP, self.OnKeyDown)
        self.SetBackgroundColour('blue')
        self.Show(True)

    def OnKeyDown(self, event):
        '''quit if user press Esc'''
        if event.GetKeyCode() == 27:
            self.Close(force=True)
        else:
            event.Skip()

if __name__ == '__main__':
    app = wx.App()
    f = FancyFrame(300, 300)
    app.MainLoop()
