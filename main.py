def main_menu():
    print("Welcome to the Olympic Data Analysis Program!")
    print("Please select an option:")
    print("1. Analyze Athlete Data")
    print("2. Analyze Medal Tally Data")
    print("3. Perform Combined Data Analysis")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")
    return choice

def athlete_menu():
    print("\nAthlete Data Analysis:")
    print("1. Top N Countries by Female Participants")
    print("2. Top N Countries by Male Participants")
    print("3. Top N Countries by Total Participants")
    print("4. Return to Main Menu")
    
    choice = input("Enter your choice (1/2/3/4): ")
    return choice

def medal_menu():
    print("\nMedal Tally Analysis:")
    print("1. Total Medal Tally")
    print("2. Rank Countries by Medals")
    print("3. Return to Main Menu")
    
    choice = input("Enter your choice (1/2/3): ")
    return choice

def combined_menu():
    print("\nCombined Data Analysis:")
    print("1. Calculate Average Medals per Athlete")
    print("2. Find Missing Countries")
    print("3. Add a New Country")
    print("4. Search for a Country")
    print("5. Return to Main Menu")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    return choice

def main():
    while True:
        choice = main_menu()

        if choice == "1":
            while True:
                athlete_choice = athlete_menu()
                if athlete_choice == "1":
                    n = int(input("Enter the number of top countries: "))
                    top_female_participants = sorted(Athletes_list, key=lambda x: x['Female'], reverse=True)[:n]
                    print("Top Countries by Female Participants:")
                    print_Whole_table(top_female_participants)
                elif athlete_choice == "2":
                    n = int(input("Enter the number of top countries: "))
                    top_male_participants = sorted(Athletes_list, key=lambda x: x['Male'], reverse=True)[:n]
                    print("Top Countries by Male Participants:")
                    print_Whole_table(top_male_participants)
                elif athlete_choice == "3":
                    n = int(input("Enter the number of top countries: "))
                    top_total_participants = sorted(Athletes_list, key=lambda x: x['Total Athletes'], reverse=True)[:n]
                    print("Top Countries by Total Participants:")
                    print_Whole_table(top_total_participants)
                elif athlete_choice == "4":
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == "2":
            while True:
                medal_choice = medal_menu()
                if medal_choice == "1":
                    print("Total Medal Tally:")
                    rank_country(medal_tally)
                    print_Whole_table(medal_tally)
                elif medal_choice == "2":
                    rank_country(medal_tally)
                    print("Countries Ranked by Medals:")
                    print_Whole_table(medal_tally)
                elif medal_choice == "3":
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == "3":
            while True:
                combined_choice = combined_menu()
                if combined_choice == "1":
                    print("Average Medals per Athlete:")
                    Whole_data = average_medals_per_athlete(Whole_data)
                    print_average_medals(Whole_data)
                elif combined_choice == "2":
                    missing_countries = find_missing_countries([entry['Country_Code'] for entry in Athletes_list], Whole_data)
                    if missing_countries:
                        print("Missing Countries:")
                        for code in missing_countries:
                            print(f"- {code}")
                    else:
                        print("No missing countries.")
                elif combined_choice == "3":
                    print("Add a New Country:")
                    new_country_data = get_user_input()
                    if new_country_data:
                        Whole_data = add_new_country(
                            new_country_data["Country_Code"],
                            new_country_data["Country"],
                            new_country_data["Female"],
                            new_country_data["Male"],
                            new_country_data.get("Medals", None)
                        )
                        print("Country added successfully!")
                elif combined_choice == "4":
                    search_term = input("Enter country name or code: ")
                    country_info = search_country(Whole_data, search_term)
                    print_country_details(country_info)
                elif combined_choice == "5":
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
