import wx
import wx.grid
#print(wx.version())

import demo
import brawl
from brawl import get_player_info, get_player_club_name, get_battles
from data_manager import save_data, load_data, is_data_fresh
from analyzer import most_mvp, display_win_rate_brawler, display_win_rate_map, best_map_brawler
from demo import MyFrame1, MyFrame2
from plots import PieChartFrame

# constants used for selection in myFrame2
MAPS = ["Gem Fort", "Stone Fort", "Bouncing Diner", "Double Swoosh", "Pinhole Punt"]
BRAWLERS = [
    "Shelly", "Nita", "Colt", "Bull", "Jessie", "Brock", "Dynamike", "Bo",
    "Tick", "8-Bit", "Emz", "Stu", "El Primo", "Barley", "Poco", "Rosa",
    "Rico", "Darryl", "Penny", "Carl", "Jacky", "Piper", "Pam", "Frank",
    "Bibi", "Bea", "Nani", "Edgar", "Griff", "Grom", "Bonnie", "Mortis",
    "Tara", "Gene", "Max", "Mr. P", "Sprout", "Byron", "Squeak", "Spike",
    "Crow", "Leon", "Sandy", "Amber", "Meg", "Gale", "Surge", "Colette",
    "Lou", "Ruffs", "Belle", "Buzz", "Ash", "Lola", "Fang", "Eve",
    "Janet", "Otis", "Sam", "Gus", "Buster", "Chester", "Gray", "Mandy",
    "R-T", "Hank", "Willow", "Pearl", "Maisie", "Doug", "Chuck", "Cordelius",
    "Charlie", "Larry", "Patches"
]
MODES = [
    "Gem Grab", "Showdown", "Duo Showdown", "Brawl Ball", "Heist",
    "Bounty", "Hot Zone", "Siege", "Knockout", "Duels", "Wipeout",
]

class BrawlFrame(demo.MyFrame1):
    def __init__(self, parent):
        demo.MyFrame1.__init__(self, parent)
        self.TagInputButton.Bind(wx.EVT_BUTTON, self.findUsername)
        self.m_button3.Bind(wx.EVT_BUTTON, self.newFrameClick)
        
    def findUsername(self, event):
        self.m_button3.Enable()
        username = self.TagInput.GetValue()
        #self.m_textCtrl1.SetValue(str(username))
        data = load_data(username)
        print(f'DATA\n\n{data}')
        if not is_data_fresh(data):
            data = brawl.get_all_player_data(username)
            save_data(data, username)
            
        player_info = data['player_info']
        club_name = data['club_name']
        """
        battle_archive = data.get('battle_archive', []) # .get() method lets us specify value if key does not exist
        recent_battles = data.get('recent_battles', [])
        """
        wins = 0
        battles = data['recent_battles']['items']
        for battle in battles:
            try:
                if battle['battle']['result'] == 'victory':
                    wins += 1
            except Exception as e:
                print(f'Error: {e}')
                
        win_rate = wins / len(battles) * 100
        print(win_rate)
            
        # Update GUI with the data
        if isinstance(player_info, dict):
            self.usernameOutput.SetValue(f"{player_info.get('name', 'N/A')}")
            self.trophiesOutput.SetValue(f"{player_info.get('trophies','N/A')}")
            self.clubOutput.SetValue(f"{club_name}")
            self.Victory3Output.SetValue(f"{player_info.get('3vs3Victories', 'N/A')}")
            self.VictoryoneOutput.SetValue(f"{player_info.get('soloVictories', 'N/A')}")
            #recent_battles = len(data['recent_battles'])
        else:
            self.usernameOutput.SetValue(str(player_info))  # Display error message
    """   
    def update_stats_display(self):
        player_tag = self.TagInput.GetValue()
        win_rate = get_win_rate(player_tag)
        most_played = get_most_played_mode(player_tag)
        print(most_played + " " + win_rate)
    """
    
    def newFrameClick(self, event):
        print("Second Button Clicked!")
        tag = self.TagInput.GetValue()
        second_frame = MyFrame2(self, tag)
        second_frame.Show()
        
class MyFrame2(demo.MyFrame2):
    def __init__(self, parent, tag):
        demo.MyFrame2.__init__(self, parent)
        self.tag = tag
        self.m_button5.Disable()
        self.current_selection = None
        self.m_button2.Bind(wx.EVT_BUTTON, self.show_stats)
        self.m_listBox1.Bind(wx.EVT_LISTBOX, self.on_select)
        self.m_button5.Bind(wx.EVT_BUTTON, self.on_show_pie_chart)
        
        # Bind the event handler
        self.m_choice1.Bind(wx.EVT_CHOICE, self.on_category_change)

        # Initialize the ListBox with the default category (Map)
        self.update_list_box("Map")

    def update_list_box(self, category):
        if category == "Map":
            self.m_listBox1.Set(MAPS)
        elif category == "Brawler":
            self.m_listBox1.Set([brawler.upper() for brawler in BRAWLERS])
        elif category == "Mode":
            self.m_listBox1.Set(MODES)

    def on_category_change(self, event=None):
        """This function is used to change the selection of strings (map, brawler, event)"""
        selected_category = self.m_choice1.GetStringSelection()
        self.update_list_box(selected_category)
        return selected_category
    
    
    def on_select(self, event):
        self.current_selection = event.GetString()
        #print(f"Selection updated: {self.current_selection}")
        
    def on_show_pie_chart(self, event):
        result = self.get_stats()
        try:
            pie_chart_frame = PieChartFrame(self, "Win Rate Pie Chart", result)
            pie_chart_frame.Show()
        except:
            wx.MessageBox("Please select a valid option and show stats first.", "Error", wx.OK | wx.ICON_ERROR)
    
    def get_stats(self, selection=None):
        """This function is used to get the win rate of the selected map,brawler,or mode"""
        cat = self.on_category_change()
        selection = self.current_selection
        print(f"Category: {cat}")
        print(f"Current selection: {self.current_selection}")
        if cat == "Brawler" and self.current_selection:
            #print(selection)
            brawler_stats = display_win_rate_brawler(self.tag, self.current_selection)
            win = brawler_stats[0]
            total = brawler_stats[1]
            star = brawler_stats[2]
            
            fav = best_map_brawler(self.tag, self.current_selection)
            return [win, total, fav, star]
        elif cat == "Map":
            map_stats = display_win_rate_map(self.tag, self.current_selection)
            win = map_stats[0]
            total = map_stats[1]
            
            return [win, total, win]
            
    def show_stats(self, event):
        stats = self.get_stats()
        print(f'stats: {stats}')
        self.m_grid1.SetRowLabelValue(0, self.current_selection)
        self.m_grid1.SetCellValue(0, 0, str(stats[0]))
        self.m_grid1.SetCellValue(0, 1, str(stats[1]))
        self.m_grid1.SetCellValue(0, 2, str(stats[2]))
        self.m_grid1.AutoSizeColumn(0)
        self.m_button5.Enable()
        self.m_grid1.ForceRefresh()
            
            
        

            
            
        
        
        
        

        
            
        
            
    
            

app = wx.App(False)
frame = BrawlFrame(None)
frame.Show(True)
app.MainLoop()