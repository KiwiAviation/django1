import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Sheet():
    '''class used to access and edit Google Sheets'''
 
    def __init__(self, open: str):
            # vars for access
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("qm/client_secret.json", scope)
        client = gspread.authorize(creds)
        # sheet to access
        self.sheet = client.open(open).sheet1
 
    # helper function that allows col inputs to be name of col and row inputs to be ids (get_cell('ta1', 'condition')) 
    def col_index(self, col):
        '''converts input col name to a num'''
        for i, val in enumerate(self.sheet.row_values(1)):
            if val == col:
                return i + 1
        try:
            return int(col)
        except ValueError:
            raise ValueError(f'The col \'{col}\' could not be found in the sheet')
 
    def row_index(self, row):
        '''converts input id to a num'''
        for i, val in enumerate(self.sheet.col_values(1)):
            if val == row:
                return i + 1
        try: 
            return int(row)
        except ValueError:
            raise ValueError(f'The row \'{row}\' could not be found in the sheet')
 
    # search methods
    def get_cell(self, row, col):
        '''returns the value of a cell with the given position'''
        row = self.row_index(row)
        col = self.col_index(col)
        return self.sheet.cell(row, col).value
 
    def get_row(self, row):
        '''returns a list with all values in the given row'''
        row = self.row_index(row)
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
        '''updates a cell at the given position'''
        row = self.row_index(row)
        col = self.col_index(col)
        self.sheet.update_cell(row, col, new[0])
        return
 
    def insert_row(self, new, row):
        '''inserts a new row at the position given'''
        row = self.row_index(row)
        self.sheet.insert_row(new, row)
        return
 
    def update_cell_by_val(self, value, new):
        '''finds all cells with the given search value and updates each cell with the new value'''
        cells = self.sheet.findall(value)
        for cell in cells:
            self.sheet.update_cell(cell.row, cell.col, new[0])
        return
 
    def update_row_by_val(self, value, new):
        '''finds the row with the given search value and inserts a new row at the position given'''
        cell = self.sheet.find(value)
        self.sheet.delete_rows(cell.row)
        self.sheet.insert_row(new, cell.row)
        return

    # execute function
    def execute(self, action, **kwargs):
        '''executes a method'''
        value = None
        row = None
        col = None
        new = None

        for key, val in kwargs.items():
            if key == 'value':
                value = val
            elif key == 'row':
                row = val
            elif key == 'col':
                col = val
            elif key == 'new':
                new = val

        if action == 'get_cell':
            return self.get_cell(row, col)

        elif action == 'get_row':
            return self.get_row(row)

        elif action == 'get_all':
            return self.get_all()

        elif action == 'find_cell':
            return self.find_cell(value)

        elif action == 'find_row':
            return self.find_row(value)

        elif action == 'update_cell':
            self.update_cell(row, col, new)
            return self.get_cell(row, col)

        elif action == 'insert_row':
            self.insert_row(new, row)
            return self.get_row(row)

        elif action == 'update_cell_by_val':
            self.update_cell_by_val(value, new)
            return

        elif action == 'update_row_by_val':
            self.update_row_by_val(value, new)
            return
