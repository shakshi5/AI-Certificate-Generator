import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("AI Certificate Generator")

name = st.text_input("Enter Student Name")

course = st.text_input("Enter Course Name")

date = st.text_input("Date")


if st.button("Generate Certificate"):

    img = Image.open("certificate_template.png")

    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("Roboto-Regular.ttf", 60)
    except:
        font = ImageFont.load_default()
        
    draw.text((726,695),name,font=font,fill="black")

    draw.text((1025,809),course,font=font,fill="black")

    draw.text((594,896),date,font=font,fill="black")

    img.save("certificate.png")

    st.image(img)

    with open("certificate.png","rb") as file:
        st.download_button(
            "Download Certificate",
            file,
            file_name="certificate.png")