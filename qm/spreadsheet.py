import gspread
from oauth2client.service_account import ServiceAccountCredentials

class mSheet():
    '''class used to access and edit the Master_qm Google Sheet'''
    # vars for access
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    # sheet to access
    sheet = client.open('Master_qm').sheet1

    # search methods
    def get_cell(row, col):
        '''returns the value of a cell with the given position'''
        return mSheet.sheet.cell(row, col).value

    def get_row(row):
        '''returns a list with all values in the given row'''
        return mSheet.sheet.row_values(row)

    def get_all():
        '''returns list of lists with all values in the spreadsheet'''
        return mSheet.sheet.get_all_values()

    def find_cell(value):
        '''returns all cells with the given search value'''
        return mSheet.sheet.findall(value)

    def find_row(value):
        '''finds the row with the search value and returns a list of all values within the row'''
        cell = mSheet.sheet.find(value)
        return mSheet.sheet.row_values(cell.row)

    # edit methods
    def update_cell(row, col, new):
        '''updates a cell at the given position'''
        mSheet.sheet.update_cell(row, col, new)
        return

    def insert_row(new, row):
        '''inserts a new row at the position given'''
        mSheet.sheet.insert_row(new, row)
        return

    def update_cell_by_val(value, new):
        '''finds all cells with the given search value and updates each cell with the new value'''
        cells = mSheet.sheet.findall(value)
        for cell in cells:
            mSheet.sheet.update_cell(cell.row, cell.col, new)
        return

    def update_row_by_val(value, new):
        '''finds the row with the given search value and inserts a new row at the position given'''
        cell = mSheet.sheet.find(value)
        mSheet.sheet.delete_rows(cell.row)
        mSheet.sheet.insert_row(new, cell.row)
        return

class tSheet():
    '''class used to access and edit the Tent_db Google Sheet'''
    # vars for access
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    # sheet to access
    sheet = client.open('Tent_db').sheet1

    ## TODO create helper function allow col inputs to be name of col and row inputs to be ids (get_cell('ta1', 'condition)) 
    ## TODO implement try / except to catch errots

    # search methods
    def get_cell(row, col):
        '''returns the value of a cell with the given position'''
        return tSheet.sheet.cell(row, col).value
 
    def get_row(row):
        '''returns a list with all values in the given row'''
        return tSheet.sheet.row_values(row)
 
    def get_all():
        '''returns list of lists with all values in the spreadsheet'''
        return tSheet.sheet.get_all_values()
 
    def find_cell(value):
        '''returns all cells with the given search value'''
        return tSheet.sheet.findall(value)
 
    def find_row(value):
        '''finds the row with the search value and returns a list of all values within the row'''
        cell = tSheet.sheet.find(value)
        return tSheet.sheet.row_values(cell.row)
 
    # edit methods
    def update_cell(row, col, new):
        '''updates a cell at the given position'''
        tSheet.sheet.update_cell(row, col, new)
        return
 
    def insert_row(new, row):
        '''inserts a new row at the position given'''
        tSheet.sheet.insert_row(new, row)
        return
 
    def update_cell_by_val(value, new):
        '''finds all cells with the given search value and updates each cell with the new value'''
        cells = tSheet.sheet.findall(value)
        for cell in cells:
            tSheet.sheet.update_cell(cell.row, cell.col, new)
        return
 
    def update_row_by_val(value, new):
        '''finds the row with the given search value and inserts a new row at the position given'''
        cell = tSheet.sheet.find(value)
        tSheet.sheet.delete_rows(cell.row)
        tSheet.sheet.insert_row(new, cell.row)
        return
