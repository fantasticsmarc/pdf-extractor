# PyInstaller spec for PDF Extractor
a=Analysis(['main.py'], hiddenimports=['PyPDF2','pdfplumber','customtkinter'])
exe=EXE(a.pure,a.scripts,name='pdf-extractor',console=False)
