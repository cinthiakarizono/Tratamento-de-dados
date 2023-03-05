import tabula
from Importar import Importando

class Convertendo():
    
    def ConvertePdf():
        #convertendo o arquivo pdf em csv
        tabula.convert_into(url_pdf, 'pdf.csv', output_format = 'csv', pages = 'all')
    def ConverterTxt():
        pass
    def ConverterExcel():
        excel.to_csv(url_excel)
  
