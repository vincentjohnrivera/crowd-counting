import streamlit as st 
from PIL import Image
from crowdcounter import predict

st.title("LT6 Crowd Counter")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Counting...")
    plt = predict(uploaded_file)
    st.pyplot(fig=plt)

