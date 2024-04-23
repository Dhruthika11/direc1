import fitz
import pandas as pd


doc_pdf1 = fitz.open('/content/pdf1.pdf')
table1_df = pd.DataFrame()

for page in range(len(doc_pdf1)):
    page = doc_pdf1.load_page(page)
    tables = page.find_tables()
    if tables:
        for rows in tables:
            table_data = rows.to_pandas()
            table1_df = pd.concat([table1_df, table_data])

csv_table1 = '/content/output_table1.csv'
table1_df.to_csv(csv_table1, index=False)

doc_pdf2 = fitz.open('/content/pdf2.pdf')
table2_df = pd.DataFrame()

for page in range(len(doc_pdf2)):
    page = doc_pdf2.load_page(page)
    tables = page.find_tables()
    if tables:
        for rows in tables:
            table_data = rows.to_pandas()
            table2_df = pd.concat([table2_df, table_data])

csv_table2 = '/content/output_table2.csv'
table2_df.to_csv(csv_table2, index=False)