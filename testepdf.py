from PIL import Image
import io
from pypdf import PdfWriter, PdfReader

def write_pdf():
    img_path = r'behive_reporter\fotos\WhatsApp_Image_2024-06-16_at_20.20.43.jpeg'
    
    try:
        # Open the image using Pillow
        with Image.open(img_path) as image:
            # Convert the image to RGB (necessary for PDF conversion)
            image = image.convert('RGB')
            
            # Save the image as a PDF in a BytesIO object
            img_pdf = io.BytesIO()
            image.save(img_pdf, format="PDF")
            img_pdf.seek(0)
        
        # Read the PDF page generated from the image
        pdf_page = PdfReader(img_pdf)
        
        # Create a PDF writer object
        pdf_writer = PdfWriter()
        
        # Add the image page to the PDF
        pdf_writer.add_page(pdf_page.pages[0])
        
        # Write the final PDF to a file
        output_pdf_path = r'behive_reporter\fotos\test.pdf'
        with open(output_pdf_path, 'wb') as pdf_file:
            pdf_writer.write(pdf_file)
        
        print("PDF created successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

write_pdf()
