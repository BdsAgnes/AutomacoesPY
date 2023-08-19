import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
# lista todos arquivos que estão dentro desse caminho
lista_arquivos = os.listdir(caminho)
''' dicionário de arquivos com o nome pasta e
as extensões de arquivos que irá na quela pasta '''
locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
}

for arquivo in lista_arquivos:
    
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            # verifica se a pasta existe
            if not os.path.exists(f"{caminho}/{pasta}"):
                # caso não, irá criar
                os.mkdir(f"{caminho}/{pasta}")
                # reorganizando os arquivos
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")