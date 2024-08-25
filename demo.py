#List Of Countries by their athletes counts

Athletes_list = [
    {'Country_Code': 'USA', 'Country': 'United States', 'Female': 328, 'Male': 291, 'Total Athletes': 619},
    {'Country_Code': 'FRA', 'Country': 'France', 'Female': 295, 'Male': 305, 'Total Athletes': 600},
    {'Country_Code': 'AUS', 'Country': 'Australia', 'Female': 265, 'Male': 210, 'Total Athletes': 475},
    {'Country_Code': 'GER', 'Country': 'Germany', 'Female': 225, 'Male': 232, 'Total Athletes': 457},
    {'Country_Code': 'JPN', 'Country': 'Japan', 'Female': 201, 'Male': 230, 'Total Athletes': 431},
    {'Country_Code': 'ESP', 'Country': 'Spain', 'Female': 202, 'Male': 199, 'Total Athletes': 401},
    {'Country_Code': 'CHN', 'Country': 'China', 'Female': 264, 'Male': 134, 'Total Athletes': 398},
    {'Country_Code': 'ITA', 'Country': 'Italy', 'Female': 192, 'Male': 205, 'Total Athletes': 397},
    {'Country_Code': 'GBR', 'Country': 'Great Britain', 'Female': 178, 'Male': 164, 'Total Athletes': 342},
    {'Country_Code': 'CAN', 'Country': 'Canada', 'Female': 203, 'Male': 129, 'Total Athletes': 332},
    {'Country_Code': 'BRA', 'Country': 'Brazil', 'Female': 164, 'Male': 126, 'Total Athletes': 290},
    {'Country_Code': 'NED', 'Country': 'Netherlands', 'Female': 172, 'Male': 117, 'Total Athletes': 289},
    {'Country_Code': 'POL', 'Country': 'Poland', 'Female': 124, 'Male': 102, 'Total Athletes': 226},
    {'Country_Code': 'NZL', 'Country': 'New Zealand', 'Female': 101, 'Male': 107, 'Total Athletes': 208},
    {'Country_Code': 'HUN', 'Country': 'Hungary', 'Female': 85, 'Male': 92, 'Total Athletes': 177},
    {'Country_Code': 'BEL', 'Country': 'Belgium', 'Female': 88, 'Male': 89, 'Total Athletes': 177},
    {'Country_Code': 'EGY', 'Country': 'Egypt', 'Female': 54, 'Male': 103, 'Total Athletes': 157},
    {'Country_Code': 'KOR', 'Country': 'Korea', 'Female': 81, 'Male': 66, 'Total Athletes': 147},
    {'Country_Code': 'IRL', 'Country': 'Ireland', 'Female': 69, 'Male': 74, 'Total Athletes': 143},
    {'Country_Code': 'ARG', 'Country': 'Argentina', 'Female': 33, 'Male': 110, 'Total Athletes': 143},
    {'Country_Code': 'RSA', 'Country': 'South Africa', 'Female': 63, 'Male': 78, 'Total Athletes': 141},
    {'Country_Code': 'UKR', 'Country': 'Ukraine', 'Female': 69, 'Male': 72, 'Total Athletes': 141},
    {'Country_Code': 'SUI', 'Country': 'Switzerland', 'Female': 66, 'Male': 71, 'Total Athletes': 137},
    {'Country_Code': 'DEN', 'Country': 'Denmark', 'Female': 74, 'Male': 57, 'Total Athletes': 131},
    {'Country_Code': 'SWE', 'Country': 'Sweden', 'Female': 66, 'Male': 59, 'Total Athletes': 125},
    {'Country_Code': 'SRB', 'Country': 'Serbia', 'Female': 44, 'Male': 70, 'Total Athletes': 114},
    {'Country_Code': 'IND', 'Country': 'India', 'Female': 46, 'Male': 66, 'Total Athletes': 112},
    {'Country_Code': 'CZE', 'Country': 'Czechia', 'Female': 49, 'Male': 62, 'Total Athletes': 111},
    {'Country_Code': 'NOR', 'Country': 'Norway', 'Female': 53, 'Male': 56, 'Total Athletes': 109},
    {'Country_Code': 'MEX', 'Country': 'Mexico', 'Female': 63, 'Male': 45, 'Total Athletes': 108},
    {'Country_Code': 'TUR', 'Country': 'Türkiye', 'Female': 54, 'Male': 47, 'Total Athletes': 101},
    {'Country_Code': 'GRE', 'Country': 'Greece', 'Female': 41, 'Male': 59, 'Total Athletes': 100},
    {'Country_Code': 'ROU', 'Country': 'Romania', 'Female': 47, 'Male': 49, 'Total Athletes': 96},
    {'Country_Code': 'SLO', 'Country': 'Slovenia', 'Female': 47, 'Male': 48, 'Total Athletes': 95},
    {'Country_Code': 'ISR', 'Country': 'Israel', 'Female': 33, 'Male': 56, 'Total Athletes': 89},
    {'Country_Code': 'COL', 'Country': 'Colombia', 'Female': 51, 'Male': 37, 'Total Athletes': 88},
    {'Country_Code': 'UZB', 'Country': 'Uzbekistan', 'Female': 31, 'Male': 57, 'Total Athletes': 88},
    {'Country_Code': 'NGR', 'Country': 'Nigeria', 'Female': 63, 'Male': 23, 'Total Athletes': 86},
    {'Country_Code': 'AUT', 'Country': 'Austria', 'Female': 37, 'Male': 47, 'Total Athletes': 84},
    {'Country_Code': 'KAZ', 'Country': 'Kazakhstan', 'Female': 25, 'Male': 54, 'Total Athletes': 79},
    {'Country_Code': 'POR', 'Country': 'Portugal', 'Female': 37, 'Male': 38, 'Total Athletes': 75},
    {'Country_Code': 'KEN', 'Country': 'Kenya', 'Female': 34, 'Male': 40, 'Total Athletes': 74},
    {'Country_Code': 'CRO', 'Country': 'Croatia', 'Female': 15, 'Male': 58, 'Total Athletes': 73},
    {'Country_Code': 'JAM', 'Country': 'Jamaica', 'Female': 32, 'Male': 33, 'Total Athletes': 65},
    {'Country_Code': 'MAR', 'Country': 'Morocco', 'Female': 18, 'Male': 43, 'Total Athletes': 61},
    {'Country_Code': 'CUB', 'Country': 'Cuba', 'Female': 27, 'Male': 34, 'Total Athletes': 61},
    {'Country_Code': 'TPE', 'Country': 'Chinese Taipei', 'Female': 34, 'Male': 26, 'Total Athletes': 60},
    {'Country_Code': 'DOM', 'Country': 'Dominican Republic', 'Female': 25, 'Male': 34, 'Total Athletes': 59},
    {'Country_Code': 'FIN', 'Country': 'Finland', 'Female': 34, 'Male': 23, 'Total Athletes': 57},
    {'Country_Code': 'THA', 'Country': 'Thailand', 'Female': 28, 'Male': 24, 'Total Athletes': 52},
    {'Country_Code': 'LTU', 'Country': 'Lithuania', 'Female': 24, 'Male': 27, 'Total Athletes': 51},
    {'Country_Code': 'PUR', 'Country': 'Puerto Rico', 'Female': 24, 'Male': 27, 'Total Athletes': 51},
    {'Country_Code': 'AZE', 'Country': 'Azerbaijan', 'Female': 20, 'Male': 28, 'Total Athletes': 48},
    {'Country_Code': 'CHI', 'Country': 'Chile', 'Female': 18, 'Male': 30, 'Total Athletes': 48},
    {'Country_Code': 'BUL', 'Country': 'Bulgaria', 'Female': 25, 'Male': 21, 'Total Athletes': 46},
    {'Country_Code': 'ALG', 'Country': 'Algeria', 'Female': 19, 'Male': 27, 'Total Athletes': 46},
    {'Country_Code': 'IRI', 'Country': 'IR Iran', 'Female': 11, 'Male': 30, 'Total Athletes': 41},
    {'Country_Code': 'ECU', 'Country': 'Ecuador', 'Female': 24, 'Male': 16, 'Total Athletes': 40},
    {'Country_Code': 'EOR', 'Country': 'EOR', 'Female': 13, 'Male': 24, 'Total Athletes': 37},
    {'Country_Code': 'FIJ', 'Country': 'Fiji', 'Female': 17, 'Male': 19, 'Total Athletes': 36},
    {'Country_Code': 'HKG', 'Country': 'Hong Kong, China', 'Female': 18, 'Male': 16, 'Total Athletes': 34},
    {'Country_Code': 'ETH', 'Country': 'Ethiopia', 'Female': 17, 'Male': 16, 'Total Athletes': 33},
    {'Country_Code': 'AIN', 'Country': 'AIN', 'Female': 17, 'Male': 15, 'Total Athletes': 32},
    {'Country_Code': 'MGL', 'Country': 'Mongolia', 'Female': 18, 'Male': 14, 'Total Athletes': 32},
    {'Country_Code': 'ZAM', 'Country': 'Zambia', 'Female': 22, 'Male': 9, 'Total Athletes': 31},
    {'Country_Code': 'VEN', 'Country': 'Venezuela', 'Female': 14, 'Male': 17, 'Total Athletes': 31},
    {'Country_Code': 'PAR', 'Country': 'Paraguay', 'Female': 6, 'Male': 23, 'Total Athletes': 29},
    {'Country_Code': 'INA', 'Country': 'Indonesia', 'Female': 13, 'Male': 16, 'Total Athletes': 29},
    {'Country_Code': 'LAT', 'Country': 'Latvia', 'Female': 13, 'Male': 16, 'Total Athletes': 29},
    {'Country_Code': 'SVK', 'Country': 'Slovakia', 'Female': 14, 'Male': 14, 'Total Athletes': 28},
    {'Country_Code': 'GEO', 'Country': 'Georgia', 'Female': 7, 'Male': 21, 'Total Athletes': 28},
    {'Country_Code': 'URU', 'Country': 'Uruguay', 'Female': 4, 'Male': 23, 'Total Athletes': 27},
    {'Country_Code': 'MAS', 'Country': 'Malaysia', 'Female': 13, 'Male': 13, 'Total Athletes': 26},
    {'Country_Code': 'TUN', 'Country': 'Tunisia', 'Female': 14, 'Male': 12, 'Total Athletes': 26},
    {'Country_Code': 'PER', 'Country': 'Peru', 'Female': 17, 'Male': 9, 'Total Athletes': 26},
    {'Country_Code': 'MDA', 'Country': 'Republic of Moldova', 'Female': 12, 'Male': 14, 'Total Athletes': 26},
    {'Country_Code': 'GUI', 'Country': 'Guinea', 'Female': 5, 'Male': 20, 'Total Athletes': 25},
    {'Country_Code': 'UGA', 'Country': 'Uganda', 'Female': 13, 'Male': 12, 'Total Athletes': 25},
    {'Country_Code': 'ANG', 'Country': 'Angola', 'Female': 17, 'Male': 8, 'Total Athletes': 25},
    {'Country_Code': 'SAM', 'Country': 'Samoa', 'Female': 4, 'Male': 20, 'Total Athletes': 24},
    {'Country_Code': 'MLI', 'Country': 'Mali', 'Female': 2, 'Male': 22, 'Total Athletes': 24},
    {'Country_Code': 'EST', 'Country': 'Estonia', 'Female': 8, 'Male': 16, 'Total Athletes': 24},
    {'Country_Code': 'SGP', 'Country': 'Singapore', 'Female': 16, 'Male': 7, 'Total Athletes': 23},
    {'Country_Code': 'IRQ', 'Country': 'Iraq', 'Female': 0, 'Male': 23, 'Total Athletes': 23},
    {'Country_Code': 'PHI', 'Country': 'Philippines', 'Female': 15, 'Male': 7, 'Total Athletes': 22},
    {'Country_Code': 'BAH', 'Country': 'Bahamas', 'Female': 8, 'Male': 11, 'Total Athletes': 19},
    {'Country_Code': 'MNE', 'Country': 'Montenegro', 'Female': 3, 'Male': 16, 'Total Athletes': 19},
    {'Country_Code': 'TTO', 'Country': 'Trinidad and Tobago', 'Female': 7, 'Male': 10, 'Total Athletes': 17},
    {'Country_Code': 'VIE', 'Country': 'Vietnam', 'Female': 12, 'Male': 4, 'Total Athletes': 16},
    {'Country_Code': 'KGZ', 'Country': 'Kyrgyzstan', 'Female': 5, 'Male': 11, 'Total Athletes': 16},
    {'Country_Code': 'GUA', 'Country': 'Guatemala', 'Female': 6, 'Male': 10, 'Total Athletes': 16},
    {'Country_Code': 'CYP', 'Country': 'Cyprus', 'Female': 9, 'Male': 6, 'Total Athletes': 15},
    {'Country_Code': 'ARM', 'Country': 'Armenia', 'Female': 2, 'Male': 13, 'Total Athletes': 15},
    {'Country_Code': 'BOT', 'Country': 'Botswana', 'Female': 2, 'Male': 12, 'Total Athletes': 14},
    {'Country_Code': 'PRK', 'Country': 'DPR Korea', 'Female': 10, 'Male': 4, 'Total Athletes': 14},
    {'Country_Code': 'SRI', 'Country': 'Sri Lanka', 'Female': 9, 'Male': 5, 'Total Athletes': 14},
    {'Country_Code': 'CIV', 'Country': 'Côte d’Ivoire', 'Female': 7, 'Male': 6, 'Total Athletes': 13},
    {'Country_Code': 'BIH', 'Country': 'Bosnia and Herzegovina', 'Female': 4, 'Male': 8, 'Total Athletes': 12},
    {'Country_Code': 'SEN', 'Country': 'Senegal', 'Female': 2, 'Male': 10, 'Total Athletes': 12},
    {'Country_Code': 'HON', 'Country': 'Honduras', 'Female': 4, 'Male': 8, 'Total Athletes': 12},
    {'Country_Code': 'SYR', 'Country': 'Syrian Arab Republic', 'Female': 5, 'Male': 6, 'Total Athletes': 11},
    {'Country_Code': 'BAR', 'Country': 'Barbados', 'Female': 5, 'Male': 6, 'Total Athletes': 11},
    {'Country_Code': 'QAT', 'Country': 'Qatar', 'Female': 4, 'Male': 7, 'Total Athletes': 11},
    {'Country_Code': 'SUD', 'Country': 'Sudan', 'Female': 5, 'Male': 5, 'Total Athletes': 10},
    {'Country_Code': 'KOS', 'Country': 'Kosovo', 'Female': 4, 'Male': 5, 'Total Athletes': 9},
    {'Country_Code': 'MRI', 'Country': 'Mauritius', 'Female': 3, 'Male': 6, 'Total Athletes': 9},
    {'Country_Code': 'SUR', 'Country': 'Suriname', 'Female': 2, 'Male': 6, 'Total Athletes': 8},
    {'Country_Code': 'LBN', 'Country': 'Lebanon', 'Female': 3, 'Male': 4, 'Total Athletes': 7},
    {'Country_Code': 'TJK', 'Country': 'Tajikistan', 'Female': 2, 'Male': 5, 'Total Athletes': 7},
    {'Country_Code': 'TOG', 'Country': 'Togo', 'Female': 3, 'Male': 4, 'Total Athletes': 7},
    {'Country_Code': 'CPV', 'Country': 'Cabo Verde', 'Female': 3, 'Male': 4, 'Total Athletes': 7},
    {'Country_Code': 'NEP', 'Country': 'Nepal', 'Female': 5, 'Male': 2, 'Total Athletes': 7},
    {'Country_Code': 'SOM', 'Country': 'Somalia', 'Female': 5, 'Male': 1, 'Total Athletes': 6},
    {'Country_Code': 'DJI', 'Country': 'Djibouti', 'Female': 1, 'Male': 5, 'Total Athletes': 6},
    {'Country_Code': 'GAB', 'Country': 'Gabon', 'Female': 1, 'Male': 5, 'Total Athletes': 6},
    {'Country_Code': 'COD', 'Country': 'Democratic Republic of the Congo', 'Female': 1, 'Male': 4, 'Total Athletes': 5},
    {'Country_Code': 'TLS', 'Country': 'Timor-Leste', 'Female': 2, 'Male': 3, 'Total Athletes': 5},
    {'Country_Code': 'SEY', 'Country': 'Seychelles', 'Female': 3, 'Male': 2, 'Total Athletes': 5},
    {'Country_Code': 'CGO', 'Country': 'Congo', 'Female': 3, 'Male': 2, 'Total Athletes': 5},
    {'Country_Code': 'MDV', 'Country': 'Maldives', 'Female': 4, 'Male': 0, 'Total Athletes': 4},
    {'Country_Code': 'SMR', 'Country': 'San Marino', 'Female': 2, 'Male': 2, 'Total Athletes': 4},
    {'Country_Code': 'BIZ', 'Country': 'Belize', 'Female': 3, 'Male': 1, 'Total Athletes': 4},
    {'Country_Code': 'HAI', 'Country': 'Haiti', 'Female': 2, 'Male': 2, 'Total Athletes': 4},
    {'Country_Code': 'KIR', 'Country': 'Kiribati', 'Female': 1, 'Male': 2, 'Total Athletes': 3},
    {'Country_Code': 'BRU', 'Country': 'Brunei Darussalam', 'Female': 1, 'Male': 2, 'Total Athletes': 3},
    {'Country_Code': 'CHA', 'Country': 'Chad', 'Female': 1, 'Male': 2, 'Total Athletes': 3},
    {'Country_Code': 'LAO', 'Country': 'Lao People\'s Democratic Republic', 'Female': 1, 'Male': 2, 'Total Athletes': 3},
    {'Country_Code': 'MAL', 'Country': 'Malta', 'Female': 1, 'Male': 2, 'Total Athletes': 3},
    {'Country_Code': 'ISL', 'Country': 'Iceland', 'Female': 2, 'Male': 0, 'Total Athletes': 2},
    {'Country_Code': 'STP', 'Country': 'Sao Tome and Principe', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'CAM', 'Country': 'Cambodia', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'YEM', 'Country': 'Yemen', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'AND', 'Country': 'Andorra', 'Female': 0, 'Male': 2, 'Total Athletes': 2},
    {'Country_Code': 'BER', 'Country': 'Bermuda', 'Female': 0, 'Male': 2, 'Total Athletes': 2},
    {'Country_Code': 'SOL', 'Country': 'Solomon Islands', 'Female': 1, 'Male': 0, 'Total Athletes': 1},
    {'Country_Code': 'LBR', 'Country': 'Liberia', 'Female': 1, 'Male': 0, 'Total Athletes': 1},
    {'Country_Code': 'TUV', 'Country': 'Tuvalu', 'Female': 1, 'Male': 0, 'Total Athletes': 1},
    {'Country_Code': 'RWA', 'Country': 'Rwanda', 'Female': 1, 'Male': 0, 'Total Athletes': 1},
    {'Country_Code': 'STK', 'Country': 'St Kitts and Nevis', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'CUW', 'Country': 'Curaçao', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'LBA', 'Country': 'Libya', 'Female': 1, 'Male': 3, 'Total Athletes': 4},
    {'Country_Code': 'MYA', 'Country': 'Myanmar', 'Female': 0, 'Male': 3, 'Total Athletes': 3}, 
    {'Country_Code': 'COM', 'Country': 'Comoros', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'CAF', 'Country': 'Central African Republic', 'Female': 0, 'Male': 2, 'Total Athletes': 2},
    {'Country_Code': 'SLE', 'Country': 'Sierra Leone', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'MAD', 'Country': 'Madagascar', 'Female': 0, 'Male': 2, 'Total Athletes': 2},
    {'Country_Code': 'LES', 'Country': 'Lesotho', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'MTN', 'Country': 'Mauritania', 'Female': 0, 'Male': 2, 'Total Athletes': 2},
    {'Country_Code': 'SWZ', 'Country': 'Eswatini', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'BEN', 'Country': 'Benin', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'NAM', 'Country': 'Namibia', 'Female': 2, 'Male': 0, 'Total Athletes': 2},
    {'Country_Code': 'FSM', 'Country': 'Micronesia', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'GAM', 'Country': 'Gambia', 'Female': 1, 'Male': 1, 'Total Athletes': 2},
    {'Country_Code': 'PLW', 'Country': 'Palau', 'Female': 1, 'Male': 0, 'Total Athletes': 1},
    {'Country_Code': 'SSD', 'Country': 'South Sudan', 'Female': 1, 'Male': 0, 'Total Athletes': 1},
    {'Country_Code': 'TGA', 'Country': 'Tonga', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'COK', 'Country': 'Cook Islands', 'Female': 1, 'Male': 0, 'Total Athletes': 1},
    {'Country_Code': 'MTQ', 'Country': 'Martinique', 'Female': 1, 'Male': 0, 'Total Athletes': 1},
    {'Country_Code': 'VIN', 'Country': 'Saint Vincent and the Grenadines', 'Female': 1, 'Male': 0, 'Total Athletes': 1},
    {'Country_Code': 'VAN', 'Country': 'Vanuatu', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'GRN', 'Country': 'Grenada', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'MHL', 'Country': 'Marshall Islands', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'DMA', 'Country': 'Dominica', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'MON', 'Country': 'Monaco', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'NRU', 'Country': 'Nauru', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'NCA', 'Country': 'Nicaragua', 'Female': 0, 'Male': 1, 'Total Athletes': 1},
    {'Country_Code': 'MAW', 'Country': 'Malawi', 'Female': 0, 'Male': 1, 'Total Athletes': 1}

]
print(len(Athletes_list))

