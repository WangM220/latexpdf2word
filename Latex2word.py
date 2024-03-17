
# pip install pypandoc 

# pip install python-docx

"""Convert latex file to word"""
# import Converter module
import os 
import pypandoc


latex_file_path = "/latex_file.tex"
word_file_path = "/word_file.docx"

#c onvert latex to word
pypandoc.convert_file(latex_file_path, 'docx', outputfile=word_file_path)

"""Convert pdf file to word"""

# import Converter module
from pdf2docx import Converter


pdf_file_path = "/pdf_file"
word_file_path = "/word_file"

# convert pdf to word
Converter(pdf_file_path ).convert(word_file_path)





