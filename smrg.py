import os
import sys
import click
import pandas as pd

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(no_args_is_help=True, context_settings=CONTEXT_SETTINGS)
@click.argument('filenames', nargs=-1, type=click.Path(exists=True))
@click.option('-x', '--xls', is_flag=True, show_default=True, default=False, help="merge xls files")
@click.option('--dedupe', is_flag=True, show_default=True, default=False, help="output a file with no duplicate rows")
@click.option('--dupes', is_flag=True, show_default=True, default=False, help="output a file with only the duplicate rows")
@click.option('-o', '--output', help='file name to output to')
@click.version_option(version='1.0.0', prog_name='smrg')

def cli(filenames, xls, dedupe, dupes, output):
     
     # If a directory, load all files of the specified type from it
     if is_a_file(filenames) == False:
          filenames = load_files_from_dir(filenames[0], xls)
     
     df = merge_files(filenames, xls)
     if dedupe:
          df = drop_duplicate_rows(df)
     elif dupes:
          df = get_duplicate_rows(df)
     
     output_file(df, xls, output)
      
def get_file_extension(file_path):
     return os.path.splitext(file_path)[1]

def is_a_file(filenames):
     return os.path.exists(filenames[0]) and os.path.isfile(filenames[0])

def load_files_from_dir(directory, xls):
     if xls:
          file_extensions = ['.xls', '.xlsx']
     else:
          file_extensions = ['.csv']
          
     # Filter the files by extension
     full_path_files = [os.path.join(directory, file) for file in os.listdir(directory) if any(file.endswith(ext) for ext in file_extensions)]
     return full_path_files


def merge_files(filenames, xls):
     """
     Merges together the dataframes
     """
     if xls:
          reader = pd.read_excel
     else:
          reader = pd.read_csv
          
     # merging multiple files 
     df = pd.concat(map(reader, filenames), ignore_index=True) 
     # Output columns and row count
     row_count = df.shape[0]
     columns_count = df.shape[1]
     print(f'Rows {row_count}, Columns {columns_count}')
     return df

def get_duplicate_rows(df):
     """
     Return any duplicate rows
     """
     return df[df.duplicated()]

def drop_duplicate_rows(df):
     """
     Drop any duplicate rows from the dataframe
     """
     return df.drop_duplicates(subset=None, keep='first', inplace=False)
          
def increment_filename(xls, optional_arg=None):
     if optional_arg is not None:
          default_filename = optional_arg
     else:
          if xls:
               default_filename = 'Merged.xlsx'
          else:
               default_filename = 'Merged.csv'
     # Check if the file exists
     if not os.path.exists(default_filename):
          return default_filename
     
     # Split filename and extension
     filename, file_extension = os.path.splitext(default_filename)
     counter = 1
     
     # Keep incrementing the counter until a unique filename is found
     while os.path.exists(f"{filename}_{counter}{file_extension}"):
          counter += 1
          
     return f"{filename}_{counter}{file_extension}"

def output_file(df, xls, output):
     """
     Output the dataframe to the appropriate file format
     If the filename exists already, increment it
     """
     if xls:
          writer = df.to_excel
     else:
          writer = df.to_csv
          
     if output:
          writer(increment_filename(xls, output), index=False)
     else:
          writer(increment_filename(xls), index=False)


if __name__ == '__main__':
    cli()