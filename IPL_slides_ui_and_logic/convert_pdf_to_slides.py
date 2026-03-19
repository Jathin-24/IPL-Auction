import fitz  # PyMuPDF
import os

pdf_path = "IPL AUCTION KITS.pdf"
output_dir = "slides"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Opening {pdf_path}...")
doc = fitz.open(os.path.join(os.path.dirname(__file__), pdf_path))

for i in range(len(doc)):
    page = doc.load_page(i)
    # Increase zoom for better quality (2.0 = 200%)
    zoom = 2.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    
    image_path = os.path.join(os.path.dirname(__file__), output_dir, f"slide_{i+1}.jpg")
    pix.save(image_path)
    print(f"Saved {image_path}")

doc.close()
print("Done extracting all slides.")
