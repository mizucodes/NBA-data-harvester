# NBA Player Data Fetcher

## Description

This Python script retrieves data for NBA players using the balldontlie.io API and saves the data to CSV files. It fetches data for 60 players at a time, starting with player ID 1 and incrementing the player ID by 60 for each subsequent request. The data is saved in files named `player1.csv`, `player2.csv`, and so on, until player ID 5000.

## Requirements

- Python 3
- `requests` library

## Installation

1. Ensure Python 3 is installed on your system.
2. Install the `requests` library using pip:

`pip install requests`

## Usage

Run the script via the terminal with the command associated with what ever system you are on.
The script will automatically start fetching data and save it into CSV files in the current directory.

## Notes

- The script includes a delay of 61 seconds between each API request to comply with rate limits.
- The CSV files contain player details such as name, position, team, and physical attributes.
