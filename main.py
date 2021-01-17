# A slide rail control to move the camera
# code adapted from realpython.com How to Build a Python GUI Application With wxPython

import wx

##create the class that creates everything
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Camera Mover')
        ## create the window
        panel = wx.Panel(self)
        ## define the panel to be vertically stacked
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        ## create a first set of text boxes. One to say enter distance value, and one for the value
        # declare them
        self.enter_distance = wx.TextCtrl(panel, value = "Enter Distance below:", style = wx.TE_READONLY)
        self.distance_box = wx.TextCtrl(panel)
        # add them
        my_sizer.Add(self.enter_distance, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.distance_box, 0, wx.ALL | wx.EXPAND, 5)
        ## create a second pair of text boxes for time
        # declare them
        self.enter_time = wx.TextCtrl(panel, value="Enter time to move below:", style=wx.TE_READONLY)
        self.time_box = wx.TextCtrl(panel)
        # add them
        my_sizer.Add(self.enter_time, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.time_box, 0, wx.ALL | wx.EXPAND, 5)
        ## create the button to tell it to move
        btn_1 = wx.Button(panel, label='Move to position')
        # attach the function on_press to the button
        btn_1.Bind(wx.EVT_BUTTON, self.on_press)
        # add it to the sizer
        my_sizer.Add(btn_1, 0, wx.ALL | wx.CENTER, 5)
        # #apply the sizer formatting
        panel.SetSizer(my_sizer)
        self.Show()
    ## when button is pressed, say what was typed. If nothing typed, say nothing was entered
    def on_press(self, event):
        ## retrieve the values from the text boxes
        distance = self.distance_box.GetValue()
        time = self.time_box.GetValue()
        if not distance and not time:
            print("You didn't enter anything!")
        elif not distance and time:
            print("You didn't enter a distance")
        elif distance and not time:
            print("You didn't enter a timeframe")
        else:
            print(f'You want to move it {distance} units over the {time} seconds.')
## run program
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    # set it to main loop so the execution pauses so the window stays open
    app.MainLoop()