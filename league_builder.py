import csv
import random

def assign_players():
    with open('soccer_players.csv') as csvfile:
        soccerplayers = csv.DictReader(csvfile)
        players = list(soccerplayers)

        target = open('teams.txt', 'w')

        raptors=[]
        dragons=[]
        celtics=[]

        for player in players:
            experienced_player = 0
            if len(raptors)<6:
                raptors.append(player)
                if player['Soccer Experience'] == 'YES':
                    experienced_player+=1
                    if experienced_player >3:
                        break

            elif len(dragons)<6:
                dragons.append(player)
                if player['Soccer Experience'] == 'YES':
                    experienced_player+=1
                    if experienced_player >3:
                        break

            else:
                celtics.append(player)
                if player['Soccer Experience'] == 'YES':
                    experienced_player+=1
                    if experienced_player >3:
                        break

        target.write("Raptors")
        target.write("\n")
        for raptor in raptors:
            target.write(str(raptor['Name', 'Soccer Experience', 'Guardian Name(s)']))
            target.write("\n")

        target.write("\n")
        target.write("Dragons")
        target.write("\n")
        for raptor in raptors:
            target.write(str(raptor))
            target.write("\n")

        target.write("\n")
        target.write("Celtics")
        target.write("\n")
        for raptor in raptors:
            target.write(str(raptor))
            target.write("\n")



if __name__ == "__main__":
     assign_players()