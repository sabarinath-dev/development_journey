#pip install reportlab


# Import the canvas class from reportlab to create a PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Our list of dictionaries (each one is an item in the bill)
items = [
    {'name': 'tea', 'qty': 2, 'total': 24},
    {'name': 'coffee', 'qty': 1, 'total': 20},
    {'name': 'limejuice', 'qty': 1, 'total': 20}
]

# Create a PDF file name
pdf_file = "bill.pdf"

# Create a canvas object (like a blank page to draw on)
# 'letter' gives the page size (8.5 x 11 inches)
c = canvas.Canvas(pdf_file, pagesize=letter)

# -------------------- TITLE --------------------
# Set font: Helvetica-Bold, size 16
c.setFont("Helvetica-Bold", 16)

# Draw the title text at (x=230, y=750) position
# (0,0) starts from bottom-left of the page
c.drawString(230, 750, "Cafe Bill")

# -------------------- TABLE HEADER --------------------
# Set bold font for the table header
c.setFont("Helvetica-Bold", 12)

# Draw column names
c.drawString(100, 710, "Item")   # First column
c.drawString(250, 710, "Qty")    # Second column
c.drawString(350, 710, "Total")  # Third column

# Draw a horizontal line under the header
c.line(90, 705, 450, 705)

# -------------------- TABLE DATA --------------------
# Use normal font for table rows
c.setFont("Helvetica", 12)

# Starting y position for the first row
y = 685

# Variable to store the total amount
grand_total = 0

# Loop through each item in the list
for item in items:
    # Draw item name (capitalize first letter)
    c.drawString(100, y, item['name'].capitalize())
    
    # Draw quantity
    c.drawString(260, y, str(item['qty']))
    
    # Draw total price
    c.drawString(360, y, str(item['total']))
    
    # Add total to grand total
    grand_total += item['total']
    
    # Move to the next line (reduce y position)
    y -= 20

# -------------------- TOTAL SECTION --------------------
# Draw a line below the last item
c.line(90, y-5, 450, y-5)

# Set bold font for total text
c.setFont("Helvetica-Bold", 12)

# Draw the text “Grand Total” label
c.drawString(250, y-25, "Grand Total:")

# Draw the total amount next to it
c.drawString(360, y-25, str(grand_total))

# -------------------- SAVE THE PDF --------------------
# Save (finalize) the PDF file
c.save()

# Print a success message in console
print(f"✅ PDF '{pdf_file}' generated successfully!")
