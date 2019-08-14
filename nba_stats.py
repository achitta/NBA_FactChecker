from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.endpoints import leagueleaders
from nba_api.stats.endpoints import drafthistory
from nba_api.stats.endpoints import scoreboardv2
from nba_api.stats.endpoints import playerawards
from nba_api.stats.endpoints import playerfantasyprofile
from nba_api.stats.endpoints import playerprofilev2
from datetime import date
from datetime import timedelta
import json

class nba_data:
    def getPlayerId(self, full_name = "Stephen Curry"):
        try:
            player_details = players.find_players_by_full_name(full_name)
            return(player_details[0]['id']) 
        except:
            raise Exception("No player with the given name")

    def getTeamId(self,full_name = "Golden State Warriors"):
        try:
            team_details = teams.find_teams_by_full_name(full_name)
            return(team_details[0]['id'])
        except:
            raise Exception("No team with the given name")
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
            raise Exception("Team ID not valid")

    def getRoster(self, full_name = "Golden State Warriors", season = "2019-20"):
        id = self.getTeamId(full_name)
        my_players = self.getRosterFromId(id, season)
        return my_players

    def printRoster(self, full_name = "Golden State Warriors", season = "2019-20"):
        players = self.getRoster(full_name, season)
        with open('roster.txt','w') as fp:
            print("", end = "") 

        for player in players:
            # print(player)
            with open('roster.txt', 'a') as fp:
                fp.write(player + '\n')

    
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

    # ****************************************************************************************************************
    # Headline Stats
    def printHeadlineStats(self,full_name = "Stephen Curry"): 
        id = self.getPlayerId(full_name)
        player_info = commonplayerinfo.CommonPlayerInfo(id)
        headline_stats = player_info.player_headline_stats.get_dict()
        with open('headline_stats.txt', 'w') as fp:
            fp.write("")
        for i in range(1,6):
            print(headline_stats['headers'][i] + ": " + str(headline_stats['data'][0][i]))
            with open('headline_stats.txt', 'a') as fp:
                fp.write(headline_stats['headers'][i] + ": " + str(headline_stats['data'][0][i]) + " | ")
    # ****************************************************************************************************************

    # ****************************************************************************************************************
    # Common Player Info
    def printCommonPlayerInfo(self,full_name = "Stephen Curry"):
        id = self.getPlayerId(full_name)
        player = commonplayerinfo.CommonPlayerInfo(id)
        common_info = player.common_player_info.get_dict()
        with open('general.txt', 'w') as fp:
            fp.write("")
        for i in range(0,30):
            if(i == 0 or i == 3 or i == 4 or i == 5 or i == 15 or i == 16 or i == 19 or i == 21 or i == 24 or i == 25 or i == 26):
                continue
            print(common_info['headers'][i] + ": " + str(common_info['data'][0][i]))
            with open('general.txt', 'a') as fp:
                fp.write(common_info['headers'][i] + ": " + str(common_info['data'][0][i]) + '\n')
    # ****************************************************************************************************************

    # ****************************************************************************************************************
    # Draft Info
    # 
    def getDraftClassInfo(self, team_num="", my_pick="", my_round="", ovlpick="", my_college="", league_num = "00", visible_amount = "", my_season = "2019") :
        info = drafthistory.DraftHistory(league_id="00", topx_nullable=visible_amount, team_id_nullable=team_num, season_year_nullable=my_season, round_pick_nullable=my_pick, round_num_nullable=my_round, overall_pick_nullable=ovlpick, college_nullable=my_college)
        draft_details = info.get_dict()
        return draft_details

    def printDraftInfoForPlayer(self, full_name = "Stephen Curry"):
        id = self.getPlayerId(full_name)
        with open('draft_player.txt', 'w') as fp:
            fp.write("")
        player = commonplayerinfo.CommonPlayerInfo(id)
        common_info = player.common_player_info.get_dict()
        print("Draft Year: " + str(common_info['data'][0][27]))
        print("Round Number: " + str(common_info['data'][0][28]))
        print("Pick Number: " + str(common_info['data'][0][29]))
        with open('draft_player.txt', 'a') as fp:
            fp.write("Draft Year: " + str(common_info['data'][0][27]) + '\n')
            fp.write("Round Number: " + str(common_info['data'][0][28]) + '\n')
            fp.write("Pick Number: " + str(common_info['data'][0][29]) + '\n')
        
    def printDraftClassForGivenSeason(self, season = "2019", show_num = 10):
        draft_dict = self.getDraftClassInfo(league_num = "00", visible_amount = str(show_num), my_season = season)
        player_list = draft_dict['resultSets'][0]['rowSet']
        with open('general.txt', 'w') as fp:
            fp.write("")
        for players in player_list:
            print(players[1], end = " - ")
            print("Round num: " + str(players[3]), end = " | ")
            print("Pick num: " + str(players[4]), end = " | ")
            print("Overall: " + str(players[5]), end = " | ")
            print("Team: " + str(players[10]), end = " | ")
            print("College: " + str(players[11]))
            with open('general.txt', 'a') as fp:
                fp.write("Player Name: " + players[1] + '\n')
                fp.write("Round num: " + str(players[3]) + '\n')
                fp.write("Pick Number: " + str(players[4]) + '\n')
                fp.write("Overall: " + str(players[5]) + '\n')
                fp.write("Team: " + str(players[10]) + '\n')
                fp.write("College: " + str(players[11]) + '\n')
                fp.write('\n')

    def printPlayerFromDraftPick(self, overall = "1", round_n = "", pick_n = "", season = "2019"):
        draft_dict = self.getDraftClassInfo(my_pick=pick_n, my_round=round_n, ovlpick=overall)
        player_list = draft_dict['resultSets'][0]['rowSet']  
        i = 0    
        print(player_list[i][1])
        print("Round num: " + str(player_list[i][3]))
        print("Pick num: " + str(player_list[i][4]))
        print("Overall: " + str(player_list[i][5]))
        print("Team: " + str(player_list[i][10]))
        print("College: " + str(player_list[i][11]))

    def printCollegeDraftStats(self, college_name = "Duke", season = "2019"):
        draft_dict = self.getDraftClassInfo(my_college=college_name, my_season=season)
        # print(draft_dict)
        with open('general.txt', 'w') as fp:
            fp.write("")
        player_list = draft_dict['resultSets'][0]['rowSet']
        for players in player_list:
            print(players[1], end = " - ")
            print("Round num: " + str(players[3]), end = " | ")
            print("Pick num: " + str(players[4]), end = " | ")
            print("Overall: " + str(players[5]), end = " | ")
            print("Team: " + str(players[10]), end = " | ")
            print("College: " + str(players[11]))

            with open('general.txt', 'a') as fp:
                fp.write("Player Name: " + players[1] + '\n')
                fp.write("Round num: " + str(players[3])+'\n')
                fp.write("Pick num: " + str(players[4])+'\n')
                fp.write("Overall: " + str(players[5])+'\n')
                fp.write("Team: " + str(players[10])+'\n')
                fp.write("College: " + str(players[11]) + '\n')
                fp.write('\n')

    def printDraftStatsByTeam(self, team_name = "Golden State Warriors", season = "2019"):
        id = self.getTeamId(team_name)
        draft_dict = self.getDraftClassInfo(my_season=season, team_num=id)
        player_list = draft_dict['resultSets'][0]['rowSet']
        with open('general.txt', 'w') as fp:
            fp.write("")
        for players in player_list:
            print(players[1], end = " - ")
            print("Round num: " + str(players[3]), end = " | ")
            print("Pick num: " + str(players[4]), end = " | ")
            print("Overall: " + str(players[5]), end = " | ")
            print("Team: " + str(players[10]), end = " | ")
            print("College: " + str(players[11]))

            with open('general.txt', 'a') as fp:
                fp.write("Player Name: " + players[1] + '\n')
                fp.write("Round num: " + str(players[3])+'\n')
                fp.write("Pick num: " + str(players[4])+'\n')
                fp.write("Overall: " + str(players[5])+'\n')
                fp.write("Team: " + str(players[10])+'\n')
                fp.write("College: " + str(players[11]) + '\n')
                fp.write('\n')

    # ****************************************************************************************************************

    # ****************************************************************************************************************
    # Daily Score Board
    def getScoreBoard(self, date = "2016-02-27"):
        scoreBoard = scoreboardv2.ScoreboardV2(game_date=date, league_id="00", day_offset="0").get_dict()
        with open('scoreboard.json', 'w') as fp:
            json.dump(scoreBoard, fp, indent=3)
        return scoreBoard

    def getScoresForDay(self, myDate = "2016-02-27"):
        dayScores_dict = self.getScoreBoard(date=myDate)
        scores = dayScores_dict['resultSets'][1]['rowSet']
        combined = []
        for score in scores:
            combined.append([score[4],score[22]])
        return combined

    def printScoresForDay(self, date = "2016-02-27") :
        combined = self.getScoresForDay(myDate=date)
        i = 0
        with open('scores.txt','w') as fp:
            print("")   

        while(i < len(combined)) :
            team1 = combined[i][0]
            score1 = combined[i][1]
            team2 = combined[i+1][0]
            score2 = combined[i+1][1]
            if(score1 > score2) :
                print(team1 + " def. " + team2 + " " + str(score1) + "-" + str(score2))
                with open('scores.txt', 'a') as fp:
                    fp.write(team1 + " def. " + team2 + " " + str(score1) + "-" + str(score2))
            else:
                print(team2 + " def. " + team1 + " " + str(score2) + "-" + str(score1))
                with open('scores.txt', 'a') as fp:
                    fp.write(team2 + " def. " + team1 + " " + str(score2) + "-" + str(score1))
            
            with open('scores.txt', 'a') as fp:
                fp.write(" | ")
            i = i + 2

        
    def printScoresForYesterday(self) :
        yesterday = self.getYesterday()
        combined = self.getScoresForDay(myDate=yesterday)
        i = 0
        with open('scores.txt','w') as fp:
            print("", end = "")   
        
        if(len(combined) == 0) :
            with open('scores.txt', 'a') as fp:
                fp.write("No games played yesterday")

        while(i < len(combined)) :
            team1 = combined[i][0]
            score1 = combined[i][1]
            team2 = combined[i+1][0]
            score2 = combined[i+1][1]
            if(score1 > score2) :
                print(team1 + " def. " + team2 + " " + str(score1) + "-" + str(score2))
                with open('scores.txt', 'a') as fp:
                    fp.write(team1 + " def. " + team2 + " " + str(score1) + "-" + str(score2))
            else:
                print(team2 + " def. " + team1 + " " + str(score2) + "-" + str(score1))
                with open('scores.txt', 'a') as fp:
                    fp.write(team2 + " def. " + team1 + " " + str(score2) + "-" + str(score1))
            
            with open('scores.txt', 'a') as fp:
                fp.write(" | ")
            i = i + 2

    def getYesterday(self):
        yesterday = date.strftime(date.today() - timedelta(1), '%Y-%m-%d')
        return (str(yesterday))

    
            

    # ****************************************************************************************************************

    # ****************************************************************************************************************
    #Player Awards
    def getPlayerAwards(self, id = "201939"):
        awards_dict = playerawards.PlayerAwards(player_id = id).get_dict()
        return awards_dict

    def printPlayerAward(self, name = "Stephen Curry"):
        my_id = self.getPlayerId(full_name=name)
        awards_dict = self.getPlayerAwards(id=my_id)
        # print(awards_dict)
        with open('awards.json', 'w') as fp:
            json.dump(awards_dict, fp, indent=3)

        awards = awards_dict['resultSets'][0]['rowSet']
        with open('awards.txt', 'w') as fp:
            print("", end = "")
        my_dict = {}
        for award in awards:
            name = award[4]
            if(award[5] != None) :
                name += (" " + str(award[5]))
            
            if (name in my_dict) :
                my_dict[name] += 1
            else:
                my_dict[name] = 1

        for x,y in my_dict.items():
            with open('awards.txt', 'a') as fp:
                fp.write(str(y) + "x " + x + "\n")
                print(str(y) + "x " + x + "\n")
    # ****************************************************************************************************************

    # ****************************************************************************************************************
    # Fantasy Profile
    def getFantasyProfileDict(self, mode = "PerGame",type_season = "Regular Season", id = "201939", my_season = "2018-19"):
        fantasy_obj = playerfantasyprofile.PlayerFantasyProfile(player_id=id, measure_type_base="Base", pace_adjust_no="N", per_mode36=mode, plus_minus_no="N", rank_no="N", season=my_season, season_type_playoffs=type_season, league_id_nullable="00")
        fantasy_dict = fantasy_obj.get_dict()
        with open('season_stats.json', 'w') as fp:
            json.dump(fantasy_dict, fp, indent=3)
        return fantasy_dict

    def printSeasonStats(self, my_mode = "PerGame", season = "Regular Season", my_name = "Stephen Curry", year = "2018-19") :
        with open('season_stats.txt', 'w') as fp:
            print("", end = "")
        my_id = self.getPlayerId(my_name)
        profile_dict = self.getFantasyProfileDict(mode = my_mode, type_season=season, id= my_id, my_season=year)
        my_headers = profile_dict['resultSets'][0]['headers']
        pts_idx = self.getArrayIndexHeader(col_name="PTS", stat_mode="PerGame", headers = my_headers)
        ast_idx = self.getArrayIndexHeader(col_name="AST", stat_mode="PerGame", headers = my_headers)
        reb_idx = self.getArrayIndexHeader(col_name="REB", stat_mode="PerGame", headers = my_headers)
        fg_idx = self.getArrayIndexHeader(col_name = "FG_PCT", stat_mode = "PerGame", headers = my_headers)
        three_idx = self.getArrayIndexHeader(col_name = "FG3_PCT", stat_mode = "PerGame", headers = my_headers)
        ft_idx = self.getArrayIndexHeader(col_name = "FT_PCT", stat_mode = "PerGame", headers = my_headers)
        results = profile_dict['resultSets'][0]['rowSet'][0]
        print("PTS: " + str(results[pts_idx]), end = " | ")
        print("AST: " + str(results[ast_idx]), end = " | ")
        print("REB: " + str(results[reb_idx]), end = " | ")
        print("FG%: " + str(round(results[fg_idx] * 100,2)) + "%", end = " | ")
        print("3pt%: " + str(round(results[three_idx] * 100,2)) + "%", end = " | ")
        print("FT%: " + str(round(results[ft_idx] * 100,2)) + "%")
        with open('season_stats.txt', 'a') as fp:
            fp.write("PTS: " + str(results[pts_idx]) + " | ")
            fp.write("AST: " + str(results[ast_idx])+ " | ")
            fp.write("REB: " + str(results[reb_idx])+" | ")
            fp.write("FG%: " + str(round(results[fg_idx] * 100,2)) + "%"+ " | ")
            fp.write("3pt%: " + str(round(results[three_idx] * 100,2)) + "%"+" | ")
            fp.write("FT%: " + str(round(results[ft_idx] * 100,2)) + "%")

    def getPlayerProfileDict(self, mode = "PerGame", player_name = "Stephen Curry") :
        id = self.getPlayerId(full_name=player_name)
        profile_dict = playerprofilev2.PlayerProfileV2(per_mode36=mode, player_id=id).get_dict()
        with open('career_stats.json', 'w') as fp:
            json.dump(profile_dict, fp, indent=3)
        return profile_dict

    def printCareerStats(self, my_mode = "PerGame", name = "Stephen Curry"):
        profile_dict = self.getPlayerProfileDict(mode= my_mode, player_name=name)
        with open('career_stats.txt', 'w') as fp:
            print("", end = "")
        headers = profile_dict['resultSets'][1]['headers']
        results = profile_dict['resultSets'][1]['rowSet'][0]
        pts_idx = self.getArrayIndexHeader(col_name="PTS", stat_mode="PerGame", headers = headers)
        ast_idx = self.getArrayIndexHeader(col_name="AST", stat_mode="PerGame", headers = headers)
        reb_idx = self.getArrayIndexHeader(col_name="REB", stat_mode="PerGame", headers = headers)
        fg_idx = self.getArrayIndexHeader(col_name = "FG_PCT", stat_mode = "PerGame", headers = headers)
        three_idx = self.getArrayIndexHeader(col_name = "FG3_PCT", stat_mode = "PerGame", headers = headers)
        ft_idx = self.getArrayIndexHeader(col_name = "FT_PCT", stat_mode = "PerGame", headers = headers)
        print("PTS: " + str(results[pts_idx]), end = " | ")
        print("AST: " + str(results[ast_idx]), end = " | ")
        print("REB: " + str(results[reb_idx]), end = " | ")
        print("FG%: " + str(round(results[fg_idx] * 100,2)) + "%", end = " | ")
        print("3pt%: " + str(round(results[three_idx] * 100,2)) + "%", end = " | ")
        print("FT%: " + str(round(results[ft_idx] * 100,2)) + "%")
        with open('career_stats.txt', 'a') as fp:
            fp.write("PTS: " + str(results[pts_idx]) + " | ")
            fp.write("AST: " + str(results[ast_idx])+ " | ")
            fp.write("REB: " + str(results[reb_idx])+" | ")
            fp.write("FG%: " + str(round(results[fg_idx] * 100,2)) + "%"+ " | ")
            fp.write("3pt%: " + str(round(results[three_idx] * 100,2)) + "%"+" | ")
            fp.write("FT%: " + str(round(results[ft_idx] * 100,2)) + "%")
        
    # ****************************************************************************************************************
