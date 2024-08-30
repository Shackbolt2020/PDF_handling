import PyPDF2

main_file = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark_file = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(main_file.pages)):
    page = main_file.pages[i]
    page.merge_page(watermark_file.pages[0])
    output.add_page(page)

with open('watermarked.pdf', 'wb') as file:
    output.write(file)