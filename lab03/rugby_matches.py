# rugby_matches.py
# Colm Murphy 121353486

"""
Write a program that asks the user for the names of two Rugby teams, the ‘tries’ and
‘points’ scored and prints out the results
"""

def print_results_table():
    team1 = input("Enter the name of team 1: ")
    team2 = input("Enter the name of team 2: ")

    tries_team1 = int(input("Enter the number of tries for %s: " % team1))
    tries_team2 = int(input("Enter the number of tries for %s: " % team2))

    points_team1 = int(input("Enter the number of converted/penalty points for %s: " % team1))
    points_team2 = int(input("Enter the number of converted/penalty points for %s: " % team2))

    print("Results")
    print("\tTeam\tTries\t\tPoints")
    print("-" * 48)
    print("%12.12s\t%d\t\t%d" % (team1, tries_team1, points_team1))
    print("%12.12s\t%d\t\t%d" % (team2, tries_team2, points_team2))


def get_player_age():
    player = input("Enter the name of an Irish rugby player: ")
    age_days = int(input("Enter %s's age (in days): " % player))
    age_years = age_days // 365
    remaining_days = age_days % 365
    print("%s is %d years and %d days old" % (player, age_years, remaining_days))



def main():
    print_results_table()

if __name__ == "__main__":
    print_results_table()