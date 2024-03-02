# Healthcare_Automation

# Selenium Data Entry Automation

This project showcases a Selenium script for automating data entry in a healthcare web application. The script interacts with the application's forms, navigates through different pages, and submits data from a CSV file. Additionally, a preprocessing script is included to modify the dataset before automation.

## Project Structure

- `main.py`: The main Selenium script responsible for automating data entry.
- `preprocess.py`: A preprocessing script to modify the dataset.
- `modified_dataset.csv`: The modified dataset after preprocessing.

## Prerequisites

Before running the scripts, ensure you have the following:

- Python 3.x
- Chrome WebDriver
- Selenium, pandas

## How to Use

Run the preprocessing script to modify the dataset:

Copy code
python preprocess.py
The modified dataset will be saved as modified_dataset.csv.

Run Selenium Script:

Execute the main Selenium script to automate data entry:

Copy code
python main.py
The script will interact with the web application using the modified dataset.

Dataset Modification
The preprocessing script (preprocess.py) reads a CSV file, drops the 'NRC' column (if exists), and combines 'Date' and 'Time' columns into a datetime format.

Notes
Adjust wait times and XPaths in main.py based on the web application's structure.
