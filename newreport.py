from fpdf import FPDF
name='Frank'
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, f'Hello my name is {name}!')
pdf.output('tutorial.pdf', 'F')