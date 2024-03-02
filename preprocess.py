import pandas as pd

# Read the CSV file
df = pd.read_csv('F:\Sample Dataset.csv')

# Print the column names to check their correctness
print("Column Names:", df.columns)

# Drop the 'NRC' column if it exists
if 'NRC' in df.columns:
    df = df.drop(columns=['NRC'])
    print("'NRC' column dropped.")
else:
    print("'NRC' column not found in the DataFrame.")

# Check for the existence of 'Date' column (case-insensitive)
date_column = next((col for col in df.columns if col.lower() == 'date'), None)

if date_column:
    # Combine 'Date' and 'Time', and convert to datetime
    datetime_column = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors='coerce')

    # Remove timestamp "12:00:00 AM" and keep only the date
    df[date_column] = datetime_column.dt.strftime('%d-%m-%Y')

    # Keep the 'Time' column
    df['Time'] = datetime_column.dt.strftime('%H:%M:%S')

    # Save the modified DataFrame to a new CSV file without any additional formatting
    df.to_csv('modified_dataset.csv', index=False, sep=',')
    print("Modified dataset saved to 'modified_dataset.csv'.")
else:
    print("'Date' column not found in the DataFrame.")