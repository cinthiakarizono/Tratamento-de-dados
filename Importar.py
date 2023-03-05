from urllib.request import urlretrieve
import pandas as pd
import tabula

url_excel = 'https://docs.google.com/spreadsheets/d/1HPlw9FPQ3qkHmZMziGbME7aqiPnZs08bjoFuJbN07NI/edit#gid=0'
url_pdf = 'https://www.fitabase.com/media/1930/fitabasedatadictionary102320.pdf'
url_txt = 'https://www.kaggle.com/kenmatsu4/feature-store-for-indoor-location-navigation'
#def arquivoPdf(arquivo):

    #importando o arquivo pdf para o python
    #pdf = tabula.read_pdf(url_pdf, pages = 'all')
    #convertendo o arquivo pdf em csv
    #tabula.convert_into(url_pdf, 'pdf.csv', output_format = 'csv', pages = 'all')

#importando o arquivo txt para o python
urlretrieve(url_txt, 'index.txt')
txt = pd.read_csv('index.txt', sep='/t', engine='python', lineterminator='\r\n')
txt.to_csv(txt.csv, sep='\t', index=False, header=True)

#excel = pd.read_excel(url_excel)
#excel.to_csv(url_excel)