from random import choice


# read only
file_players = open('players.txt', 'r')
file_teams = open('teams.txt', 'r')

players = file_players.read().splitlines()
teams = file_teams.read().splitlines()

print('Players: ', players)
print('Team names: ', teams)

teamA = []
teamB = []

while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    if players == []:
        break

    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

teamAName = ''
teamBName = ''
while teamAName == '' or teamAName == teamBName:
    teamAName = choice(teams)
    teamBName = choice(teams)
print(teamAName, teamA)
print(teamBName, teamB)



