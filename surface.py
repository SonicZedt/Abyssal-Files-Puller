from abyss import Pull_From_Abyss
from tkinter import Tk, filedialog

Tk().withdraw()
abyssal_dir = filedialog.askdirectory(title='Select Source Folder')

Pull_From_Abyss(abyssal_dir)

input("\nPress Enter to exit")
exit()