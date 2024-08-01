import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import wx

class PieChartFrame(wx.Frame):
    def __init__(self, parent, stats):
        super(PieChartFrame, self).__init__(parent, title="title", size=(400, 400))
        
        panel = wx.Panel(self)
        
        # Create the pie chart
        figure = Figure(figsize=(5, 4), dpi=100)
        subplot = figure.add_subplot(111)
        
        # Data for the pie chart
        wins = stats[0]
        losses = stats[1] - stats[0]
        losses = losses / stats[1] * 100
        sizes = [wins, losses]
        labels = 'Wins', 'Losses'
        colors = ['#ff9999', '#66b3ff']
        
        subplot.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        subplot.axis('equal')
        
        # Create the canvas to display the chart
        canvas = FigureCanvas(panel, -1, figure)
        
        # Use a sizer to manage the layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(canvas, 0, wx.EXPAND)
        panel.SetSizer(sizer)
        
        self.Center()
    