#Medal Tally By Country Details
medal_tally = [
     {"Rank": 1, "Country_Code": "USA", "Country": "United States", "Gold": 40, "Silver": 44, "Bronze": 42, "Total": 126},
    {"Rank": 2, "Country_Code": "CHN", "Country": "China", "Gold": 40, "Silver": 27, "Bronze": 24, "Total": 91},
    {"Rank": 3, "Country_Code": "JPN", "Country": "Japan", "Gold": 20, "Silver": 12, "Bronze": 13, "Total": 45},
    {"Rank": 4, "Country_Code": "AUS", "Country": "Australia", "Gold": 18, "Silver": 19, "Bronze": 16, "Total": 53},
    {"Rank": 5, "Country_Code": "FRA", "Country": "France", "Gold": 16, "Silver": 26, "Bronze": 22, "Total": 64},
    {"Rank": 6, "Country_Code": "NED", "Country": "Netherlands", "Gold": 15, "Silver": 7, "Bronze": 12, "Total": 34},
    {"Rank": 7, "Country_Code": "GBR", "Country": "Great Britain", "Gold": 14, "Silver": 22, "Bronze": 29, "Total": 65},
    {"Rank": 8, "Country_Code": "KOR", "Country": "Korea", "Gold": 13, "Silver": 9, "Bronze": 10, "Total": 32},
    {"Rank": 9, "Country_Code": "ITA", "Country": "Italy", "Gold": 12, "Silver": 13, "Bronze": 15, "Total": 40},
    {"Rank": 10, "Country_Code": "GER", "Country": "Germany", "Gold": 12, "Silver": 13, "Bronze": 8, "Total": 33},
    {"Rank": 11, "Country_Code": "NZL", "Country": "New Zealand", "Gold": 10, "Silver": 7, "Bronze": 3, "Total": 20},
    {"Rank": 12, "Country_Code": "CAN", "Country": "Canada", "Gold": 9, "Silver": 7, "Bronze": 11, "Total": 27},
    {"Rank": 13, "Country_Code": "UZB", "Country": "Uzbekistan", "Gold": 8, "Silver": 2, "Bronze": 3, "Total": 13},
    {"Rank": 14, "Country_Code": "HUN", "Country": "Hungary", "Gold": 6, "Silver": 7, "Bronze": 6, "Total": 19},
    {"Rank": 15, "Country_Code": "ESP", "Country": "Spain", "Gold": 5, "Silver": 4, "Bronze": 9, "Total": 18},
    {"Rank": 16, "Country_Code": "SWE", "Country": "Sweden", "Gold": 4, "Silver": 4, "Bronze": 3, "Total": 11},
    {"Rank": 17, "Country_Code": "KEN", "Country": "Kenya", "Gold": 4, "Silver": 2, "Bronze": 5, "Total": 11},
    {"Rank": 18, "Country_Code": "NOR", "Country": "Norway", "Gold": 4, "Silver": 1, "Bronze": 3, "Total": 8},
    {"Rank": 19, "Country_Code": "IRL", "Country": "Ireland", "Gold": 4, "Silver": 0, "Bronze": 3, "Total": 7},
    {"Rank": 20, "Country_Code": "BRA", "Country": "Brazil", "Gold": 3, "Silver": 7, "Bronze": 10, "Total": 20},
    {"Rank": 21, "Country_Code": "IRI", "Country": "IR Iran", "Gold": 3, "Silver": 6, "Bronze": 3, "Total": 12},
    {"Rank": 22, "Country_Code": "UKR", "Country": "Ukraine", "Gold": 3, "Silver": 5, "Bronze": 4, "Total": 12},
    {"Rank": 23, "Country_Code": "ROU", "Country": "Romania", "Gold": 3, "Silver": 4, "Bronze": 2, "Total": 9},
    {"Rank": 24, "Country_Code": "GEO", "Country": "Georgia", "Gold": 3, "Silver": 3, "Bronze": 1, "Total": 7},
    {"Rank": 25, "Country_Code": "BEL", "Country": "Belgium", "Gold": 3, "Silver": 1, "Bronze": 6, "Total": 10},
    {"Rank": 26, "Country_Code": "BUL", "Country": "Bulgaria", "Gold": 3, "Silver": 1, "Bronze": 3, "Total": 7},
    {"Rank": 27, "Country_Code": "SRB", "Country": "Serbia", "Gold": 3, "Silver": 1, "Bronze": 1, "Total": 5},
    {"Rank": 28, "Country_Code": "CZE", "Country": "Czechia", "Gold": 3, "Silver": 0, "Bronze": 2, "Total": 5},
    {"Rank": 29, "Country_Code": "DEN", "Country": "Denmark", "Gold": 2, "Silver": 2, "Bronze": 5, "Total": 9},
    {"Rank": 30, "Country_Code": "AZE", "Country": "Azerbaijan", "Gold": 2, "Silver": 2, "Bronze": 3, "Total": 7},
    {"Rank": 31, "Country_Code": "CRO", "Country": "Croatia", "Gold": 2, "Silver": 2, "Bronze": 3, "Total": 7},
    {"Rank": 32, "Country_Code": "CUB", "Country": "Cuba", "Gold": 2, "Silver": 1, "Bronze": 6, "Total": 9},
    {"Rank": 33, "Country_Code": "BRN", "Country": "Bahrain", "Gold": 2, "Silver": 1, "Bronze": 1, "Total": 4},
    {"Rank": 34, "Country_Code": "SLO", "Country": "Slovenia", "Gold": 2, "Silver": 1, "Bronze": 0, "Total": 3},
    {"Rank": 35, "Country_Code": "TPE", "Country": "Chinese Taipei", "Gold": 2, "Silver": 0, "Bronze": 5, "Total": 7},
    {"Rank": 36, "Country_Code": "AUT", "Country": "Austria", "Gold": 2, "Silver": 0, "Bronze": 3, "Total": 5},
    {"Rank": 37, "Country_Code": "HKG", "Country": "Hong Kong, China", "Gold": 2, "Silver": 0, "Bronze": 2, "Total": 4},
    {"Rank": 38, "Country_Code": "PHI", "Country": "Philippines", "Gold": 2, "Silver": 0, "Bronze": 2, "Total": 4},
    {"Rank": 39, "Country_Code": "ALG", "Country": "Algeria", "Gold": 2, "Silver": 0, "Bronze": 1, "Total": 3},
    {"Rank": 40, "Country_Code": "INA", "Country": "Indonesia", "Gold": 2, "Silver": 0, "Bronze": 0, "Total": 2},
    {"Rank": 41, "Country_Code": "ISR", "Country": "Israel", "Gold": 1, "Silver": 5, "Bronze": 1, "Total": 7},
    {"Rank": 42, "Country_Code": "POL", "Country": "Poland", "Gold": 1, "Silver": 4, "Bronze": 5, "Total": 10},
    {"Rank": 43, "Country_Code": "KAZ", "Country": "Kazakhstan", "Gold": 1, "Silver": 3, "Bronze": 3, "Total": 7},
    {"Rank": 44, "Country_Code": "JAM", "Country": "Jamaica", "Gold": 1, "Silver": 3, "Bronze": 2, "Total": 6},
    {"Rank": 45, "Country_Code": "RSA", "Country": "South Africa", "Gold": 1, "Silver": 3, "Bronze": 2, "Total": 6},
    {"Rank": 46, "Country_Code": "THA", "Country": "Thailand", "Gold": 1, "Silver": 3, "Bronze": 2, "Total": 6},
    {"Rank": 47, "Country_Code": "AIN", "Country": "AIN", "Gold": 1, "Silver": 3, "Bronze": 1, "Total": 5},
    {"Rank": 48, "Country_Code": "ETH", "Country": "Ethiopia", "Gold": 1, "Silver": 3, "Bronze": 0, "Total": 4},
    {"Rank": 49, "Country_Code": "SUI", "Country": "Switzerland", "Gold": 1, "Silver": 2, "Bronze": 5, "Total": 8},
    {"Rank": 50, "Country_Code": "ECU", "Country": "Ecuador", "Gold": 1, "Silver": 2, "Bronze": 2, "Total": 5},
    {"Rank": 51, "Country_Code": "POR", "Country": "Portugal", "Gold": 1, "Silver": 2, "Bronze": 1, "Total": 4},
    {"Rank": 52, "Country_Code": "GRE", "Country": "Greece", "Gold": 1, "Silver": 1, "Bronze": 6, "Total": 8},
    {"Rank": 53, "Country_Code": "ARG", "Country": "Argentina", "Gold": 1, "Silver": 1, "Bronze": 1, "Total": 3},
    {"Rank": 54, "Country_Code": "EGY", "Country": "Egypt", "Gold": 1, "Silver": 1, "Bronze": 1, "Total": 3},
    {"Rank": 55, "Country_Code": "TUN", "Country": "Tunisia", "Gold": 1, "Silver": 1, "Bronze": 1, "Total": 3},
    {"Rank": 56, "Country_Code": "BOT", "Country": "Botswana", "Gold": 1, "Silver": 1, "Bronze": 0, "Total": 2},
    {"Rank": 57, "Country_Code": "CHI", "Country": "Chile", "Gold": 1, "Silver": 1, "Bronze": 0, "Total": 2},
    {"Rank": 58, "Country_Code": "LCA", "Country": "Saint Lucia", "Gold": 1, "Silver": 1, "Bronze": 0, "Total": 2},
    {"Rank": 59, "Country_Code": "UGA", "Country": "Uganda", "Gold": 1, "Silver": 1, "Bronze": 0, "Total": 2},
    {"Rank": 60, "Country_Code": "DOM", "Country": "Dominican Republic", "Gold": 1, "Silver": 0, "Bronze": 2, "Total": 3},
    {"Rank": 61, "Country_Code": "GUA", "Country": "Guatemala", "Gold": 1, "Silver": 0, "Bronze": 1, "Total": 2},
    {"Rank": 62, "Country_Code": "MAR", "Country": "Morocco", "Gold": 1, "Silver": 0, "Bronze": 1, "Total": 2},
    {"Rank": 63, "Country_Code": "DMA", "Country": "Dominica", "Gold": 1, "Silver": 0, "Bronze": 0, "Total": 1},
    {"Rank": 64, "Country_Code": "PAK", "Country": "Pakistan", "Gold": 1, "Silver": 0, "Bronze": 0, "Total": 1},
    {"Rank": 65, "Country_Code": "TUR", "Country": "Türkiye", "Gold": 0, "Silver": 3, "Bronze": 5, "Total": 8},
    {"Rank": 66, "Country_Code": "MEX", "Country": "Mexico", "Gold": 0, "Silver": 3, "Bronze": 2, "Total": 5},
    {"Rank": 67, "Country_Code": "ARM", "Country": "Armenia", "Gold": 0, "Silver": 3, "Bronze": 1, "Total": 4},
    {"Rank": 68, "Country_Code": "COL", "Country": "Colombia", "Gold": 0, "Silver": 3, "Bronze": 1, "Total": 4},
    {"Rank": 69, "Country_Code": "PRK", "Country": "DPR Korea", "Gold": 0, "Silver": 2, "Bronze": 4, "Total": 6},
    {"Rank": 70, "Country_Code": "KGZ", "Country": "Kyrgyzstan", "Gold": 0, "Silver": 2, "Bronze": 4, "Total": 6},
    {"Rank": 71, "Country_Code": "LTU", "Country": "Lithuania", "Gold": 0, "Silver": 2, "Bronze": 2, "Total": 4},
    {"Rank": 72, "Country_Code": "IND", "Country": "India", "Gold": 0, "Silver": 1, "Bronze": 5, "Total": 6},
    {"Rank": 73, "Country_Code": "MDA", "Country": "Republic of Moldova", "Gold": 0, "Silver": 1, "Bronze": 3, "Total": 4},
    {"Rank": 74, "Country_Code": "KOS", "Country": "Kosovo", "Gold": 0, "Silver": 1, "Bronze": 1, "Total": 2},
    {"Rank": 75, "Country_Code": "CYP", "Country": "Cyprus", "Gold": 0, "Silver": 1, "Bronze": 0, "Total": 1},
    {"Rank": 76, "Country_Code": "FIJ", "Country": "Fiji", "Gold": 0, "Silver": 1, "Bronze": 0, "Total": 1},
    {"Rank": 77, "Country_Code": "JOR", "Country": "Jordan", "Gold": 0, "Silver": 1, "Bronze": 0, "Total": 1},
    {"Rank": 78, "Country_Code": "MGL", "Country": "Mongolia", "Gold": 0, "Silver": 1, "Bronze": 0, "Total": 1},
    {"Rank": 79, "Country_Code": "PAN", "Country": "Panama", "Gold": 0, "Silver": 1, "Bronze": 0, "Total": 1},
    {"Rank": 80, "Country_Code": "TJK", "Country": "Tajikistan", "Gold": 0, "Silver": 0, "Bronze": 3, "Total": 3},
    {"Rank": 81, "Country_Code": "ALB", "Country": "Albania", "Gold": 0, "Silver": 0, "Bronze": 2, "Total": 2},
    {"Rank": 82, "Country_Code": "GRN", "Country": "Grenada", "Gold": 0, "Silver": 0, "Bronze": 2, "Total": 2},
    {"Rank": 83, "Country_Code": "MAS", "Country": "Malaysia", "Gold": 0, "Silver": 0, "Bronze": 2, "Total": 2},
    {"Rank": 84, "Country_Code": "PUR", "Country": "Puerto Rico", "Gold": 0, "Silver": 0, "Bronze": 2, "Total": 2},
    {"Rank": 85, "Country_Code": "CPV", "Country": "Cabo Verde", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 86, "Country_Code": "CIV", "Country": "Côte d'Ivoire", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 87, "Country_Code": "EOR", "Country": "Refugee Olympic Team", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 88, "Country_Code": "NAM", "Country": "Namibia", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 89, "Country_Code": "NGR", "Country": "Nigeria", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 90, "Country_Code": "QAT", "Country": "Qatar", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 91, "Country_Code": "KSA", "Country": "Saudi Arabia", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 92, "Country_Code": "SEN", "Country": "Senegal", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 93, "Country_Code": "SRI", "Country": "Sri Lanka", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 94, "Country_Code": "SYR", "Country": "Syria", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 95, "Country_Code": "TTO", "Country": "Trinidad and Tobago", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1},
    {"Rank": 96, "Country_Code": "VEN", "Country": "Venezuela", "Gold": 0, "Silver": 0, "Bronze": 1, "Total": 1}
]

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

