olympic_records = {}


def record_medal_details():
    nation = input("Enter Country Name: ")
    sport_type = input("Enter Sports Name: ")
    medals_earned = int(input("Enter total medals won: "))

    if nation not in olympic_records:
        olympic_records[nation] = {"medal_count": 0}
    if sport_type not in olympic_records[nation]:
        olympic_records[nation][sport_type] = []

    for i in range(medals_earned):
        print(f"Enter Details for medal {i + 1}")
        competitor = input("Enter Athlete Name: ")
        year_achieved = int(input("Enter Year: "))
        medal_kind = input("Enter Medal Won (Bronze/Silver/Gold): ")
        olympic_records[nation][sport_type].append({'competitor': competitor, 'medal': medal_kind, 'year': year_achieved})

        olympic_records[nation]["medal_count"] += 1

def show_event_details():
    nation = input("Enter Country Name: ")
    sport_type = input("Enter Sports Name: ")

    if nation in olympic_records and sport_type in olympic_records[nation]:
        print(f"\nDetails for {sport_type} in {nation}:")
        for medal in olympic_records[nation][sport_type]:
            print(f"Athlete: {medal['competitor']}, Medal: {medal['medal']}, Year: {medal['year']}")
    else:
        print("No records found for the specified country and sport.")

def display_all_records():
    for nation, sport_data in olympic_records.items():
        print(f"\nCountry: {nation}")
        for sport_type, medals in sport_data.items():
            if sport_type != "medal_count":
                print(f"  Sport: {sport_type}")
                for medal in medals:
                    print(f"    Athlete: {medal['competitor']}, Medal: {medal['medal']}, Year: {medal['year']}")

def show_medal_summary():
    print("\nMedal Count by Country:")
    for nation, sport_data in olympic_records.items():
        print(f"{nation}: {sport_data['medal_count']} medals")

def find_athlete_performance():
    competitor = input("Enter Athlete Name to search: ")
    found = False

    for nation, sport_data in olympic_records.items():
        for sport_type, medals in sport_data.items():
            if sport_type != "medal_count":
                for medal in medals:
                    if medal['competitor'].lower() == competitor.lower():
                        found = True
                        print(f"\nAthlete: {medal['competitor']}")
                        print(f"  Country: {nation}")
                        print(f"  Sport: {sport_type}")
                        print(f"  Medal: {medal['medal']}")
                        print(f"  Year: {medal['year']}")

    if not found:
        print("No records found for the specified athlete.")

def display_olympic_stats():
    medal_totals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    athlete_count = 0
    total_medals = 0

    for nation, sport_data in olympic_records.items():
        for sport_type, medals in sport_data.items():
            if sport_type != "medal_count":
                athlete_count += len(medals)
                for medal in medals:
                    medal_totals[medal['medal']] += 1
                    total_medals += 1

    avg_medals_per_athlete = total_medals / athlete_count if athlete_count > 0 else 0

    print("\nStatistics:")
    print(f"Total Athletes: {athlete_count}")
    print(f"Total Medals: {total_medals}")
    print(f"Average Medals per Athlete: {avg_medals_per_athlete:.2f}")
    print(f"Medal Distribution: Gold: {medal_totals['Gold']}, Silver: {medal_totals['Silver']}, Bronze: {medal_totals['Bronze']}")

while True:
    print("\n-------------------------------------------------------")
    print("Olympic Medal Tracker")
    print("-------------------------------------------------------")
    print("1. Add Medal Details")
    print("2. View Event Details")
    print("3. View All Records")
    print("4. View Medal Count by Country")
    print("5. Search Athlete Performance")
    print("6. View Statistics")
    print("7. Exit")
    option = input("Choose an option: ")

    if option == '1':
        record_medal_details()
    elif option == '2':
        show_event_details()
    elif option == '3':
        display_all_records()
    elif option == '4':
        show_medal_summary()
    elif option == '5':
        find_athlete_performance()
    elif option == '6':
        display_olympic_stats()
    elif option == '7':
        break
    else:
        print("Invalid option, please try again.")
