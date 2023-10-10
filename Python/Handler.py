import os
import threading

from tkinter import ttk, Toplevel
from tkinter.messagebox import showerror, showinfo
from PyPDF2 import PdfReader, PdfWriter

class Handler:
    def __init__(self, directories, progressBar):
        self.directories = directories
        self.progressBar = progressBar

    def proccess_pdf(self):
        progress = threading.Thread(self.progressBar.progress_bar(True))
        progress.start()

        try:
            pdf = PdfReader(self.directories.get("pdf"))
            acumulator = 0

            while (acumulator < len(pdf.pages)):

                pWriter = PdfWriter()
                pWriter.add_page(pdf.pages[acumulator])
                    
                namer = open(self.directories.get("txt"), "r")
                lines = namer.read().splitlines()

                f = open(os.path.join(self.directories.get("path"), f"{lines[acumulator]}.pdf".format(self.directories.get("pdf"))), "wb")
                pWriter.write(f)
                f.close()

                acumulator = acumulator + 1

            self.progressBar.progress_bar(False)
            showinfo(message="PDFs generados correctamente!")

        except Exception as e:
            self.progressBar.progress_bar(False)
            showerror(title="Error", message=f"Error: {str(e)}")