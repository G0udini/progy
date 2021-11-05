## What does this script do

This script use chess.com api to collect information about players.
In particular, 2 functions are implemented:
1. First ```get_all_gambit_archive``` gives info about all gambits that were recognized by the site and contains data from all the matches that were played by the user
2. Scond one, starts by default and shows top 5 most played gambits that were played  by the user within 3 last months and theres winrate.


## How to use the script:
1. Clone the script from github repository
2. Create python virtual environment and install packages from ```requirements.txt```
3. Run the script using venv: ```python3 data_scrap.py```
4. Input the username of an existing account
5. The script will show information in 3 columns:
a. Full name of the gambit with a clickable link to chess.com analyzer 
b. The number of matches in which this gambit was played by the user 
c. Average user winrate

## Example:
![](/example.png)
