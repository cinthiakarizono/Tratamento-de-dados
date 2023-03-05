from Importar import Importando

class Verificando(self, arquivo):
    arquivo = self.arquivo
    if ".pdf" in arquivo:
        ImportarPdf(arquivo)
    elif ".txt" in arquivo:
        ImportarTxt(arquivo)
    elif ".xlsx" in arquivo:
        ImportarExcel(arquivo)
    else:
        print("Formato inválido")