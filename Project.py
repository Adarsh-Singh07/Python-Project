Whole_data = merge_data(Athletes_list, medal_tally)  # Combine data

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

# Main function with an interactive menu
def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Print Athletes Data")
        print("2. Print Medal Tally Data")
        print("3. Combine Data and Analyze")
        print("4. Add or Delete a Country")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\nAthletes Data Options:")
            print("1. Top 10 Countries by Male-to-Female Athlete Ratio")
            print("2. Countries with More Female Athletes")
            print("3. Countries with Equal Male and Female Athletes")
            print("4. n Countries with Least Athletes")
            print("5. Countries with Athletes Above a Threshold")
            sub_choice = input("Enter your choice (1-5): ")

            if sub_choice == '1':
                top_10_countries_by_sex_ratio(Athletes_list)
            elif sub_choice == '2':
                countries_with_more_female_athletes(Athletes_list)
            elif sub_choice == '3':
                countries = countries_with_equal_male_female(Athletes_list)
                print(f"Countries with equal male and female athletes: {countries}")
            elif sub_choice == '4':
                n = int(input("Enter the number of countries: "))
                least_athletes = n_country_with_least_athletes(Athletes_list, n)
                print(f"Countries with the least athletes: {least_athletes}")
            elif sub_choice == '5':
                threshold = int(input("Enter the athlete threshold: "))
                countries = countries_above_threshold(Athletes_list, threshold)
                print(f"Countries with more than {threshold} athletes: {countries}")
            else:
                print("Invalid choice. Please try again.")

        elif choice == '2':
            print("\nMedal Tally Data Options:")
            print("1. Country with Most Gold Medals")
            # Add more medal-related functions as needed
            sub_choice = input("Enter your choice (1): ")

            if sub_choice == '1':
                country = country_with_most_gold_medals(Whole_data)
                print(f"Country with the most gold medals: {country}")
            else:
                print("Invalid choice. Please try again.")

        elif choice == '3':
            print("\nCombine Data and Analyze:")
            print_whole_table(Whole_data)

        elif choice == '4':
            print("\nAdd or Delete a Country:")
            action = input("Enter 'add' to add a country or 'delete' to delete a country: ").lower()
            if action == 'delete':
                country_code = input("Enter the country code to delete: ")
                country_name = input("Enter the country name to delete: ")
                Athletes_list = delete_country(country_code, country_name, Athletes_list)
                medal_tally = delete_country(country_code, country_name, medal_tally)
                Whole_data = delete_country(country_code, country_name, Whole_data)
                rank_country(Whole_data)
                print("Country deleted successfully.")
            else:
                print("Invalid action. Please try again.")

        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function
main()
