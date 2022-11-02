import streamlit as st
import numpy as np
import pytesseract 
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

st.title("Our OCR APP")
st.text("Upload a image which contains English Text")

upload_image=st.sidebar.file_uploader('choose a image input for convertion',type=["jpg","png","jpeg"])
if upload_image is not None:
    img=Image.open(upload_image)
    st.image(upload_image)
    
    if st.button("Extract Text"):
        st.write("Extracted Text")
        output_text=pytesseract.image_to_string(img)
        st.write(output_text)
    