import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('CombinedReport.xlsx')

# Loop through all worksheets in the workbook
for worksheet in workbook.worksheets:
    # Change the width of column B to 20
    worksheet.column_dimensions['A'].width = 24
    worksheet.column_dimensions['B'].width = 15
    worksheet.column_dimensions['C'].width = 15
    worksheet.column_dimensions['D'].width = 15

# Save the changes to the workbook
workbook.save('CombinedReport.xlsx')
