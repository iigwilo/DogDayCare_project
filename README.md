# DogDayCare_project
DogDayCare_project is a python libray for calculating the amount of dog food this given dog shelter can order for the next month

## Prerequisites/assumption
- This dog food calculation is based on given estimated dog food consumption based on size over a given period
   Sizes of dogs and food needs:
    ● Small - 10lbs.
    ● Medium - 20lbs.
    ● Large - 30lbs.
 - Date, calender season, and dog shelter demand trends are not factored into this calculation
 - Dog shelter capacity of 30 dogs is not factored into this calculation
 - The calculated dog food data is not stored for analysis/trends calculations over time
 - Actual dog food consumtion data is not stored to be compared with projected dog food calcualted order

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dogFood.

```bash
pip install dogFood
```
##Usage

The following is the file structure:
- dogFood
  - test.py
  - monthlyDogFood
    __init__.py
    nextMonthDogFood.py
    
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
