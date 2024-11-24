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
How many character per account? 5
What is sheet name? Sheet1
What is file name? input.xlsx
What is the max character per group? 5
```

Sample outpupt

```
TASK III-1: traicay1-3 traicay4-4 sintoons1-2 traicay7-3 sintoons6-2 
TASK III-2: traicay1-2 sintoons2-5 sintoons4-5 sintoons5-5 grocery1-2 
TASK III-3: traicay4-2 sintoons1-5 grocery3-3 traicay3-3 traicay1-4 
TASK I-1: sintoons7-2 sintoons4-2 grocery1-3 sintoons2-2 sintoons6-5 
TASK I-2: sintoons3-4 sintoons5-2 traicay3-4 grocery4-3 traicay-4 
TASK I-3: traicay5-2 traicay6-3 grocery5-3 grocery2-2 
TASK IV-1: sintoons6-6 sintoons2-4 sintoons5-6 traicay4-3 traicay2-2 
TASK IV-2: sintoons6-4 traicay6-2 grocery6-3 traicay7-2 sintoons8-2 
TASK IV-3: traicay8-2 traicay5-3 sintoons4-6 sintoons2-3 sintoons6-3 
TASK IV-4: sintoons3-2 
TASK II-1: sintoons1-3 sintoons3-6 traicay-3 grocery5-2 traicay8-3 
TASK II-2: traicay3-2 traicay5-4 traicay1-5 sintoons1-6 traicay2-4 
TASK II-3: sintoons5-4 sintoons3-3 grocery4-2 sintoons9-2 sintoons2-6 
TASK V-1: traicay2-5 sintoons4-4 traicay-2 sintoons1-4 sintoons3-5 
TASK V-2: grocery3-2 grocery6-2 grocery2-3 sintoons4-3 traicay2-3 
TASK V-3: sintoons5-3 
```