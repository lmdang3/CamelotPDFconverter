# Camelot is installed on my python3 kernel
# Dependencies includes Ghostscript and Tkinter
# Documentation: https://camelot-py.readthedocs.io/en/master/user/install-deps.html#install-deps

import camelot
import pandas as pd
pdf_tables = camelot.read_pdf("C:/Users/lamda/downloads/global.pdf", pages = 'all')


pdf_tables
# empty dataframe
combined_df = pd.DataFrame()
# Iterate through each page's tables and combine them
for page_number, page_table in enumerate(pdf_tables, start=1):
    try:
        # Extract tables from the current page
        current_page_df = page_table.df

        # Append the current page's tables to the combined dataframe
        combined_df = pd.concat([combined_df, current_page_df], ignore_index=True)

    except Exception as e:
        print(f"Error processing tables on page {page_number}: {e}")
        
display(combined_df)
combined_df.to_csv("C:/Users/lamda/downloads/global.csv", index=False)