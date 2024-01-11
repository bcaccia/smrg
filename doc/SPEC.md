# Goal

The goal is to create a local CLI utility that can take multiple CSV and Excel files as input and:

- Merge XLS and CSV files to a desired target format
- Merge and de duplicate XLS and CSV files to a desired target format
- Only output the duplicates of a set of XLS and CSV files to a desired target format


# Flags

-x --xls
-d --directory provide a directory of files to merge
--dedupe remove duplicate rows from output file
--dupes create a new file containing only the duplicate rows
-o --output-file output filename
