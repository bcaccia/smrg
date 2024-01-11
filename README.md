# Description

A command line utility to merge multiple CSV or Excel files together.

# Usage

To install locally on your machine clone the repo and then run the following on the directory (this is not packaged for PyPI yet):

`pip install smrg/`

To uninstall run:

`pip uninstall smrg`

Merge together two CSV files into a single `Merged.csv` file:

`smrg file1.csv file2.csv`

Provide a directory and merge all CSV files contained within it into a single `Merged.csv` file:

`smrg bunchoCSV/`

Provide a directory and merge all XLS/XLSX files contained within it into a single `Merged.csv` file:

`smrg bunchoXLS/ -x`

Same as above but change the name of the output file:

`smrg file1.csv file2.csv -o report_data.csv`

Merge together two Excel files into a single `Merged.xlsx` file:

`smrg file1.xlsx file2.xlsx -x`

Merge two files and remove all duplicate rows from the combined file:

`smrg file1.csv file2.csv --dedupe`

Merge two files and only output the duplicate rows to the combined file:

`smrg file1.csv file2.csv --dupes`