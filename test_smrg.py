from smrg import get_file_extension, is_a_file, load_files_from_dir, merge_files

CSV_FILES = ['test_files/part1.csv', 'test_files/part2.csv', 'test_files/part3.csv']
XLSX_FILES = ['test_files/part1.xlsx', 'test_files/part2.xlsx']

def test_get_file_extension():
        result = get_file_extension('test.csv')
        assert result == '.csv'
        
def test_is_a_file_file():
        result = is_a_file(['smrg.py'])
        assert result == True
        
def test_is_a_file_directory():
        result = is_a_file(['doc/'])
        assert result == False
        
def test_load_files_from_dir_csv():
        result = load_files_from_dir('test_files', False)
        assert result == CSV_FILES
        
def test_load_files_from_dir_xls():
        result = load_files_from_dir('test_files/', True)
        assert result == XLSX_FILES