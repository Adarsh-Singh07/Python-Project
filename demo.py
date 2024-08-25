# Function to remove duplicates from the data
def remove_duplicates(data):
    unique_countries = []
    seen_codes = set()
    for entry in data:
        country_code = entry['Country_Code']
        if country_code not in seen_codes:
            unique_countries.append(entry)
            seen_codes.add(country_code)
    return unique_countries

# Function to sort and rank countries by their medal tally
def sort_country(country):
    return (-country["Gold"], -country["Silver"], -country["Bronze"], country["Country"])

def rank_country(medal_tally):
    medal_tally.sort(key=sort_country)
    rank = 1
    for i in medal_tally:
        i["Rank"] = rank
        rank += 1

# Function to merge data from two lists
def merge_data(athlete_data, medal_data):
    merged_data = []
    medal_dict = {entry['Country_Code']: entry for entry in medal_data}
    for athlete in athlete_data:
        country_code = athlete['Country_Code']
        country_medals = medal_dict.get(country_code, {"Gold": 0, "Silver": 0, "Bronze": 0, "Total": 0})
        merged_entry = {
            "Country_Code": country_code,
            "Country": athlete['Country'],
            "Female": athlete['Female'],
            "Male": athlete['Male'],
            "Total_Athletes": athlete['Total Athletes'],
            "Gold": country_medals.get("Gold", 0),
            "Silver": country_medals.get("Silver", 0),
            "Bronze": country_medals.get("Bronze", 0),
            "Total_Medals": country_medals.get("Total", 0)
        }
        merged_data.append(merged_entry)
    merged_data = remove_duplicates(merged_data)
    rank_country(merged_data)
    return merged_data

# Function to print the whole table
def print_whole_table(olympic_data):
    print(" Rank | Country                          | Female  | Male    | Total Athletes   | Gold  | Silver | Bronze | Total Medals")
    print("------|----------------------------------|---------|---------|------------------|-------|--------|--------|-------------")
    for entry in olympic_data:
        print(f"{entry['Rank']:6} | {entry['Country']:32} | {entry['Female']:7} | {entry['Male']:7} | {entry['Total_Athletes']:16} | {entry['Gold']:5} | {entry['Silver']:6} | {entry['Bronze']:6} | {entry['Total_Medals']:7}")

# Additional analysis functions
def top_10_countries_by_sex_ratio(athletes_list):
    sorted_countries = sorted(athletes_list, key=lambda x: x['Male'] / x['Female'] if x['Female'] != 0 else 0, reverse=True)
    print("Top 10 Countries by Male-to-Female Athlete Ratio:")
    print("-------------------------------------------------")
    for i in range(min(10, len(sorted_countries))):
        country = sorted_countries[i]
        ratio = country['Male'] / country['Female'] if country['Female'] != 0 else 0
        print(f"{i+1}. {country['Country']}: {ratio:.2f}")

def countries_with_more_female_athletes(athletes_list):
    countries = [(country['Country'], country['Female']) for country in athletes_list if country['Female'] > country['Male']]
    print("Countries with More Female Athletes:")
    print("-----------------------------------")
    for country, female_count in countries:
        print(f"{country}: {female_count} female athletes")

def delete_country(country_code, country_name, data_list):
    index = None
    for i, entry in enumerate(data_list):
        if entry['Country_Code'] == country_code or entry['Country'] == country_name:
            index = i
            break
    if index is not None:
        del data_list[index]
        return data_list
    print("Country not found.")
    return data_list

def country_with_most_gold_medals(olympic_data):
    max_gold = max(olympic_data, key=lambda x: x['Gold'])
    return max_gold['Country']

def countries_with_equal_male_female(athletes_list):
    countries = [country['Country'] for country in athletes_list if country['Male'] == country['Female']]
    return countries

def n_country_with_least_athletes(athletes_list, n=1):
    sorted_countries = sorted(athletes_list, key=lambda x: x['Total Athletes'])
    return sorted_countries[:n]

def countries_above_threshold(athletes_list, threshold):
    countries = [country['Country'] for country in athletes_list if country['Total Athletes'] > threshold]
    return countries

def average_medals_per_athlete(whole_data):
    total_medals = sum(entry['Total_Medals'] for entry in whole_data)
    total_athletes = sum(entry['Total_Athletes'] for entry in whole_data)
    if total_athletes == 0:
        return 0
    return total_medals / total_athletes

def find_missing_countries(country_code_list, whole_data):
    existing_codes = {entry['Country_Code'] for entry in whole_data}
    missing_codes = [code for code in country_code_list if code not in existing_codes]
    return missing_codes

def add_new_country(country_code, country_name, female_athletes, male_athletes, medal_data):
    # Create a new entry and add it to the Whole_data
    new_entry = {
        "Country_Code": country_code,
        "Country": country_name,
        "Female": female_athletes,
        "Male": male_athletes,
        "Total_Athletes": female_athletes + male_athletes,
        "Gold": medal_data.get("Gold", 0),
        "Silver": medal_data.get("Silver", 0),
        "Bronze": medal_data.get("Bronze", 0),
        "Total_Medals": medal_data.get("Total", 0)
    }
    Whole_data.append(new_entry)
    rank_country(Whole_data)
    return Whole_data

