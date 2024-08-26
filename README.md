# Olympic Data Analysis Project

## Overview

This project involves merging and analyzing data from the Paris Olympics. We have two main datasets:

1. **Medal Tally**: Contains information about the medal counts for various countries.
2. **Athlete Participation**: Contains data about the number of male and female athletes from each country.

The goal of the project is to combine these datasets to create a comprehensive view of Olympic performance, including:
- Number of athletes by gender
- Medal counts (Gold, Silver, Bronze)
- Total medals won

## Data

### Medal Tally

The `medal_tally` dataset includes:
- `Rank`: The ranking of the country based on the total medals won.
- `Country_Code`: The ISO country code.
- `Country`: The full name of the country.
- `Gold`: Number of gold medals.
- `Silver`: Number of silver medals.
- `Bronze`: Number of bronze medals.
- `Total`: Total number of medals.

### Athlete Participation

The `athletes_list` dataset includes:
- `Country_Code`: The ISO country code.
- `Country`: The full name of the country.
- `Female`: Number of female athletes.
- `Male`: Number of male athletes.
- `Total Athletes`: Total number of athletes.

## Merge Process

1. **Convert the `medal_tally` list to a dictionary**: This allows for quick lookups by `Country_Code`.
2. **Iterate through the `athletes_list`**: For each country, merge the data from `medal_tally`. If the country does not appear in `medal_tally`, set medal counts to zero.
3. **Create a merged dataset**: The resulting data includes:
   - `Country_Code`
   - `Country`
   - `Female`
   - `Male`
   - `Total_Athletes`
   - `Gold`
   - `Silver`
   - `Bronze`
   - `Total_Medals`

## Usage

1. **Prepare Data**: Ensure that both datasets (`medal_tally` and `athletes_list`) are in list format as described above.
2. **Run the Merge Script**: Use the provided Python script to merge the data.
3. **Analyze Results**: The output will be a list of dictionaries with the combined information.

## Contributors

- **Adarsh**: Data analysis and script development.
- **Aditi**: Data processing and documentation.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact:

- **Adarsh**: [adarsh2001gop@gmail.com](adarsh2001gop@gmail.com)
- **Aditi**: [aditirauniyar243@gmail.com](aditirauniyar243@gmail.com)
