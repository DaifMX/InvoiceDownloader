import os, threading

from PyPDF2 import PdfReader, PdfWriter

from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

#Window Properties
window = Tk()
window.geometry("250x150")
window.title("AutoPDF")

directories = {}
loading = None

def progress_bar(status:bool):
    global loading
    
    if status:
        loading = Toplevel(window)
        loading.geometry("250x80")
        loading.title("Loading...")
        window.withdraw()

        pb = ttk.Progressbar(loading, orient="horizontal", mode="indeterminate", length=225)
        pb.pack(expand=True)
        pb.start([8])

    else:
        loading.destroy()
        loading.update()
        window.deiconify()

#Select .txt file
def select_txt():
    filetypes = ("Text", "*.txt"), ("All files", "*.*")
    txt_dir = askopenfilename(title="Seleccionar nombres de facturas", initialdir="/", filetypes=filetypes)
    directories["txt"] = txt_dir

    progress = threading.Thread(progress_bar(True))
    progress.start()

    if txt_dir:
        progress_bar(False)
        showinfo(title="Archivo seleccionado", message="Archivo seleccionado correctamente")

    else:
        progress_bar(False)
        showerror(title="Error", message="Error seleccionando el archivo de texto.")
    
#Select .pdf file
def select_pdf():
    filetypes = ("PDF", "*.pdf"), ("All files", "*.*")
    pdf_dir = askopenfilename(title="Seleccionar PDF", initialdir="/", filetypes=filetypes)
    directories["pdf"] = pdf_dir

    progress = threading.Thread(progress_bar(True))
    progress.start()

    if pdf_dir:
        progress_bar(False)
        showinfo(title="PDF seleccionado", message="PDF seleccionado correctamente")

    else:
        progress_bar(False)
        showerror(title="Error", message="Error seleccionando el archivo PDF")

#Select saving path
def select_path():
    path = askdirectory(title="Guardar en", initialdir="/")
    directories["path"] = path

    progress = threading.Thread(progress_bar(True))
    progress.start()

    if path:
        progress_bar(False)
        showinfo(title="Selected Path", message="Directorio guardado correctamente")
    
    else:
        progress_bar(False)
        showerror(title="Error", message="Error seleccionando ruta")

#PDF Creation
def proccess_pdf():
    progress = threading.Thread(progress_bar(True))
    progress.start()

    try:
        pdf = PdfReader(directories.get("pdf"))
    
        acumulator = 0

        while (acumulator < len(pdf.pages)):

            pWriter = PdfWriter()
            pWriter.add_page(pdf.pages[acumulator])
            
            namer = open(directories.get("txt"), "r")
            lines = namer.read().splitlines()

            f = open(os.path.join(directories.get("path"), f"{lines[acumulator]}.pdf".format(directories.get("pdf"))), "wb")
            pWriter.write(f)
            f.close()

            acumulator = acumulator + 1

        progress_bar(False)
        showinfo(message="PDFs generados correctamente!")

    except Exception as e:
        progress_bar(False)
        showerror(title="Error", message=f"Error: {str(e)}")

open_txt_button = ttk.Button(window, text="Seleccionar archivo de texto", command=select_txt)
open_txt_button.pack(expand=True)

open_pdf_button = ttk.Button(window, text="Seleccionar PDF", command=select_pdf)
open_pdf_button.pack(expand=True)

open_dir_button = ttk.Button(window, text="Seleccionar destino", command=select_path)
open_dir_button.pack(expand=True)

start_button = ttk.Button(window, text="Start", command=proccess_pdf)
start_button.pack(expand=True)

window.mainloop()