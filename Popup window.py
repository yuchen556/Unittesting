import wx

app = wx.App()

dlg = wx.MessageDialog(None, "Do you want to update?",'Updater',wx.YES_NO | wx.ICON_QUESTION)
result = dlg.ShowModal()

if result == wx.ID_YES:
    print("Yes pressed")
else:
    print("No pressed")