nba_obj = nba_data()
# nba_data.printLeagueLeaderSummary(s_category="FG3A", s_mode="PerGame")
# nba_data.printLeagueLeaderSingle(s_mode="PerGame")
# nba_data.printCommonPlayerInfo("Kevin Durant")
# print(nba_data.getTeamId())
# nba_data.getDraftClassInfo()
# nba_data.printDraftInfoForPlayer("Greg Oden")
# nba_data.printPlayerFromDraftPick(overall=3)
# nba_data.printCollegeDraftStats()
# nba_data.printDraftClassForGivenSeason(season="2018")
# nba_data.printDraftStatsByTeam()
# nba_data.printScoresForDay(date="2016-02-27")
nba_obj.printPlayerAward(name="Stephen Curry")
# nba_data.printScoresForYesterday()
# nba_data.printHeadlineStats()
# nba_obj.printSeasonStats()
# nba_obj.printCareerStats()
###USER FUNCTIONS

##Roster
#printRoster()

##League Leader
#printLeagueLeaderSingle()
#printLeagueLeaderSummary()

##Headline Stats
#printHeadlineStats()

##Common Player Info
#printCommonPlayerInfo()

##Draft Info
#printDraftInfoForPlayer()
#printDraftClassForGivenSeason()
#printPlayerFromDraftPick()
#printCollegeDraftStats()
#printDraftStatsByTeam()