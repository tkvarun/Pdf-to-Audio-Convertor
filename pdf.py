import streamlit as st
from tkinter import filedialog
from tkinter import messagebox
import pyttsx3
import PyPDF2

# Function to extract text from PDF
def extract_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

# Function to convert text to audio
def text_to_audio(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()

# Function to handle file selection
def select_pdf_file():
    file_path = st.file_uploader("Select a PDF file", type="pdf")
    if file_path:
        pdf_text = extract_text(file_path)
        output_path = file_path.name.replace(".pdf", ".mp3")
        text_to_audio(pdf_text, output_path)
        st.success("PDF has been converted to audio successfully!")
        st.audio(output_path)

# Streamlit UI
st.title("PDF to Audio Translator")
select_pdf_file()
