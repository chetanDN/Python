import PyPDF2
import re
import xlsxwriter


workbook=xlsxwriter.Workbook("C:\\temp\\pylog.xlsx")
ws=workbook.add_worksheet("MISRA")
cell_format1= workbook.add_format({'border':True, 'font_name':'Century Gothic', 'font_size':10, 'text_wrap':True})



object = open("C:\\temp\\Release_Notes\\Misra_Voilation_Reports\\Zip\\ADC_MisraReport\\403\\Adc.c.pdf",'rb')


reader = PyPDF2.PdfFileReader(object)

pages = reader.numPages
print("no of pages present : ",pages)

DataStr=""
Flag=False
for i in range(pages):
	page = reader.getPage(i)
	pageContent = page.extractText()
	misra_start=re.search("MISRA\sRULE\s*Line\sNumbers",pageContent)
	misra_end=re.search("Justified MISRA Violations",pageContent)
	
	
	if misra_start:
		Flag = True
		
	if Flag:
		DataStr += pageContent
		
	if misra_end:
		Flag = False
		

DataStr=DataStr.split("Justified MISRA Violations")[0]
		
# print("DataStr :",DataStr)

misra=re.compile('[0-9]{2}\.[0-9]{2}')

voilation_lsit = misra.finditer(DataStr)

row=0
for i in voilation_lsit:
	row+=1
	# print(row,i.group())
	ws.write(row,0,float(i.group()),cell_format1)

workbook.close()

	
	
#page.extractText()
# pageContent = page.extractText()
#pageContent = page.getContents()

# print("pageContent :",pageContent)
