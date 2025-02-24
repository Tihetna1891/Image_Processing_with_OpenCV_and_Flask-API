# import streamlit as st
# import cv2
# import numpy as np
# from PIL import Image

# st.title("Image Processing with Streamlit and OpenCV")
# st.write("Upload an image and apply grayscale conversion and edge detection.")

# # Upload image
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Read the image
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     image = cv2.imdecode(file_bytes, 1)

#     # Display the original image
#     st.image(image, channels="BGR", caption="Original Image", use_container_width=True)

#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     st.image(gray, caption="Grayscale Image", use_container_width=True)

#     # Detect edges
#     edges = cv2.Canny(gray, 100, 200)
#     st.image(edges, caption="Edge Detection", use_container_width=True)
import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("PixelForge - Real-Time Image Processesor")
st.write("Upload an image and apply various image processing techniques.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Display the original image
    st.image(image, channels="BGR", caption="Original Image", use_container_width=True)

    # Sidebar for image processing options
    st.sidebar.header("Image Processing Options")
    process_options = st.sidebar.multiselect(
        "Select processing techniques:",
        ["Grayscale", "Edge Detection", "Blurring", "Thresholding", "Resize"]
    )

    # Apply selected processing techniques
    if "Grayscale" in process_options:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        st.image(gray, caption="Grayscale Image", use_container_width=True)

    if "Edge Detection" in process_options:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        st.image(edges, caption="Edge Detection", use_container_width=True)

    if "Blurring" in process_options:
        blur_amount = st.sidebar.slider("Blur Amount", 1, 25, 5)
        blurred = cv2.GaussianBlur(image, (blur_amount, blur_amount), 0)
        st.image(blurred, channels="BGR", caption=f"Blurred Image (Kernel Size: {blur_amount})", use_container_width=True)

    if "Thresholding" in process_options:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        threshold_value = st.sidebar.slider("Threshold Value", 0, 255, 127)
        _, thresholded = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
        st.image(thresholded, caption=f"Thresholded Image (Threshold: {threshold_value})", use_container_width=True)

    if "Resize" in process_options:
        resize_width = st.sidebar.slider("Resize Width", 50, 1000, 300)
        aspect_ratio = image.shape[1] / image.shape[0]  # Maintain aspect ratio
        resize_height = int(resize_width / aspect_ratio)
        resized = cv2.resize(image, (resize_width, resize_height))
        st.image(resized, channels="BGR", caption=f"Resized Image ({resize_width}x{resize_height})", use_container_width=True)