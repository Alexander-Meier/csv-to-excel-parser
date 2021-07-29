import openpyxl as pyxl

class ExcelFileFabric:
    _fileName = ''

    def __init__(self, fileName):
        self._fileName = fileName

    def writeValues(self, headers, lines):
        _wb = pyxl.Workbook()
        _headers = headers
        _lines = lines
        _ws = _wb.active
        _ws.append(_headers)
        for _ in _lines:
            _ws.append(_)
        _wb.save(filename = self._fileName)
        
