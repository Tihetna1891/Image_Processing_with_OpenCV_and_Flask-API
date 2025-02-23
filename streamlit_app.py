import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Image Processing with Streamlit and OpenCV")
st.write("Upload an image and apply grayscale conversion and edge detection.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Display the original image
    st.image(image, channels="BGR", caption="Original Image", use_column_width=True)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    st.image(gray, caption="Grayscale Image", use_column_width=True)

    # Detect edges
    edges = cv2.Canny(gray, 100, 200)
    st.image(edges, caption="Edge Detection", use_column_width=True)