def main_menu():
    print("\n=== Olympic Data Analysis Menu ===")
    print("1. Analyze Athlete Data")
    print("2. Analyze Medal Tally")
    print("3. Combine and Analyze Data")
    print("4. Add or Delete a Country")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def athlete_data_menu():
    print("\n=== Athlete Data Analysis ===")
    print("1. Top N countries with most male participants")
    print("2. Top N countries with most female participants")
    print("3. Top N countries with most total participants")
    print("4. Top 10 countries by male-to-female athlete ratio")
    print("5. Countries with more female athletes than male")
    print("6. Countries with equal male and female athletes")
    print("7. Country with the least athletes")
    print("8. Countries with more than a threshold number of athletes")
    print("9. Go Back")
    choice = input("Enter your choice (1-9): ")
    return choice

def medal_tally_menu():
    print("\n=== Medal Tally Analysis ===")
    print("1. Country with the most gold medals")
    print("2. Print entire medal tally")
    print("3. Go Back")
    choice = input("Enter your choice (1-3): ")
    return choice

def combined_data_menu():
    print("\n=== Combined Data Analysis ===")
    print("1. Average medals per athlete")
    print("2. Find missing countries between lists")
    print("3. Go Back")
    choice = input("Enter your choice (1-3): ")
    return choice

def add_new_country_flow():
    print("\n=== Add a New Country ===")
    country_code = input("Enter the country code: ").upper()
    country_name = input("Enter the country name: ").title()
    female_athletes = int(input("Enter the number of female athletes: "))
    male_athletes = int(input("Enter the number of male athletes: "))
    has_medals = input("Does the country have medals? (yes/no): ").lower()
    medal_data = None
    if has_medals == 'yes':
        gold = int(input("Enter the number of gold medals: "))
        silver = int(input("Enter the number of silver medals: "))
        bronze = int(input("Enter the number of bronze medals: "))
        medal_data = {"Gold": gold, "Silver": silver, "Bronze": bronze, "Total": gold + silver + bronze}
    Whole_data = add_new_country(country_code, country_name, female_athletes, male_athletes, medal_data)
    print("\nCountry added successfully!")
    return Whole_data

def delete_country_flow():
    print("\n=== Delete a Country ===")
    country_code = input("Enter the country code: ").upper()
    country_name = input("Enter the country name: ").title()
    
    global Athletes_list, medal_tally, Whole_data
    
    Athletes_list = delete_country(country_code, country_name, Athletes_list)
    medal_tally = delete_country(country_code, country_name, medal_tally)
    Whole_data = delete_country(country_code, country_name, Whole_data)
    
    print("\nCountry deleted successfully!")

def main():
    global Athletes_list, medal_tally, Whole_data
    
    # Sample data
    Athletes_list = [
        {"Country_Code": "USA", "Country": "United States", "Female": 200, "Male": 300, "Total Athletes": 500},
        {"Country_Code": "CAN", "Country": "Canada", "Female": 150, "Male": 250, "Total Athletes": 400},
    ]
    
    medal_tally = [
        {"Country_Code": "USA", "Gold": 30, "Silver": 20, "Bronze": 15, "Total": 65},
        {"Country_Code": "CAN", "Gold": 10, "Silver": 15, "Bronze": 12, "Total": 37},
    ]
    
    Whole_data = merge_data(Athletes_list, medal_tally)
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            while True:
                sub_choice = athlete_data_menu()
                if sub_choice == '1':
                    # Example function call
                    pass  # Implement top N countries with most male participants here
                elif sub_choice == '2':
                    # Example function call
                    pass  # Implement top N countries with most female participants here
                elif sub_choice == '3':
                    # Example function call
                    pass  # Implement top N countries with most total participants here
                elif sub_choice == '4':
                    top_10_countries_by_sex_ratio(Athletes_list)
                elif sub_choice == '5':
                    countries_with_more_female_athletes(Athletes_list)
                elif sub_choice == '6':
                    equal_male_female_countries = countries_with_equal_male_female(Athletes_list)
                    print("Countries with equal male and female athletes:")
                    for country in equal_male_female_countries:
                        print(country)
                elif sub_choice == '7':
                    least_athletes = n_country_with_least_athletes(Athletes_list, 1)
                    print("Country with the least athletes:")
                    for country in least_athletes:
                        print(country['Country'])
                elif sub_choice == '8':
                    threshold = int(input("Enter the threshold number of athletes: "))
                    above_threshold = countries_above_threshold(Athletes_list, threshold)
                    print("Countries with more than the threshold number of athletes:")
                    for country in above_threshold:
                        print(country)
                elif sub_choice == '9':
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == '2':
            while True:
                sub_choice = medal_tally_menu()
                if sub_choice == '1':
                    most_gold_country = country_with_most_gold_medals(Whole_data)
                    print(f"Country with the most gold medals: {most_gold_country}")
                elif sub_choice == '2':
                    print_whole_table(Whole_data)
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == '3':
            while True:
                sub_choice = combined_data_menu()
                if sub_choice == '1':
                    avg_medals = average_medals_per_athlete(Whole_data)
                    print(f"Average medals per athlete: {avg_medals:.2f}")
                elif sub_choice == '2':
                    country_code_list = [entry['Country_Code'] for entry in Athletes_list]
                    missing_countries = find_missing_countries(country_code_list, Whole_data)
                    print("Missing countries:")
                    for code in missing_countries:
                        print(code)
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == '4':
            while True:
                print("\n=== Add or Delete a Country ===")
                print("1. Add a New Country")
                print("2. Delete a Country")
                print("3. Go Back")
                sub_choice = input("Enter your choice (1-3): ")
                
                if sub_choice == '1':
                    Whole_data = add_new_country_flow()
                elif sub_choice == '2':
                    delete_country_flow()
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

