import chessdotcom
import collections
from chessdotcom.types import ChessDotComError
import requests

MONTH_TO_COUNT= 3
NUMBER_OF_TOP = 5

def get_all_gambit_archive(acc_name, most=5):
    """recieve all archive of gambits that were played"""

    data = collections.Counter()
    
    chess_archive_response = chessdotcom.get_player_game_archives(acc_name)
    archive_json_by_month = chess_archive_response.json["archives"]
    
    for month_data in archive_json_by_month:
        req = requests.get(month_data).json()["games"]

        for game in req:
            try:
                val = game["pgn"].split("\n")[10][40:-2]
            except KeyError as ex:
                print(ex)
                continue

            if val in data:
                data[val] += 1
            else:
                data[val] = 1
    return data.most_common(n=most)

def get_last_gambits(acc_name, most=NUMBER_OF_TOP, month=MONTH_TO_COUNT):
    """recieve info about gambits name, count and winrate"""
    data = collections.Counter()

    chess_archive_response = chessdotcom.get_player_game_archives(acc_name)
    archive_json_by_month = chess_archive_response.json["archives"][-month:]

    for month_data in archive_json_by_month:
        req = requests.get(month_data).json()["games"]

        for game in req:
            try:
                pgn = game["pgn"].split("\n")
                val = pgn[10][40:-2]
                link = pgn[10][9:-2]
                if acc_name in pgn[16]:
                    win = 1
                elif 'drawn' in pgn[16]:
                    win = 0.5
                else:
                    win = 0
            except KeyError as er:
                continue

            if val in data:
                data[val][0] += 1
                if win:
                    data[val][1] += 1 
            else:
                data[val] = [1, win, link]
    return data.most_common(n=most+1)


def main():
    acc_name = input('input name: ')

    try:
        gambit_stat = get_last_gambits(acc_name)
    except ChessDotComError as er:
        print('No user found')
        return

    gambit_stat = gambit_stat[1:] if not gambit_stat[0][0] else gambit_stat[:-1]

    for gambit in gambit_stat:

        perc = int(round(gambit[1][1] / gambit[1][0], 2) * 100)
        text = gambit[0].ljust(70)
        target = gambit[1][2]
        print(f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\ | {str(gambit[1][0]).rjust(3)} | {perc}%")

if __name__ == '__main__':
    main()