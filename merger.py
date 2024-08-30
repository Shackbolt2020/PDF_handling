#PDF Merger
import sys
import PyPDF2

files = sys.argv[1:]

def file_merger(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')

file_merger(files)
