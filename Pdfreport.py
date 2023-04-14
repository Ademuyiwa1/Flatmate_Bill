import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file tha contains data about the flatmates such as
    their names, their due amount and the period of the bill.

    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #insert image on top of the file in a png file method.
        pdf.image("house.png", w=30, h=30)

        #insert title, name of the app
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)
        #border=0 is not make the text to be inside a block, ln is for new line.

        #insert period label and value.
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40,  txt=bill.period,border=0, ln=1)

        #insert name and due amount for the first flatmate.
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill,flatmate2), 2)), border=0, ln=1)
        # its needed to pass that attribute as a string because if would be returned as a float and fpdf can't
        #inteperet a float, also the round function will round up the pay method return i.e round up the returned
        #value also 2 stands for rounding up to 2 decimal point.

        # insert name and due amount for the second flatmate.
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=100, h=25, txt=flatmate2.name,border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill, flatmate1), 2)),border=0, ln=1)

        pdf.output(self.filename)

        #webbrowser is used to view the pdf result automatically.
        webbrowser.open(self.filename)
