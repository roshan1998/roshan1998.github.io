from pathlib import Path
from pypdf import PdfReader

pdf = Path(r'C:\Users\roshan.patro\Downloads\Roshan-Kumar-Patro-Resume (1).pdf')
print('exists:', pdf.exists())
if pdf.exists():
    reader = PdfReader(str(pdf))
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ''
        print(f'--- PAGE {i} ---')
        print(text)
