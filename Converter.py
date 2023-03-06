import tabula
from Importar import Importando

class Convertendo():
    
    def ConvertePdf():
        #convertendo o arquivo pdf em csv
        tabula.convert_into(arquivo, 'pdf.csv', output_format = 'csv', pages = 'all')
    def ConverterTxt():
        texto.to_csv('dadosCsv/texto.csv')
    def ConverterExcel():
        excel.to_csv('dadosCsv/excel.csv')
  
