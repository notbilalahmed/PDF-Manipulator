import PyPDF2
import tkinter as tk
from tkinter import filedialog, simpledialog

def combiner(pdf_files, output_filename):
    merger = PyPDF2.PdfMerger()
    
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    
    merger.write(output_filename)
    merger.close()

def deleter(input_filename, output_filename, page_number):
    with open(input_filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_index in range(len(pdf_reader.pages)):
            if page_index + 1 != page_number:  # Skip the page to delete
                page = pdf_reader.pages[page_index]
                pdf_writer.add_page(page)

        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

def extractor(input_filename, output_filename, page_number):
    with open(input_filename, 'rb') as file: 
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()
        
    page = pdf_reader.pages[page_number]
    pdf_writer.addPage(page)
    with open(output_filename, 'wb') as output_file: 
        pdf_writer.write(output_file)

class PDFApp:

    def __init__(self, master):
        self.master = master
        master.title("PDF Manipulation Tool By Bilal")

        self.pdf1_label = tk.Label(master, text="PDF 1:")
        self.pdf1_label.grid(row=0, column=0, padx=10, pady=10)

        self.pdf1_entry = tk.Entry(master, width=50, state='disabled')
        self.pdf1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.pdf1_button = tk.Button(master, text="Browse", command=self.load_pdf1)
        self.pdf1_button.grid(row=0, column=2, padx=10, pady=10)

        self.pdf2_label = tk.Label(master, text="PDF 2:")
        self.pdf2_label.grid(row=1, column=0, padx=10, pady=10)

        self.pdf2_entry = tk.Entry(master, width=50, state='disabled')
        self.pdf2_entry.grid(row=1, column=1, padx=10, pady=10)

        self.pdf2_button = tk.Button(master, text="Browse", command=self.load_pdf2)
        self.pdf2_button.grid(row=1, column=2, padx=10, pady=10)

        self.combine_button = tk.Button(master, text="Combine PDFs", command=self.combiner)
        self.combine_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.delete_button = tk.Button(master, text="Delete Page", command=self.deleter_dialog)
        self.delete_button.grid(row=3, column=0, columnspan=3, pady=10)

    def load_pdf1(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.pdf1_entry.config(state='normal')
        self.pdf1_entry.delete(0, tk.END)
        self.pdf1_entry.insert(0, file_path)
        self.pdf1_entry.config(state='disabled')

    def load_pdf2(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.pdf2_entry.config(state='normal')
        self.pdf2_entry.delete(0, tk.END)
        self.pdf2_entry.insert(0, file_path)
        self.pdf2_entry.config(state='disabled')

    def combiner(self):
        pdf1 = self.pdf1_entry.get()
        pdf2 = self.pdf2_entry.get()

        if pdf1 and pdf2:
            combined_output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            combiner([pdf1, pdf2], combined_output)
            tk.messagebox.showinfo("Success", "PDFs combined successfully!")

    def deleter_dialog(self):
        pdf_file = self.pdf1_entry.get()

        if pdf_file:
            page_number = simpledialog.askinteger("Delete Page", "Enter page number to delete:")

            if page_number:
                output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                deleter(pdf_file, output_file, page_number)
                tk.messagebox.showinfo("Success", "Page deleted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFApp(root)
    root.mainloop()

