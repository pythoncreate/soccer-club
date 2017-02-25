import csv
import random

def read_players(filepath):
    """
    Read a list of players (each one represented by a dictionary) and return the list
    """
    with open(filepath) as csvfile:
        soccerplayers = csv.DictReader(csvfile)
        return list(soccerplayers)

def assign_teams(players, teams):
    """
    Given a list of players and a list of teams, randomly assisng
    players to teams--but in a fair way that balances experienced
    players as evenly as possible across teams.  Returns a dictionary
    mapping team name --> list of players on the team.
    """

    # shuffle order of teams and players so there's no hint of
    # favoriteism
    random.shuffle(teams)
    random.shuffle(players)

    # partition player list into experienced and inexperienced players
    experienced = [p for p in players if p['Soccer Experience'] == 'YES']
    inexperienced = [p for p in players if p['Soccer Experience'] == 'NO']

    # create a roster
    n_teams = len(teams)
    roster = {team_name: [] for team_name in teams}

    # pick the experienced players (round-robin)
    for i, player in enumerate(experienced):
        teammate = teams[i % n_teams]
        roster[teammate].append(player)

    # add inexperienced players (round-robing)
    for i, player in enumerate(inexperienced):
        teamate = teams[i % n_teams]
        roster[teamate].append(player)

    return roster

def write_roster(roster, filepath):
    """
    Write a roster dictionary to given filepath.
    """
    fields = ["Name", "Soccer Experience", "Guardian Name(s)"]
    with open(filepath, 'w') as f:
        for team in roster.keys():
            f.write(team + '\n')
            for player in roster[team]:
                #select just the desired fields for output
                row = [player[f] for f in fields]
                #construct and write out a formatted record
                formatted_row = ', '.join(row)+ '\n'
                f.write(formatted_row)
            # separate teams with a little more white space
            f.write('\n')

def create_welcome_letter(players):
    for player in players:
        name = player['Name'].split()
        filepath = name[0].lower()+'_'+name[1].lower()+ '.txt'
        with open(filepath, 'w') as f:
            f.write("Dear " + player['Guardian Name(s)'] +",\n" +
                    "We are so happy to have " + player['Name'] + " as a participant"
                    " in the New soccer league!" + "\n")

if __name__ == "__main__":
     players = read_players('soccer_players.csv')
     teams = ['Raptors', 'Dragons','Sharks']
     roster = assign_teams(players,teams)
     write_roster(roster, 'teams.txt')
     create_welcome_letter(players)

     print('done!')