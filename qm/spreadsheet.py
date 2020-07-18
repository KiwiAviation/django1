import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Sheet():
    '''class used to access and edit Google Sheets'''
 
    def __init__(self, open: str):
            # vars for access
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        # sheet to access
        self.sheet = client.open(open).sheet1
 
    # helper function that allows col inputs to be name of col and row inputs to be ids (get_cell('ta1', 'condition')) 
    def col_index(self, col):
        '''converts input col name to a num'''
        for i, val in enumerate(self.sheet.row_values(1)):
            if val == col:
                return i + 1
        return col
 
    def row_index(self, row):
        '''converts input id to a num'''
        for i, val in enumerate(self.sheet.col_values(1)):
            if val == row:
                return i + 1
        return row
 
    # search methods
    def get_cell(self, row, col):
        row = self.row_index(row)
        col = self.col_index(col)
        '''returns the value of a cell with the given position'''
        return self.sheet.cell(row, col).value
 
    def get_row(self, row):
        row = self.row_index(row)
        '''returns a list with all values in the given row'''
        return self.sheet.row_values(row)
 
    def get_all(self):
        '''returns list of lists with all values in the spreadsheet'''
        return self.sheet.get_all_values()
 
    def find_cell(self, value):
        '''returns all cells with the given search value'''
        return self.sheet.findall(value)
 
    def find_row(self, value):
        '''finds the row with the search value and returns a list of all values within the row'''
        cell = self.sheet.find(value)
        return self.sheet.row_values(cell.row)
 
    # edit methods
    def update_cell(self, row, col, new):
        row = self.row_index(row)
        col = self.col_index(col)
        '''updates a cell at the given position'''
        self.sheet.update_cell(row, col, new)
        return
 
    def insert_row(self, new, row):
        row = self.row_index(row)
        '''inserts a new row at the position given'''
        self.sheet.insert_row(new, row)
        return
 
    def update_cell_by_val(self, value, new):
        '''finds all cells with the given search value and updates each cell with the new value'''
        cells = self.sheet.findall(value)
        for cell in cells:
            self.sheet.update_cell(cell.row, cell.col, new)
        return
 
    def update_row_by_val(self, value, new):
        '''finds the row with the given search value and inserts a new row at the position given'''
        cell = self.sheet.find(value)
        self.sheet.delete_rows(cell.row)
        self.sheet.insert_row(new, cell.row)
        return

mSheet = Sheet('Master_qm')
tSheet = Sheet('Tent_db')