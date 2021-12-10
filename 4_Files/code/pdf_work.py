#%% Working with PDF files

#%% environment
import os
import sys
import glob

sys.path.append(r'D:\Documents\python\repo\Introduction_Python_Nov21\week4\code')
from settings import *  

# set main dir
os.chdir(main_dir + '/' + resource_dir)

#%%
# pip install PyPDF2
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileMerger

# read
anna = PdfFileReader('anna_karenina.pdf')
nPages = anna.getNumPages()        # how many pages?
page = anna.getPage(0)             # first page
page_content = page.extractText()  # take text
print(page_content) 

# slice
input_pdf = PdfFileReader('anna_karenina_long.pdf')
pdf_writer = PdfFileWriter()
for n in range(1, 4):
    page = input_pdf.getPage(n)
    pdf_writer.addPage(page)
    
with open('../' + result_dir + '/' + 'anna_2_4.pdf','wb') as output_file:
    pdf_writer.write(output_file)

   
input_pdf = PdfFileReader('khanbank.pdf')
pdf_writer = PdfFileWriter()
for n in range(1, 4):
    page = input_pdf.getPage(n)
    pdf_writer.addPage(page)
    
with open('../' + result_dir + '/' + 'khan_2_4.pdf','wb') as output_file:
    pdf_writer.write(output_file)

# merge
pdf_merger = PdfFileMerger()
pdfs = list(glob.glob("*.pdf"))

for path in pdfs:
    pdf_merger.append(str(path))

with open('../' + result_dir + '/' + 'all_pdf.pdf','wb') as output_file:
    pdf_merger.write(output_file)


# write
#pip3 install fpdf
import fpdf 

pdf = fpdf.FPDF(format='letter') #pdf format
pdf.add_page() #create new page
pdf.set_font("Arial", size=12) # font and textsize
pdf.cell(35, 4, txt="HAPPY families", ln=0, align="L") # ln=0 after,ln=1 new line, ln=2 below
pdf.cell(25, 4, txt="are all alike;", ln=0, align="L")   # L, R, C
pdf.cell(50, 4, txt="every unhappy family", ln=0, align="L")
pdf.cell(20, 4, txt="End of story.", ln=2, align="L")
pdf.output('../' + result_dir + '/' + "letter.pdf")


# pip install reportlab
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas('../' + result_dir + '/' + "font.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 12) # Set font to Times New Roman with 12-point size
canvas.setFillColor(blue) # Draw blue text one inch from the left and ten inches from the bottom
canvas.drawString(1 * inch, 10 * inch, "Blue text")
canvas.save() # Save the PDF file


# Other
# tabula-py  -- # pip install tabule-py, import tabula  - Java should be installed
# import textract
# pdfkit

# install Java
import tabula
# Read remote pdf into list of DataFrame
df2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")