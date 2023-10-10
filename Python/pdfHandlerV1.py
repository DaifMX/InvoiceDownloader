import os
from PyPDF2 import PdfReader, PdfFileWriter

# PDF Generator
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(ROOT_DIR, "dist/invoices.pdf")

pdf = PdfReader(FILE_PATH)
acumulator = 0

while (acumulator < pdf.numPages):

    pWriter = PdfFileWriter()

    pWriter.addPage(pdf.getPage(acumulator))
    
    namer = open("dist/invoiceList.txt", "r")
    lines = namer.read().splitlines()

    f = open(os.path.join(ROOT_DIR, f"dist/Result/{lines[acumulator]}.pdf".format(FILE_PATH)), "wb")
    pWriter.write(f)
    f.close()

    acumulator = acumulator + 1

os.system("pause")