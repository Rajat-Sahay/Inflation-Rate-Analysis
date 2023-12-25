import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urlparse
import time

url = 'https://www.inflationtool.com/indian-rupee'
response = requests.get(url)

# Create an empty list to store href values and currency names
href_list = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the unordered list with a specific class
    ul_element = soup.find('ul', class_='mt-1 grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-x-6')

    # Check if the ul_element is found
    if ul_element:
        # Find all list items within the unordered list
        list_items = ul_element.find_all('li')

        # Extract href attributes from anchor elements within each list item
        for li in list_items:
            anchor = li.find('a')
            if anchor:
                href = anchor.get('href')
                href_list.append(href)  # Append href value to the list

# Extract currency names from href_list
currency_names = [urlparse(href).path.split('/')[-1] for href in href_list]

# Print the array of href values and currency names
print("Href List:")
print(href_list)
print("\nCurrency Names:")
print(currency_names)

url_pattern = '{base_url}/{year}-to-present-value'

# Loop through each item in href_list
for base_url, currency_name in zip(href_list, currency_names):
    # Open a new CSV file for writing with the corresponding currency name
    with open(f'{currency_name}_cpi_data.csv', 'w', newline='') as csvfile:
        # Create a CSV writer
        csvwriter = csv.writer(csvfile)

        # Write header to CSV file
        csvwriter.writerow(['Year', 'CPI Value'])

        # Loop through the years from 1958 to 2023
        for year in range(1958, 2023):
            # Construct the URL for the current year
            current_url = url_pattern.format(base_url=base_url, year=year)

            # Make a GET request to the URL
            response = requests.get(current_url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find all occurrences of <td> elements with class "text-right text-sm"
                cpi_elements = soup.find_all('td', class_='text-right text-sm')

                # Check if there are at least 3 occurrences
                if len(cpi_elements) >= 3:
                    # Extract the text from the 3rd occurrence
                    cpi_value = cpi_elements[2].text.strip()

                    # Write the data to the CSV file
                    csvwriter.writerow([year, cpi_value])
                else:
                    print(f'Insufficient occurrences of "text-right text-sm" class for {year}. Writing "N/A".')
            else:
                print(f'Failed to retrieve content for {year}. Status code: {response.status_code}. Writing "N/A".')

    # Schedule a temporary hiatus to prevent server overload and maintain data integrity
    print(f'Waiting for 5 minutes...')
    time.sleep(300)
    