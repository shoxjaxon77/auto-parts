from openpyxl import Workbook

class Excel:
    def __init__(self):
        self.fayl = Workbook()
        self.jadval = self.fayl.active
     
    def add(self, *s):
        row = []
        for value in s:
            if isinstance(value, (str, int, float)):
                row.append(value)
            elif hasattr(value, '__str__'):
                row.append(str(value))
            else:
                row.append("")
        self.jadval.append(row)


    def save(self):
        file_path = 'mahsulotlar.xlsx'
        self.fayl.save(file_path)
        return file_path