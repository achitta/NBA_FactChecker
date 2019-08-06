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

roster_info = commonteamroster.CommonTeamRoster(season=2019, team_id = 1610612739)
roster_cavs = roster_info.get_dict()

with open('nba.json', 'w') as fp:
    json.dump(roster_cavs, fp, indent=3)

a = roster_cavs['resultSets']
b = a[0]
c = b['rowSet']

for player in c:
    print(player[3])