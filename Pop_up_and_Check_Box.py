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
        wx.Frame.__init__(self, None, title=title, pos=(150, 150), size=(350, 600))
        self.Bind(wx.EVT_CLOSE, self.OnClose1)

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        m_text = wx.StaticText(panel, -1, "Maxwell Function Test!")
        m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        m_text.SetSize(m_text.GetBestSize())
        box.Add(m_text, 0, wx.ALL, 10)

        m_close = wx.Button(panel, wx.ID_CLOSE, "Start Test")
        m_close.Bind(wx.EVT_BUTTON, self.Start_Test)
        box.Add(m_close, 0, wx.ALL, 10)

        self.m_serial = wx.TextCtrl(panel)
        box.Add(self.m_serial, flag=wx.ALL, border=6)

        self._01_VGA = wx.CheckBox(panel, 1, '01-VGA Test')
        self._01_VGA.SetValue(True)
        self._02_Write_MAC = wx.CheckBox(panel, 2, '02-Write_MAC')
        self._02_Write_MAC.SetValue(True)
        self._03_Write_FRU = wx.CheckBox(panel, 3, '03-Write_FRU')
        self._03_Write_FRU.SetValue(True)

        self._04_ETH = wx.CheckBox(panel, 4, '04-ETH_Test')
        self._04_ETH.SetValue(True)
        self._05_SFP = wx.CheckBox(panel, 5, '05-SFP_Test')
        self._05_SFP.SetValue(True)
        self._06_CPU = wx.CheckBox(panel, 6, '06-CPU_Test')
        self._06_CPU.SetValue(True)

        self._07_Memory = wx.CheckBox(panel, 7, '07-Memory_Test')
        self._07_Memory.SetValue(True)
        self._08_Console = wx.CheckBox(panel, 8, '08-Console_Test')
        self._08_Console.SetValue(True)
        self._09_USB = wx.CheckBox(panel, 9, '09-USB_Test')
        self._09_USB.SetValue(True)

        self._10_PCI_E = wx.CheckBox(panel, 10, '10-PCI-E_Test')
        self._10_PCI_E.SetValue(True)
        self._11_SATA = wx.CheckBox(panel, 11, '11-SATA_Test')
        self._11_SATA.SetValue(True)
        self._12_M_2 = wx.CheckBox(panel, 12, '12-M.2_Test')
        self._12_M_2.SetValue(True)

        # self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=1, id2=3)
        # self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=1)
        # self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=2)
        # self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=3)

        box.Add(self._01_VGA, flag=wx.ALL, border=6)
        box.Add(self._02_Write_MAC, flag=wx.ALL, border=6)
        box.Add(self._03_Write_FRU, flag=wx.ALL, border=6)

        box.Add(self._04_ETH, flag=wx.ALL, border=6)
        box.Add(self._05_SFP, flag=wx.ALL, border=6)
        box.Add(self._06_CPU, flag=wx.ALL, border=6)

        box.Add(self._07_Memory, flag=wx.ALL, border=6)
        box.Add(self._08_Console, flag=wx.ALL, border=6)
        box.Add(self._09_USB, flag=wx.ALL, border=6)

        box.Add(self._10_PCI_E, flag=wx.ALL, border=6)
        box.Add(self._11_SATA, flag=wx.ALL, border=6)
        box.Add(self._12_M_2, flag=wx.ALL, border=6)

        panel.SetSizer(box)
        panel.Layout()


    def Start_Test(self, event):
        dialog = wx.MessageDialog(None, "要进行测试吗？ Do You Want To Test?", "测试", wx.YES_NO | wx.ICON_QUESTION)
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_YES:
            _101_VGA = self._01_VGA.GetValue()
            _102_Write_MAC = self._02_Write_MAC.GetValue()
            _103_Write_FRU = self._03_Write_FRU.GetValue()

            _104_ETH = self._04_ETH.GetValue()
            _105_SFP = self._05_SFP.GetValue()
            _106_CPU = self._06_CPU.GetValue()

            _107_Memort = self._07_Memory.GetValue()
            _108_Console = self._08_Console.GetValue()
            _109_USB = self._09_USB.GetValue()

            _110_PCI_E = self._10_PCI_E.GetValue()
            _111_SATA = self._11_SATA.GetValue()
            _112_M_2 = self._12_M_2.GetValue()

            ETH_Test.ethernet(_104_ETH)
            print("Yes")
            self.Destroy()
        else:
            print("No")
            print("No")
            print("No")
            print("No")
            print("No")
            print("No")
            self.Destroy()


    def OnClose1(self, event):
        dialog = wx.MessageDialog(None, "Do You Want To Exit?", "Close", wx.YES_NO | wx.ICON_QUESTION)
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_YES:
            self.Destroy()



# app = wx.App(redirect=True)  # Error messages go to popup window
app = wx.App()
top = Frame("Function Test Platform V0.9")
top.Show()
app.MainLoop()