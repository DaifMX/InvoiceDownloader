import Selector
from Selector import Selector
from Handler import Handler
from ProgressBar import ProgressBar
from tkinter import *
from tkinter import ttk

class MainInterface:
    window = Tk()
    progressBar = ProgressBar(window)
    directories = {}

    def __init__(self):
        self.window.geometry("250x150")
        self.window.title("AutoPDF")

        selector1 = Selector(self, self.progressBar, self.directories)
        handler1 = Handler(self.directories, self.progressBar)

        open_txt_button = ttk.Button(self.window, text="Seleccionar archivo de texto", command=selector1.select_txt)
        open_txt_button.pack(expand=True)

        open_pdf_button = ttk.Button(self.window, text="Seleccionar PDF", command=selector1.select_pdf)
        open_pdf_button.pack(expand=True)

        open_dir_button = ttk.Button(self.window, text="Seleccionar destino", command=selector1.select_path)
        open_dir_button.pack(expand=True)

        start_button = ttk.Button(self.window, text="Start", command=handler1.proccess_pdf)
        start_button.pack(expand=True)

    def initialize(self):
        self.window.mainloop()