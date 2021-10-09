# coding=utf-8
# 代码文件：chapter21/ch21.6.3.py

import wx
import ETH_Test

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='复选框', size=(240, 160))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(self)

        statictext = wx.StaticText(panel, label='选择你喜欢的编程语言：')
        self.cb1 = wx.CheckBox(panel, 1, 'Python')
        self.cb1.SetValue(True)
        self.cb2 = wx.CheckBox(panel, 2, 'Java')
        self.cb2.SetValue(True)
        self.cb3 = wx.CheckBox(panel, 3, 'C++')
        self.cb3.SetValue(True)
        # self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=1, id2=3)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=1)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=2)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=3)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(statictext, flag=wx.ALL, border=6)
        vbox.Add(self.cb1, flag=wx.ALL, border=6)
        vbox.Add(self.cb2, flag=wx.ALL, border=6)
        vbox.Add(self.cb3, flag=wx.ALL, border=6)

        panel.SetSizer(vbox)




    def on_checkbox_click(self, event):
    #     # cb = event.GetEventObject()
    #     # print('选择 {0}，状态{1}'.format(cb.GetLabel(), event.IsChecked()))
        m1 = self.cb1.GetValue()
        print(m1)
    #
    #     m2 = self.cb2.GetValue()
    #     print(m2)
    #
    #     m3 = self.cb3.GetValue()
    #     print(m3)
    #
        ETH_Test.ethernet(m1)


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()

        dlg = wx.MessageDialog(None, "Do you want to update?", 'Updater', wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()

        if result == wx.ID_YES:
            print("Yes pressed")
        else:
            print("No pressed")

        return True


if __name__ == '__main__':
    app = App()

    app.MainLoop()  # 进入主事件循环
