import wx
import wx.xrc
import wx.grid # library for grid on Frame2

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,375 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.UsernameLabel = wx.StaticText( self, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UsernameLabel.Wrap( -1 )
		bSizer6.Add( self.UsernameLabel, 0, wx.ALL, 5 )
		
		self.TrophiesLabel = wx.StaticText( self, wx.ID_ANY, u"Trophies:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TrophiesLabel.Wrap( -1 )
		bSizer6.Add( self.TrophiesLabel, 0, wx.ALL, 5 )
		
		self.clubLabel = wx.StaticText( self, wx.ID_ANY, u"Club (if any):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clubLabel.Wrap( -1 )
		bSizer6.Add( self.clubLabel, 0, wx.ALL, 5 )
		
		self.Victoriesthree = wx.StaticText( self, wx.ID_ANY, u"3s Victories:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Victoriesthree.Wrap( -1 )
		bSizer6.Add( self.Victoriesthree, 0, wx.ALL, 5 )
		
		self.Victoriessolo = wx.StaticText( self, wx.ID_ANY, u"Solo Victories:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Victoriessolo.Wrap( -1 )
		bSizer6.Add( self.Victoriessolo, 0, wx.ALL, 5 )
  
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Win Rate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer6.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.TagLabel = wx.StaticText( self, wx.ID_ANY, u"Input Tag", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TagLabel.Wrap( -1 )
		bSizer9.Add( self.TagLabel, 0, wx.ALL, 5 )
		
		self.TagInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.TagInput, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.usernameOutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.usernameOutput.Enable( False )
		
		bSizer8.Add( self.usernameOutput, 0, wx.ALL, 2 )
		
		self.trophiesOutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.trophiesOutput.Enable( False )
		
		bSizer8.Add( self.trophiesOutput, 0, wx.ALL, 2 )
		
		self.clubOutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clubOutput.Enable( False )
		
		bSizer8.Add( self.clubOutput, 0, wx.ALL, 2 )
		
		self.Victory3Output = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Victory3Output.Enable( False )
		
		bSizer8.Add( self.Victory3Output, 0, wx.ALL, 2 )
		
		self.VictoryoneOutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VictoryoneOutput.Enable( False )
		
		bSizer8.Add( self.VictoryoneOutput, 0, wx.ALL, 2 )
		
		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl8.Enable( False )
		
		bSizer8.Add( self.m_textCtrl8, 0, wx.ALL, 2 )
  
		bSizer8.Add( (1,2), 0, wx.ALL, 20 )
		bSizer8.Add( ( 0, 10), 0, wx.EXPAND, 5 )  # This adds a small vertical space
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.TagInputButton = wx.Button( self, wx.ID_ANY, u"Look up player", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TagInputButton.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )
		
		bSizer10.Add( self.TagInputButton, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"See more -->", wx.DefaultPosition, wx.Size( 120,50 ), 0 )
		self.m_button3.Enable( False )
		
		bSizer10.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
  
class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choice1Choices = [ u"Map", u"Brawler", u"Mode" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer8.Add( self.m_choice1, 0, wx.ALL, 5 )
		
		m_listBox1Choices = [ u"Draco", u"Kit", u"Cordelius", u"Chester", u"Brock" ]
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		bSizer8.Add( self.m_listBox1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Show Stats", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Vizualize stats\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button5, 0, wx.ALL, 5 )
		
		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		
		# Grid
		self.m_grid1.CreateGrid( 1, 3 )
		self.m_grid1.EnableEditing( False )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"Win rate" )
		self.m_grid1.SetColLabelValue( 1, u"Star Player" )
		self.m_grid1.SetColLabelValue( 2, u"Favorite Map" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelValue( 0, u"_____" )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer7.Add( self.m_grid1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass