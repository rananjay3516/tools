import PyPDF2, os

os.chdir('C:\\Users\\ranan\\main\\code\\Py')

pdf1File = open('meeting1.pdf', 'rb')
pdf2File = open('meeting2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)


for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

output = open('minutes.pdf', 'wb')
writer.write(output)
output.close()
pdf1File.close()
pdf1File.close()
