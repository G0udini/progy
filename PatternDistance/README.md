## What does this script do

This script is created and used to help to count the size of arrival traffic patterns('Trombon\Veer') in civil aviation. 
It uses only basic knowledge of chart creation and statistics and should not be used at official projects.

It requires for the number of aircraft per merge point of a traffic pattern.
And gives information about the distance of active part of the pattern. 

## How to use the script:
1. Clone the script from github (git clone https://github.com/G0udini/progy.git)
2. Go to the dir where python file is located (cd PatternDistance)
3. Run the script using python or venv (python3 pat_dist.py)
4. Firstly, input the type of the pattern where t(Trombon) and v(Veer)
5. Secondly, input the number of aircraft per point like: '1 2 3 4 5 6' (up to 6)
6. Thirdly, input the distance for statistic calculations, 10 km - the standart value
7. Finally, you will recieve file in the same dir with all output info.