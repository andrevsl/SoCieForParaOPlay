import pandas as pd

def getGsheetPData(sheetName):
    if sheetName=='LBResumo':
        sheet_name = 'LBResumo' # replace with your own sheet name
        sheet_id = '1oTq6KeoAYEfu-0JIapbsMGrUFLOr1kXid5yU2y5Pn94' # replace with your sheet's ID
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        data = pd.read_csv(url)
        return data