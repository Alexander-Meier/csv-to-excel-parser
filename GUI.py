import tkinter.filedialog
import tkinter as tk
import FileReader as fr
import ExcelFileFabric as eff

class GUI():
    _root = tk.Tk()
    _title = ''
    _csvFileNameEntry = tk.Entry(_root)
    _excelFileEntry = tk.Entry(_root)

    def __init__(self, title):
        self.createWindow()
        self._root.geometry("800x600")
        self._root.title(title)
        self._root.mainloop()
        
    
    def createWindow(self):
        self._lbl = tk.Label(self._root, text="CSV Parser by Alexander Meier")
        self._lbl.pack()
        self._csvFileBtn = tk.Button(self._root,text="select CSV file", command = self.openCsvFileDialog)
        self._csvFileBtn.pack()
        self._csvFileNameEntry.pack()
        self._excelFileBtn = tk.Button(self._root, text="choose output directory", command=self.openSaveExcelFileDialog)
        self._excelFileBtn.pack()
        self._excelFileEntry.pack()
        self._saveBtn = tk.Button(self._root, text="save file", command=self.saveExcelFile)
        self._saveBtn.pack()

    
    def openCsvFileDialog(self):
        self._csvFileNameEntry.config(state="normal")
        self._csvFilePicker = tk.filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv"),
                                                       ("all files",
                                                        "*.*")))
        self._csvFileNameEntry.delete(0, tk.END)
        self._csvFileNameEntry.insert(tk.END, self._csvFilePicker)
        self._csvFileNameEntry.config(state="readonly")
    
    def openSaveExcelFileDialog(self):
        self._excelFileEntry.config(state="normal")
        self._excelFilePicker = tk.filedialog.asksaveasfile(mode='a', defaultextension=".xlsx")
        if self._excelFilePicker is None:
            return
        self._excelFileEntry.delete(0,tk.END)
        self._excelFileEntry.insert(0,self._excelFilePicker.name)
        self._excelFilePicker.close()

    def saveExcelFile(self):
        self._fileReader = fr.FileReader(self._csvFileNameEntry.get(), ";")
        _headers, _lines = self._fileReader.readFile()
        print(_headers)
        print(_lines)
        self._excelFileFabric = eff.ExcelFileFabric(self._excelFileEntry.get())
        self._excelFileFabric.writeValues(_headers,_lines)
        del self._excelFileFabric
        del self._fileReader