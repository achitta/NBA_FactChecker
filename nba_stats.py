from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.endpoints import leagueleaders
import json

class nba_data:
    def getPlayerId(self, full_name = "Stephen Curry"):
        try:
            player_details = players.find_players_by_full_name(full_name)
            return(player_details[0]['id']) 
        except:
            print("No player with the given name")
            return -1

    def getTeamId(self,full_name = "Golden State Warriors"):
        try:
            team_details = teams.find_teams_by_full_name(full_name)
            return(team_details[0]['id'])
        except:
            print("No team with the given name")
            return -1
    # ****************************************************************************************************************
    #Roster Info Functions
    def getRosterFromId(self,my_team_id = "1610612744", my_season = "2018-19"):
        try:
            roster_info = commonteamroster.CommonTeamRoster(season=my_season,team_id = my_team_id)
            roster = roster_info.get_dict()
            a = roster['resultSets']
            b = a[0]
            c = b['rowSet']
            my_players = []
            for player in c:
                my_players.append(player[3])
            return my_players
        except:
            print("Team ID is not valid")
            return -1

    def getRoster(self, full_name = "Golden State Warriors", season = "2019-20"):
        id = self.getTeamId(full_name)
        my_players = self.getRosterFromId(id, season)
        return my_players

    def printRoster(self, full_name = "Golden State Warriors", season = "2019-20"):
        players = self.getRoster(full_name, season)
        for player in players:
            print(player)
    
    # ****************************************************************************************************************

    # ****************************************************************************************************************
    # Season Leaders Section
    def getLeagueLeaderInfo(self, league_num = "00", mode = "PerGame", my_scope = "S", my_season = "2018-19", my_type = "Regular Season", category = "PTS"):
        leader_info = leagueleaders.LeagueLeaders(league_id=league_num, per_mode48=mode, scope=my_scope, season=my_season, season_type_all_star= my_type, stat_category_abbreviation=category)
        with open('nba.json', 'w') as fp:
            json.dump(leader_info.get_dict(), fp, indent=3)
        return leader_info.get_dict()

    def getArrayIndexHeader(self, col_name, stat_mode, headers) :
        count = 0
        for header in headers:
            if(header == col_name):
                return count
            count = count + 1
        raise Exception('Should not reach here')
        
    def printLeagueLeaderSingle(self, s_league_num = "00", s_mode = "PerGame", s_my_scope = "S", s_my_season = "2018-19", s_my_type = "Regular Season", s_category = "PTS"):
        leader_dict = self.getLeagueLeaderInfo(league_num=s_league_num, mode=s_mode, my_scope=s_my_scope, my_season=s_my_season, my_type=s_my_type, category=s_category)
        headers = leader_dict['resultSet']['headers']
        for header in headers:
            if(header == "PLAYER_ID" or header == "RANK"):
                continue
            print(header + ": ", end = " ")
            idx = self.getArrayIndexHeader(header, s_mode, headers)
            print(leader_dict['resultSet']['rowSet'][0][idx])

    def printLeagueLeaderSummary(self, s_league_num = "00", s_mode = "PerGame", s_my_scope = "S", s_my_season = "2018-19", s_my_type = "Regular Season", s_category = "PTS"):
        leader_dict = self.getLeagueLeaderInfo(league_num=s_league_num, mode=s_mode, my_scope=s_my_scope, my_season=s_my_season, my_type=s_my_type, category=s_category)
        flag = True
        if(s_category == "PTS" or s_category == "AST" or s_category == "REB"):
            flag = False
        for i in range(0,10):
            print(str(i+1) + ".) ", end="")
            print(leader_dict['resultSet']['rowSet'][i][2] + " - ", end = " ")
            pts_idx = self.getArrayIndexHeader("PTS", s_mode, leader_dict['resultSet']['headers'])
            print("PTS: " + str(leader_dict['resultSet']['rowSet'][i][pts_idx]) + " | ", end = " ")
            ast_idx = self.getArrayIndexHeader("AST", s_mode, leader_dict['resultSet']['headers'])
            print("AST: " + str(leader_dict['resultSet']['rowSet'][i][ast_idx]) + " | ", end = " ")
            reb_idx = self.getArrayIndexHeader("REB", s_mode, leader_dict['resultSet']['headers'])
            print("REB: " + str(leader_dict['resultSet']['rowSet'][i][reb_idx]), end = "")
            if(flag):
                wild_idx = self.getArrayIndexHeader(s_category, s_mode, leader_dict['resultSet']['headers'])
                print(" | " + str(s_category) + ": " + str(leader_dict['resultSet']['rowSet'][i][wild_idx]))
            else :
                print("")
    # ****************************************************************************************************************
nba_data = nba_data()
nba_data.printLeagueLeaderSummary(s_category="FG3A", s_mode="PerGame")
# nba_data.printLeagueLeaderSingle(s_mode="PerGame")

