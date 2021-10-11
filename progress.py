import time

import wx
import wx.lib.agw.pygauge as PG


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "PyGauge Demo", size=(200,100))
        panel = wx.Panel(self)
        self.gauge1 = PG.PyGauge(panel, -1, size=(100, 25), style=wx.GA_HORIZONTAL)
        self.gauge1.SetValue(10)
        self.gauge1.SetDrawValue(draw=True, drawPercent=True, font=None, colour=wx.BLACK, formatString=None)
        self.gauge1.SetBackgroundColour(wx.WHITE)
        self.gauge1.SetBorderColor(wx.BLACK)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.gauge1, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        panel.SetSizer(sizer)
        sizer.Layout()

    def test(self):
        for i in [0, 1, 2, 3, 4, 5]:
            time.sleep(1)
            self.gauge1.Update(1.0, time=1)
            i += 1



app = wx.App()
frame = MyFrame(None)
frame.Show()
frame.test()


app.MainLoop()