# DogDayCare_project
DogDayCare_project is written in python to calculate the amount of dog food needed for next month for a dog shelter.

## Prerequisites/Assumption
- The dog food calculation is based on dog food consumption by dog size as follows;
    - Small - 10lbs.
    - Medium - 20lbs.
    - Large - 30lbs.

 - Date, calender season, and dog shelter food demand trend are not factored into the dog food calculation
 - Dog shelter maximum capacity of 30 dogs is not factored into the calculation
 - The calculated dog food data is not stored for analysis and trends over time
 - Actual dog food consumtion data is not stored to be compared with projected dog food calculated

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dogFood.

```bash
pip install dogFood
```
##Usage

Create a folder dir using your terminal
```bash
mkdir dogFood
```
In the dogFood folder create another folder 
```bash
mkdir monthlyDogFood
```
Then set up the following file structure with the attach .py files as shown below:
- dogFood(Folder)
  - test.py
  - monthlyDogFood(Folder)
    - __init__.py
    - nextMonthDogFood.py
    
To run dog food calculation for next month execute the following, while in dogFood folder
```python
python nextMonthDogFood.py
```
Note: You can open the nexMonthDogFood.py to edit the input variables.

To run the unit test for calculating dog food, run the following test file
```python
python test.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
