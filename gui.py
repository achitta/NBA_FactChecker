from PyQt5 import QtWidgets, QtGui, QtCore
font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(10)
font_but.setWeight(95)

class PushButWrap(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super(PushButWrap, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet("""margin: 1px; padding: 7px;
                            background-color: rgba(1,255,0,100);
                            color: rgba(1,140,0,100);
                            border-style: solid;
                            border-radius: 3px; border-width: 0.5px;
                            border-color: rgba(1,140,0,100);""")
    
    def enterEvent(self, event):
        self.setStyleSheet("""margin: 1px; padding: 7px;
                            background- color: rgba(1,140,040,100);
                            color: rgba(1,140,255,100);
                            border-style: solid; border-radius: 3px;
                            border-width: 0.5px;
                            border-color: rgba(1,140,140,100);""")
    
    def leaveEvent(self, event):
        self.setStyleSheet("""margin: 1px; padding: 7px;
                            background-color: rgba(1,255,0,100);
                            color: rgba(1,140,0,100);
                            border-style: solid;
                            border-radius: 3px; border-width: 0.5px;
                            border-color: rgba(1,140,0,100);""")
    
    
class PyQtApp(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("NBA Twilio Application")
        self.setWindowIcon(QtGui.QIcon("Your/image/file.png"))
        self.setMinimumWidth(resolution.width())
        self.setMinimumHeight(resolution.height())
        self.setStyleSheet("""QWidget
                            {background-color: rgba(128,128,128,128);}
                            QScrollBar:horizontal
                            {width: 1px; height: 1px;
                            background-color: rgba(0,0,0,1);}
                            QScrollBar:vertical
                            {width: 1px; height: 1px;
                            background-color: rgba(0,0,0,1);}""")

        self.phone_num = QtWidgets.QTextEdit(self)
        self.phone_num.setPlaceholderText("Enter Phone Number...")
        self.phone_num.resize(175,40)
        self.phone_num.move(1100,110)
        self.phone_num.setStyleSheet("""margin: 1px; padding: 1px;
                                    background-color:      
                                    rgba(255,255,255,1);
                                    color: rgba(1,140,0,100);
                                    border-style: solid;
                                    border-radius: 3px;
                                    border-width: 0.5px;
                                    border-color: rgba(0,0,0,1);""")

        self.subscribe = QtWidgets.QPushButton(self)
        self.subscribe.setText("SUBSCRIBE")
        self.subscribe.move(1300,110)
        self.subscribe.resize(100,40)
        self.subscribe.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.subscribe.clicked.connect(self.subscribe_func)

        self.query_box = QtWidgets.QTextEdit(self)
        self.query_box.setPlaceholderText("Team or Player Name...")
        self.query_box.move(10,200)
        self.query_box.resize(175,40)
        self.query_box.setStyleSheet("""margin: 1px; padding: 1px;
                                    background-color:      
                                    rgba(255,255,255,1);
                                    color: rgba(1,140,0,100);
                                    border-style: solid;
                                    border-radius: 3px;
                                    border-width: 0.5px;
                                    border-color: rgba(0,0,0,1);""")

        self.season = QtWidgets.QTextEdit(self)
        self.season.setPlaceholderText("Season Year or Career...")
        self.season.move(210,200)
        self.season.resize(175,40)
        self.season.setStyleSheet("""margin: 1px; padding: 1px;
                                    background-color:      
                                    rgba(255,255,255,1);
                                    color: rgba(1,140,0,100);
                                    border-style: solid;
                                    border-radius: 3px;
                                    border-width: 0.5px;
                                    border-color: rgba(0,0,0,1);""")

                        
        self.mode = QtWidgets.QTextEdit(self)
        self.mode.setPlaceholderText("PerGame or Totals...")
        self.mode.move(410,200)
        self.mode.resize(175,40)
        self.mode.setStyleSheet("""margin: 1px; padding: 1px;
                                    background-color:      
                                    rgba(255,255,255,1);
                                    color: rgba(1,140,0,100);
                                    border-style: solid;
                                    border-radius: 3px;
                                    border-width: 0.5px;
                                    border-color: rgba(0,0,0,1);""")

        self.title = QtWidgets.QTextEdit(self)
        self.title.setText("NBA Twilio App")
        self.title.resize(1500,100)
        self.title.setStyleSheet("""margin: 1px; padding: 1px;
                                    font-size: 40px;
                                    background-color:      
                                    rgba(255,100,100,1);
                                    color: rgba(0,0,0,1);
                                    border-style: solid;
                                    border-radius: 3px;
                                    border-width: 0.5px;
                                    border-color: rgba(0,0,0,1);""")

        self.career_stats_but = QtWidgets.QPushButton(self)
        self.career_stats_but.setText("Career Stats")
        self.career_stats_but.move(15,250)
        self.career_stats_but.resize(100,40)
        self.career_stats_but.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.career_stats_but.clicked.connect(self.career_stats_func)

        self.season_stats = QtWidgets.QPushButton(self)
        self.season_stats.setText("Season Stats")
        self.season_stats.move(15,300)
        self.season_stats.resize(100,40)
        self.season_stats.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.season_stats.clicked.connect(self.season_stats_func)

        self.player_awards = QtWidgets.QPushButton(self)
        self.player_awards.setText("Player Awards" )
        self.player_awards.move(15,350)
        self.player_awards.resize(100,40)
        self.player_awards.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.player_awards.clicked.connect(self.player_awards_func)

        self.roster = QtWidgets.QPushButton(self)
        self.roster.setText("Roster" )
        self.roster.move(15,400)
        self.roster.resize(100,40)
        self.roster.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.roster.clicked.connect(self.roster_func)

        self.draft_player = QtWidgets.QPushButton(self)
        self.draft_player.setText("Draft - Player" )
        self.draft_player.move(15,450)
        self.draft_player.resize(100,40)
        self.draft_player.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.draft_player.clicked.connect(self.draft_info_player_func)

        self.draft_college = QtWidgets.QPushButton(self)
        self.draft_college.setText("Draft - College" )
        self.draft_college.move(15,500)
        self.draft_college.resize(100,40)
        self.draft_college.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.draft_college.clicked.connect(self.draft_college_func)

        self.draft_team = QtWidgets.QPushButton(self)
        self.draft_team.setText("Draft - Team" )
        self.draft_team.move(15,550)
        self.draft_team.resize(100,40)
        self.draft_team.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.draft_team.clicked.connect(self.draft_team_func)

        self.draft_class = QtWidgets.QPushButton(self)
        self.draft_class.setText("Draft - Class" )
        self.draft_class.move(15,600)
        self.draft_class.resize(100,40)
        self.draft_class.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.draft_class.clicked.connect(self.draft_class_func)
        
        self.common_player = QtWidgets.QPushButton(self)
        self.common_player.setText("Player Info" )
        self.common_player.move(15,650)
        self.common_player.resize(100,40)
        self.common_player.setStyleSheet("background-color:rgba(140,240,240,1)")
        self.common_player.clicked.connect(self.common_player_info_func)

        self.output = QtWidgets.QTextEdit(self)
        self.output.setPlaceholderText("Output Box")
        self.output.move(800,250)
        self.output.resize(500,500)
        self.output.setStyleSheet("""margin: 1px; padding: 1px;
                                    background-color:      
                                    rgba(255,255,255,1);
                                    color: rgba(1,140,0,100);
                                    border-style: solid;
                                    border-radius: 3px;
                                    border-width: 0.5px;
                                    border-color: rgba(0,0,0,1);""")

    def subscribe_func(self):
        new_number = str(self.phone_num.toPlainText())
        print(new_number)
        print(type(new_number))
        self.phone_num.clear()

    def career_stats_func(self):
        return 0

    def season_stats_func(self):
        return 0

    def player_awards_func(self):
        return 0
    
    def roster_func(self):
        return 0

    def draft_info_player_func(self):
        return 0

    def draft_college_func(self):
        return 0

    def draft_team_func(self):
        return 0

    def draft_class_func(self):
        return 0

    def common_player_info_func(self):
        return 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = PyQtApp()
    myapp.setWindowOpacity(1)
    myapp.show()
    myapp.move(resolution.center() - myapp.rect().center())
    sys.exit(app.exec_())
else:
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
