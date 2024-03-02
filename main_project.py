import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time

# Read data from CSV file
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')  # Assuming tab-separated values
        for row in reader:
            data.append(row)
    return data

# Selenium script
def submit_form_and_interact(data):
    # Set up Selenium WebDriver (make sure you have the appropriate WebDriver installed and in your PATH)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)
    driver.get("https://carepro-training.ihmafrica.com")
    driver.maximize_window()

    # Step 1: Input username and password and submit
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Your Username']")))
    username_input.send_keys('tester')
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Your Password']")))
    password_input.send_keys('tester2023!')
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    # Step 2: Select Province, District, Facility and clicking Enter
    dropdown_province = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@placeholder='Enter Province']")))
    dp = Select(dropdown_province)
    dp.select_by_value('1')
    time.sleep(2)
    dropdown_district = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@placeholder='Enter District']")))
    dd = Select(dropdown_district)
    dd.select_by_value('5')
    time.sleep(2)
    facility = driver.find_element(By.XPATH, "//input[@placeholder='Search facility']")
    facility.click()
    time.sleep(2)
    facility1 = driver.find_element(By.XPATH, "//div[normalize-space()='Dr. Watson Dental Clinic']")
    facility1.click()
    time.sleep(2)
    enter_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Enter']")))
    enter_button.click()
    time.sleep(2)

    # Step 3: Navigate to NRC and attend to patient and Click "Attend to Patient" button
    # Input NRC number and click submit
    nrc_input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search by NRC']")))
    nrc_input_field.click()
    nrc_input_field.send_keys("111111/11/1")
    submit_nrc_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_nrc_button.click()
    time.sleep(2)
    attend_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Attend to Patient']")))
    attend_button.click()
    time.sleep(2)

    # Step 4: Navigate to Vitals and click "Add Vital" button
    vitals_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/vitals')]")))
    vitals_link.click()
    time.sleep(5)

    # Iterate through the test data and submit the form
    for entry in data:
        print(entry)
        # Add code to click "Add Vital" button for each entry
        add_vital_button = driver.find_element(By.XPATH, "//button[normalize-space()='Add Vital']")
        add_vital_button.click()
        time.sleep(5)

        # Assuming the form fields have IDs corresponding to the CSV columns
        date_field = driver.find_element(By.XPATH, "//input[@placeholder='dd-mm-yyyy']")
        time_field = driver.find_element(By.XPATH, "//input[@placeholder='hh:mm:ss']")
        weight_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Weight (kg)']")
        height_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Length (cm)']")
        temperature_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Temperature (c)']")
        systolic_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Systolic (mmHg)']")
        diastolic_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Diastolic (mmHg)']")
        pulse_rate_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Pulse Rate (bpm)']")
        respiratory_rate_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Respiratory Rate (bpm)']")
        oxygen_saturation_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Oxygen Saturation (%)']")

        # Input data into the form
        date_field.send_keys(entry['Date'])
        time_field.send_keys(entry['Time'])
        weight_field.send_keys(entry['Weight'])
        height_field.send_keys(entry['Height'])
        temperature_field.send_keys(entry['Temperature'])
        systolic_field.send_keys(entry['Systolic'])
        diastolic_field.send_keys(entry['Diastolic'])
        pulse_rate_field.send_keys(entry['Pulse Rate'])
        respiratory_rate_field.send_keys(entry['Respiratory Rate'])
        oxygen_saturation_field.send_keys(entry['Oxygen Saturation'])

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Wait for the next page to load (adjust wait time as needed)
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

    # Close the browser window
    driver.quit()

if __name__ == "__main__":
    # Specify the path to your CSV file
    csv_file_path = "modified_dataset.csv"

    # Read data from CSV file
    test_data = read_csv(csv_file_path)

    try:
        # Perform actions with the combined script
        submit_form_and_interact(test_data)

    except Exception as e:
        print(f"An error occurred: {e}")