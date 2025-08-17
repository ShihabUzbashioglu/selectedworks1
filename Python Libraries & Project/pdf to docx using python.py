
from pdf2docx import converter

pdf_file = 'clcoding.pdf'
docx_file = 'clcoding.docx'


cv = converter(pdf_file)
cv.convert(docx_file)
cv.close