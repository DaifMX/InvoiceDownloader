import threading

from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import *
from tkinter.messagebox import showinfo, showerror

class Selector:
    def __init__(self, window, progressBar, directories):
        self.window = window
        self.progressBar = progressBar
        self.directories = directories
        
    def select_txt(self):
        filetypes = ("Text", "*.txt"), ("All files", "*.*")
        txt_dir = askopenfilename(title="Seleccionar nombres de facturas", initialdir="/", filetypes=filetypes)
        self.directories["txt"] = txt_dir

        progress = threading.Thread(self.progressBar.progress_bar(True))
        progress.start()

        if txt_dir:
            self.progressBar.progress_bar(False)
            showinfo(title="Archivo seleccionado", message="Archivo seleccionado correctamente")

        else:
            self.progressBar.progress_bar(False)
            showerror(title="Error", message="Error seleccionando el archivo de texto.")
    
    #Select .pdf file
    def select_pdf(self):
        filetypes = ("PDF", "*.pdf"), ("All files", "*.*")
        pdf_dir = askopenfilename(title="Seleccionar PDF", initialdir="/", filetypes=filetypes)
        self.directories["pdf"] = pdf_dir

        progress = threading.Thread(self.progressBar.progress_bar(True))
        progress.start()

        if pdf_dir:
            self.progressBar.progress_bar(False)
            showinfo(title="PDF seleccionado", message="PDF seleccionado correctamente")

        else:
            self.progressBar.progress_bar(False)
            showerror(title="Error", message="Error seleccionando el archivo PDF")

    #Select saving path
    def select_path(self):
        path = askdirectory(title="Guardar en", initialdir="/")
        self.directories["path"] = path

        progress = threading.Thread(self.progressBar.progress_bar(True))
        progress.start()

        if path:
            self.progressBar.progress_bar(False)
            showinfo(title="Selected Path", message="Directorio guardado correctamente")
    
        else:
            self.progressBar.progress_bar(False)
            showerror(title="Error", message="Error seleccionando ruta")