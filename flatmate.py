import webbrowser
# for webbrowser to work.

from fpdf import FPDF
class Bill:
    """

    Object that contains data about a bill, such as
    total amount and period of bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    create a flatmate person who lives in the flat and pays
    a share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay





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



# this is the command line interface where the user interact with the program (CLI).
user_amount = float(input("Hey user this enter the bill amount: "))
#float because the user input will not be in string
print("This is the amount", user_amount)

user_period =input("What is the bill period ? E.g April 2023: ")
print("This is the bill period", user_period)

#CLI for first flatmate
name_1 = input("What is your name?: ")
print("This is flatmate1 name", name_1)
daysIn_house1 = int(input(f"How many days did {name_1} stayed in the house during the bill period?"))
#int because the user input will be in int
# when you use a place holder like this {}, you need to put f in front of the string which will fetch
#the user's input.

#CLI for second flatmate
name_2 = input("What is the other flatmate name?: ")
print("This flatmate2 name", name_2)
daysIn_house2 = int(input(f"How many days did {name_2} stayed in the house during the bill period?"))
#int because the user input will be in int
# when you use a place holder like this {}, you need to put f in front of the string which will fetch
#the user's input.


#object instances, initializing objects.
the_bill = Bill(amount=user_amount, period=user_period)
flatmate1 = Flatmate(name=name_1, days_in_house=daysIn_house1)
flatmate2 = Flatmate(name=name_2, days_in_house=daysIn_house2)

#this part is not needed when using the commmand line interface, this is just to print to the console.
print(f"{name_1} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{name_2} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

#PdfReport instances, initializing PdfReport objects.
pdf_report = PdfReport(filename="flatmatebill.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)