#!/usr/bin/python
# -*- coding: <<encoding>> -*-
# -------------------------------------------------------------------------------
#   <<project>>
#
# -------------------------------------------------------------------------------

import wx
import ETH_Test


class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, pos=(150, 150), size=(350, 200))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        m_text = wx.StaticText(panel, -1, "Hello World!")
        m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        m_text.SetSize(m_text.GetBestSize())
        box.Add(m_text, 0, wx.ALL, 10)

        m_close = wx.Button(panel, wx.ID_CLOSE, "Close")
        m_close.Bind(wx.EVT_BUTTON, self.OnClose)
        box.Add(m_close, 0, wx.ALL, 10)

        panel.SetSizer(box)
        panel.Layout()


    # def OnClose(self, event):
    #     dlg = wx.MessageDialog(self,
    #                            "Do you really want to close this application?",
    #                            "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
    #     result = dlg.ShowModal()
    #     dlg.Destroy()
    #     if result == wx.ID_OK:
    #         self.Destroy()



    def OnClose(self, event):
        dialog = wx.MessageDialog(None, "Do You Want To Close?", "Close", wx.YES_NO | wx.ICON_QUESTION)
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_YES:
            print("Yes")
            self.Destroy()
        else:
            print("No")



app = wx.App(redirect=True)  # Error messages go to popup window
top = Frame("MON")
top.Show()
app.MainLoop()