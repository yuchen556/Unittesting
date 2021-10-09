import wx
import wx.lib.agw.pygauge as PG

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "PyGauge Demo", size=(200,100))
        panel = wx.Panel(self)
        gauge1 = PG.PyGauge(panel, -1, size=(100, 25), style=wx.GA_HORIZONTAL)
        gauge1.SetValue(80)
        gauge1.SetDrawValue(draw=True, drawPercent=True, font=None, colour=wx.BLACK, formatString=None)
        gauge1.SetBackgroundColour(wx.WHITE)
        gauge1.SetBorderColor(wx.BLACK)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(gauge1, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        panel.SetSizer(sizer)
        sizer.Layout()

app = wx.App()
frame = MyFrame(None)
frame.Show()

app.MainLoop()