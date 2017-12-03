import PyPDF2
import docx


pdfFileobj = open('sample.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileobj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

doc = docx.Document()

doc.add_paragraph(pageObj.extractText())

doc.save('Default.docx')

pdfFileobj.close()
