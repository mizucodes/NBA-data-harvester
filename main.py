import requests
import csv
import time


# function to retrive the player
def fetch_player_data(start_id, end_id):
    data = []
    for player_id in range(start_id, end_id + 1):
        response = requests.get(
            f"https://www.balldontlie.io/api/v1/players/{player_id}"
        )
        if response.status_code == 200:
            data.append(response.json())
    return data


# two iterators
player_id = 1
file_number = 1

while player_id <= 5000:
    players_data = fetch_player_data(player_id, player_id + 59)

    # flatten the data from .json
    flattened_data = []
    for item in players_data:
        team_info = item.get(
            "team",
            {
                "id": None,
                "abbreviation": None,
                "city": None,
                "conference": None,
                "division": None,
                "full_name": None,
                "name": None,
            },
        )
        flattened_item = {
            "id": item["id"],
            "first_name": item["first_name"],
            "last_name": item["last_name"],
            "position": item["position"],
            "height_feet": item.get("height_feet"),
            "height_inches": item.get("height_inches"),
            "weight_pounds": item.get("weight_pounds"),
            "team_id": team_info["id"],
            "team_abbreviation": team_info["abbreviation"],
            "team_city": team_info["city"],
            "team_conference": team_info["conference"],
            "team_division": team_info["division"],
            "team_full_name": team_info["full_name"],
            "team_name": team_info["name"],
        }
        flattened_data.append(flattened_item)

    # write the player data to a new csv file, number value will iterate
    with open(f"player{file_number}.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=flattened_data[0].keys())
        writer.writeheader()
        for row in flattened_data:
            writer.writerow(row)

    player_id += 60
    file_number += 1
    time.sleep(61)  # 61 second cool down to not over request, *1 per minute*
