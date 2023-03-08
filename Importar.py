import pandas as pd
import tabula

class Importando:
    def ImportarPdf(arquivo):
        #importando o arquivo pdf para o python
        pdf = tabula.read_pdf(arquivo, pages = 'all')
        return pdf

    def ImportarTxt(arquivo):
        #importando o arquivo txt para o python
       with open(arquivo, "r", encoding = "UTF-8") as txt:
           texto = txt.readlines()
           return texto
                
    def ImportarExcel(arquivo):
        excel = pd.read_excel(arquivo)
        return excel
        
    

