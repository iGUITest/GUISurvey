import pandas as pd

# Load the Excel file
file_path = 'paper-list.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the 'Taxonomy' sheet
df = excel_data.parse('Taxonomy')

# Convert the entire dataframe into markdown format
full_markdown_table = df.to_markdown(index=False)

# Display the full markdown table
print(full_markdown_table)
