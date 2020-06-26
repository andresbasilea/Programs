import PyPDF2
import os


print("Ingrese la dirección completa de donde se encuentran los pdfs que desea unir"
	  "los archivos dentro de la carpeta ser[a]n ordenados usando .sort() antes de juntarlos")
print("Ejemplo: C:/Users/andre/Desktop/carpetaPDFs")

carpeta = input("-> ")

pdfFinal = []

for archivo in os.listdir(carpeta):
	if archivo.endswith('.pdf'):
		pdfFinal.append(archivo)

pdfFinal.sort()

escritor = PyPDF2.PdfFileWriter()

for archivo in pdfFinal:
	obj = open(carpeta + "/" + archivo, 'rb')
	lector = PyPDF2.PdfFileReader(obj)
	for numPagina in range(0, lector.numPages):
		pgo = lector.getPage(numPagina)
		escritor.addPage(pgo)

archivoFinal = open(carpeta + "/" + 'PDF_RESULTANTE.pdf','wb')
escritor.write(archivoFinal)
archivoFinal.close()

print("Se guard[o] el resultado con el nombre PDF_RESULTANTE en la misma carpeta en"
	  "donde se estaba trabajando")