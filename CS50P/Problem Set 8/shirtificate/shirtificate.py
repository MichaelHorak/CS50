from fpdf import FPDF
from fpdf import Align


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 0, txt="CS50 Shirtificate", border=0, align="C")
        self.ln(10)

    def add_image(self):
        self.image('shirtificate.png', w=90, x=Align.C)
        # self.image("shirtificate.png", align="C")

    def add_text(self, name):
        self.set_font("helvetica", "", 12)
        self.set_text_color(255, 255, 255)
        self.cell(0, -115, f"{name} took CS50", border=0, align="C")


pdf = PDF()
pdf.add_page()
pdf.add_image()
name = input("Name: ")
pdf.add_text(name)
pdf.output("shirtificate.pdf")
