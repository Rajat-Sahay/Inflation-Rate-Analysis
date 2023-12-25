# The Inflation Rollercoaster: Up, Down, and Around the World in Five Currencies

## Overview
This repository contains a Python script for web scraping inflation data from www.inflationtool.com for major currencies. The script collects Consumer Price Index (CPI) values for each currency from 1958 to 2022 and organizes the data into CSV files. Additionally, a Power BI dashboard has been created to dynamically visualize and analyze the inflation trends over the specified period.

## Code Structure
The Python script (InflationDataCollection.py) utilizes the requests library for web scraping and BeautifulSoup for HTML parsing. The script extracts CPI values for multiple currencies, creates CSV files for each currency, stores it in a folder (CSV Data), and implements a 5-minute delay between requests to avoid overloading the server.

## Data Visualization
The Power BI dashboard presents an interactive visualization of inflation data. Each currency has a dedicated page displaying line charts representing the CPI values over the years. The dashboard allows users to dynamically explore and compare inflation trends for the United States Dollar (USD), Indian Rupee (INR), British Pound (GBP), Japanese Yen (JPY), and Euro (EUR).

## Usage
1. Clone the Repository
2. Install Dependencies
3. Run the Script
4. Explore the Power BI Dashboard:
  - Open the Power BI file (The Inflation Rollercoaster.pbix) to dynamically view and analyze the inflation data.

## Snapshot of the dashboard
![The Inflation Rollercoaster](https://github.com/Rajat-Sahay/Inflation-Rate-Analysis/assets/154502061/cf08ec19-32a4-4ab7-b36c-e7aef9a5faaf)


## Important Notes
The script respects ethical web scraping practices with a delay between requests.
The Power BI dashboard provides a user-friendly interface for exploring inflation trends.
Feel free to contribute, report issues, or suggest enhancements. Happy analyzing!

##### Author : Rajat Sahay
##### Email : sahay.r@northeastern.edu
##### LinkedIn : [Rajat Sahay](https://www.linkedin.com/in/rajat-sahay-/)
