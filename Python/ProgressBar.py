from tkinter import Toplevel, ttk

class ProgressBar:
    def __init__(self, window):
        self.window = window
    
    def progress_bar(self,status:bool):
        global loading
        
        if status:
            loading = Toplevel(self.window)
            loading.geometry("250x80")
            loading.title("Loading...")
            self.window.withdraw()

            pb = ttk.Progressbar(loading, orient="horizontal", mode="indeterminate", length=225)
            pb.pack(expand=True)
            pb.start([8])

        else:
            loading.destroy()
            loading.update()
            self.window.deiconify()