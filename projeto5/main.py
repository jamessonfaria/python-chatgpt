
# Importar o PyPDF2
from PyPDF2 import PdfMerger

# Abrir os arquivos pdf
pdf1_file = open('C:\work\pessoal\chatgpt\projetos-python\python-chatgpt\projeto5\pdf\/text1.pdf', 'rb')
pdf2_file = open('C:\work\pessoal\chatgpt\projetos-python\python-chatgpt\projeto5\pdf\/text2.pdf', 'rb')
 
# Criar PDFReader objetos
merger = PdfMerger()
merger.append(fileobj = pdf1_file) 
merger.append(fileobj = pdf2_file) 
 
# Criar o objeto de escrita de PDF
output = open('C:\work\pessoal\chatgpt\projetos-python\python-chatgpt\projeto5\pdf\/merged_output.pdf', 'wb')
merger.write(output)

