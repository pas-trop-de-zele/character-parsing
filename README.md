# character-parsing

## Setup instruction

1. Ensure python is installed

Open Command Prompt (press Win + R, type cmd, and press Enter).

`python --version`

If Python is installed, you should see something like:

`Python 3.8.5`

If Python is not installed, you will get an error message indicating that Python is not recognized or installed.

2. Ensure Pandas is installed

`python -m pip show pandas`

If Pandas is installed you will see output similar to
```
Name: pandas
Version: 1.3.2
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: The Pandas Development Team
License: BSD
Location: /path/to/python/site-packages
Requires: numpy, python-dateutil, pytz
```
If Pandas is not installed, you will see a message like:

`WARNING: Package(s) not found: pandas`

## Run instruction

`python main.py`

You need to provide certain information (case sensitive)
```
# Example run
What is the last account column? traicay8 
How many characters per account? 5
What is the excel file name? input.xlsx
What is the sheet name? Sheet1
How many character do we assign per group? 5
Enter valid tasks separated by spaces: I II III IV V
How many valid pairs are there? 2      
Enter pair 1: II III
Enter pair 2: I IV
```

Sample outpupt

```
TASK III-1: traicay1-2 traicay4-2 sintoons1-2 sintoons2-5 sintoons6-2 
TASK III-2: traicay1-4 sintoons1-5 grocery3-3 sintoons5-5 traicay4-4 
TASK III-3: traicay7-3 traicay3-3 sintoons4-5 traicay1-3 grocery1-2 
TASK I-1: sintoons3-4 sintoons2-2 traicay-4 traicay3-4 sintoons6-5 
TASK I-2: grocery5-3 sintoons4-2 sintoons5-2 grocery2-2 sintoons7-2 
TASK IV-1: sintoons6-6 sintoons2-4 sintoons8-2 traicay2-2 traicay8-2 
TASK IV-2: sintoons6-3 traicay6-2 sintoons5-6 traicay5-3 sintoons3-2 
TASK IV-3: sintoons4-6 grocery6-3 traicay4-3 sintoons6-4 traicay7-2 
TASK II-1: sintoons3-3 sintoons1-6 traicay3-2 grocery5-2 traicay1-5 
TASK II-2: sintoons3-6 traicay5-4 traicay-3 traicay2-4 sintoons2-6 
TASK II-3: sintoons9-2 grocery4-2 sintoons1-3 traicay8-3 sintoons5-4 
TASK V-1: sintoons4-4 traicay2-5 grocery6-2 grocery2-3 sintoons3-5 
TASK V-2: sintoons4-3 sintoons5-3 sintoons1-4 grocery3-2 traicay2-3 
TASK ('I', 'IV')-1: traicay6-3 grocery4-3 grocery1-3 sintoons2-3 traicay5-2 

WARNING: these players could not be processed:
traicay-2 | Task V
```