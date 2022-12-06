# Data Converter 

This [developer tool](https://appseed.us/developer-tools/) provides simple helpers for data management - provided by [AppSeed](https://appseed.us/). 

- 👉 Free [support](https://appseed.us/support/) via Email and [Discord](https://discord.gg/fZC6hup)
- 👉 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br /> 

> Features

- CSV Files:
  - Print
  - Columns: Remove, Update
  - Add New Column with random values:
    - `timestamp`, `random_int` and `random string` (via Faker)
  - `csv_to_json` Helper
- [Support](https://appseed.us/support) via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).
 
<br />

The project is bundled with a simple `Flask` app that loads the information from `samples/data.csv` and presents the information using data tables.  

<br />

## ✨ Quick Start

- Clone the project
- Install Python modules:
  - `pip install -r requirements.txt` 
- Start the `Flask` app
  - The `http://localhost:5000/datatables/` route will display the contents of `samples/data.csv` using data tables.
- Save your CSV content using the same file
  - `samples/data.csv`
- Refresh the `http://localhost:5000/datatables/` page

At this point, you should see your data nicely paginated.        

<br />

![Data Converter - Provided by AppSeed.](https://user-images.githubusercontent.com/51070104/153058975-1947b69f-231d-48cc-afb2-8cc867b8b284.png)

<br /> 

## ✨ Complete Set UP

> Clone Sources (this repo)

```bash
$ git clone https://github.com/app-generator/devtool-data-converter.git
$ cd devtool-data-converter
```

<br />

> Install Modules using a Virtual Environment

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Or for **Windows-based Systems**

```bash
$ virtualenv env
$ .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
```

<br />

> Set up the environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

Or for **Windows-based Systems**

```bash
$ # CMD terminal
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```

<br />

> Edit `sample/data.csv` manually or using a `Python` console:

Open a new terminal, activate the `VENV` and update the `CSV` sample using provided helpers:

```
$ python
>>> 
>>> from util import *
>>> input = 'samples/data.csv'
>>> csv_print( input )
```

<br />

> Print only 2 lines

```python
>>> from util import *
>>> input = 'samples/data.csv'
>>> 
>>> csv_print( input ) # print all file
>>> 
csv_print( input, 2 )  # print header and first 2 lines
... 
product_code,product_info,value,currency,type
Nike_Air,Nike Air More Uptempo,105,usd,transaction
Nike_Club,Nike Club Joggers BB,55,usd,transaction
```

<br />

> Remove a column from the the `CSV` file

```python
>>> csv_col_remove( input, 'value' ) # `vaue` is the column name
```

<br />

> Add a column to the `CSV` file

```python
>>> csv_col_add( input, 'value' ) # `vaue` is the column name   
```

<br />

--- 
Data Converter - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
