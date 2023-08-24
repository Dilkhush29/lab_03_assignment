class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        match = Match(location, team1, team2, timing)
        self.matches.append(match)

    def search_by_team(self, team_name):
        team_matches = [match for match in self.matches if team_name in (match.team1, match.team2)]
        return team_matches

    def search_by_location(self, location):
        location_matches = [match for match in self.matches if match.location == location]
        return location_matches

    def search_by_timing(self, timing):
        timing_matches = [match for match in self.matches if match.timing == timing]
        return timing_matches

# Create the FlightTable instance
flight_table = FlightTable()

# Add matches to the table
flight_table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
flight_table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
# ... Repeat this for all matches

# User interaction loop
while True:
    print("Choose a search parameter:")
    print("1. List of all matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        team_name = input("Enter the team name: ")
        team_matches = flight_table.search_by_team(team_name)
        for match in team_matches:
            print(match.location, match.team1, match.team2, match.timing)

    elif choice == '2':
        location = input("Enter the location: ")
        location_matches = flight_table.search_by_location(location)
        for match in location_matches:
            print(match.location, match.team1, match.team2, match.timing)

    elif choice == '3':
        timing = input("Enter the timing: ")
        timing_matches = flight_table.search_by_timing(timing)
        for match in timing_matches:
            print(match.location, match.team1, match.team2, match.timing)

    elif choice == '4':
        break