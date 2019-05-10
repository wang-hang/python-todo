#!/usr/bin/python3
import wx

class ToDo(wx.Frame):
  def __init__(self, parent, title):
    super(ToDo, self).__init__(parent, title = title,size = (600,200))
    panel = wx.Panel(self)
    self.panel = panel
    self.TITLE = 'Todo'
    self.todos = []
    # todo项的列表盒子
    self.listBox = wx.BoxSizer(wx.VERTICAL)

    # 标题
    titleLabel = wx.StaticText(panel, label=self.TITLE)
    titleFont = wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD)
    titleLabel.SetFont(titleFont)
    self.titleLabel = titleLabel

    # 输入框
    textInput = wx.TextCtrl(panel, size=(200, 20), style=wx.TE_PROCESS_ENTER)
    textInput.Bind(wx.EVT_TEXT_ENTER, self.handleTextInputEnter)
    self.textInput = textInput

    # 操作区域的盒子
    operatorBox = wx.BoxSizer(wx.VERTICAL)
    operatorBox.Add(self.titleLabel, 0, wx.ALIGN_CENTER_HORIZONTAL)
    operatorBox.Add(self.textInput, 0, wx.ALIGN_CENTER_HORIZONTAL)
    self.operatorBox = operatorBox

    # main盒子
    mainBox = wx.BoxSizer(wx.VERTICAL)
    mainBox.Add(self.operatorBox, 0, wx.ALIGN_CENTER_HORIZONTAL)
    mainBox.Add(self.listBox, 0, wx.ALIGN_CENTER_HORIZONTAL)
    self.mainBox = mainBox

    panel.SetSizer(self.mainBox)
    self.Centre()
    self.Show()

  def handleTextInputEnter(self, evt):
    title = evt.GetString()
    if(title == "" ):
      return
    todo = {
      "title":title,
      "finished": False
    }
    # 添加todo项到todos list中
    self.addItem(todo)
  
  def addItem(self, todo):
    title = todo["title"]
    item = wx.CheckBox(self.panel, label = todo["title"])
    self.todos.append(todo)
    self.Bind(wx.EVT_CHECKBOX,self.onChecked) 
    self.listBox.Add(item, 0, wx.ALIGN_CENTER_HORIZONTAL)
    self.clearTextInput()
    self.mainBox.Layout()
  
  def clearTextInput(self):
    self.textInput.SetValue('')
  
  def onChecked(self, evt):
    cb = evt.GetEventObject()
    checked = cb.GetValue()
    key = cb.GetLabel()

    for index, todo in enumerate(self.todos):
      if(key == todo["title"]):
        todo["finished"] = checked

    
# 实例化
app = wx.App()

ToDo(None, 'Todo')

app.MainLoop()

