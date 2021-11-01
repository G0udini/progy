import chessdotcom
import json
import requests
import pprint
import collections

chess_archive_response = chessdotcom.get_player_game_archives("g0udini")

archive_json_by_month = chess_archive_response.json["archives"]


def get_all_gambit_archive():
    data = collections.Counter()

    for month_data in archive_json_by_month:
        req = requests.get(month_data).json()["games"]

        for game in req:
            val = game["pgn"].split("\n")[10][40:-2]
            if val in data:
                data[val] += 1
            else:
                data[val] = 1
    pprint.pprint(data.most_common(n=5))


# req_last_month = requests.get(archive_json_by_month[-2])


# data = collections.Counter()

# r = req_last_month.json()["games"]

# for i in range(len(r)):
#     val = r[i]["pgn"].split("\n")[10][40:-2]
#     if val in data:
#         data[val] += 1
#     else:
#         data[val] = 1
# pprint.pprint(data.most_common(n=5))


# jsonr = r.json()["games"][0]["pgn"][11]

# get_player_games_by_month
