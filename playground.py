from nba_api.stats.static import teams

team_list = teams.get_teams()

for team in team_list:
    print(team['full_name'])

from nba_api.stats.static import players

stephen_curry = players.find_player_by_id(201939)
print(stephen_curry['full_name'])

from nba_api.stats.endpoints import commonplayerinfo

# Basic Request
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)

lebron_stats = player_info.player_headline_stats.get_dict()

print(lebron_stats['data'])

from nba_api.stats.endpoints import commonteamroster
import json

roster_info = commonteamroster.CommonTeamRoster(season=2017, team_id = 1610612739)
roster_cavs = roster_info.get_dict()

with open('nba.json', 'w') as fp:
    json.dump(roster_cavs, fp, indent=3)

a = roster_cavs['resultSets']
b = a[0]
c = b['rowSet']

for player in c:
    print(player[3])

from nba_api.stats.endpoints import leagueleaders
league_info = leagueleaders.LeagueLeaders(league_id="00",per_mode48="PerGame", scope="S", season="2018-19", season_type_all_star="Regular Season", stat_category_abbreviation="PTS")
print(league_info.get_dict())

with open('nba.json', 'w') as fp:
    json.dump(league_info.get_dict(), fp, indent=3)
    