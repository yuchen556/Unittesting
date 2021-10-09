import wx

ee1 = False
ee2 = "False"
ee3 = "False"
class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(300, 200))

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)

        self.cb1 = wx.CheckBox(pnl, label='ETH test', pos=(10, 10))
        self.cb2 = wx.CheckBox(pnl, label='USB test', pos=(10, 40))
        self.cb3 = wx.CheckBox(pnl, label='CPU test', pos=(10, 70))

        self.Bind(wx.EVT_CHECKBOX, self.onChecked)
        self.Centre()
        self.Show(True)

    def onChecked(self, e):
        cb = e.GetEventObject()
        print(cb.GetLabel(), ' is selected', cb.GetValue())
        ee1 = self.cb1.GetValue()
        print(ee1)
        ee2 = self.cb2.GetValue()
        print(ee2)
        ee3 = self.cb3.GetValue()
        t33 = type(ee3)
        print(t33)
        print(ee3)


ex = wx.App()
Kk01 = Example(None, 'CheckBox Demo - www.yiibai.com').cb1.GetValue()
print(Kk01)

ex.MainLoop()