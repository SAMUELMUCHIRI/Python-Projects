from cProfile import label
from tkinter import*
import PyPDF2
from tkinter import filedialog
root = Tk()
root.title('Codemy.com - Read PDF!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

my_text = Text(root, height=30, width=60)
my_text.pack(pady=10)

def clear_text_box():
    my_text.delete(1.0, END)

def open_pdf():
    open_file = filedialog.askopenfilename(
        initialdir="C:/gui/",
        title="Open PDF File",
        filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")))
    if open_file:
        pdf_file = PyPDF2.PdfFileReader(open_file)
        page=pdf_file.getPage(0)
        page_stuff=page.extractText()
        
        my_text.insert(1.0,page_stuff)
    
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu =Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text_box)
file_menu.add_command(label="Exit", command=root.quit) 
root.mainloop()



