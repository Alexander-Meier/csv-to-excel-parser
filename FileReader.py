class FileReader:
    _path = ''
    _separator = ''

    def __init__(self,path,separator):
        self._path = path
        self._separator = separator

    def readFile(self):
        _headers = []
        _lines = []
        _firstLine = True
        _f = open(self._path, 'r')
        _offset = 0
        _idx = 0

        for _line in _f:
            if _firstLine:
                #add headers
                _firstLine = False
                for _c in _line:
                    if not _c == self._separator:
                        _offset += 1
                        if _offset == len(_line) - 1:
                            _header = _line[_idx:_offset + 1].rstrip("\n")
                            _header = _header.replace('"',"")
                            _headers.append(_header)
                    else:
                        _header = _line[_idx:_offset].rstrip("\n")
                        _header = _header.replace('"',"")
                        _headers.append(_header)
                        _offset += 1
                        _idx = _offset
            else:
                _offset = 0
                _idx = 0
                #add lines
                _values = []
                for _c in _line:
                    if not _c == self._separator:
                        _offset += 1
                        if _offset == len(_line) - 1:
                            _value = _line[_idx:_offset + 1].rstrip("\n")
                            _value = _value.replace('"',"")
                            _values.append(_value)
                    else:
                        _value = _line[_idx:_offset].rstrip("\n")
                        _value = _value.replace('"',"")
                        _values.append(_value)
                        _offset += 1
                        _idx = _offset
                _lines.append(_values)
                
        _f.close()
        return _headers,_lines
   

    if __name__ == "__main__":
        print("FileReader executed")