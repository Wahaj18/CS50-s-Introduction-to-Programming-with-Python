from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "", 48)
        self.cell(w=0, h=60, text="CS50 Shirtificate", align="C")
        self.ln(20)
        self.image("shirtificate.png", x="C", y=70, w=190)

def main():
    name = input("Name: ").title()
    shirt50(name)


def shirt50(n):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 213, f"{n} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
