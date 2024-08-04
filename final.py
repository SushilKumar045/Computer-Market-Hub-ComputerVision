import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image

# Function to detect lines and count them
def detect_lines_and_count(edges, threshold, min_length, max_gap):
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, threshold=threshold, minLineLength=min_length, maxLineGap=max_gap)
    if lines is not None:
        filtered_endpoints = [((x1, y1), (x2, y2)) for x1, y1, x2, y2 in lines[:, 0] if np.linalg.norm([x2 - x1, y2 - y1]) > min_length]
        return filtered_endpoints
    return []

# Function to find the best parameters
def find_best_parameters(edges):
    best_threshold = 0
    best_max_gap = 0
    best_overlap_count = 0
    best_endpoints = []

    for threshold in range(70, 81, 5):
        max_gap = 0
        previous_count = -1
        while max_gap <= 100:
            endpoints = detect_lines_and_count(edges, threshold, 50, max_gap)
            overlap_count = len(endpoints)
            if overlap_count > best_overlap_count:
                best_overlap_count = overlap_count
                best_threshold = threshold
                best_max_gap = max_gap
                best_endpoints = endpoints
            if overlap_count <= previous_count + 2:  # Stop if no significant improvement
                break
            previous_count = overlap_count
            max_gap += 5

    return best_threshold, best_max_gap, best_overlap_count, best_endpoints

# Streamlit app
st.title('Sheet Stack Counter')

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the input image
    image = Image.open(uploaded_file)
    image = np.array(image)

    resize_width, resize_height = 256, 256
    image = cv.resize(image, (resize_width, resize_height))

    # Preprocess the image
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    edges = cv.Canny(blurred, 50, 150, apertureSize=3)

    # Toggle between custom and best match parameters
    use_custom_params = st.checkbox('Use Custom Parameters')

    if use_custom_params:
        # User input for custom parameters
        threshold = st.number_input('Threshold', min_value=1, max_value=200, value=80)
        min_length = st.number_input('Minimum Line Length', min_value=1, max_value=200, value=50)
        max_gap = st.number_input('Maximum Line Gap', min_value=1, max_value=200, value=50)
    else:
        threshold, min_length, max_gap = None, None, None

    use_optimal_params = st.checkbox('Use Optimal Parameters')

    if st.button('Run'):
        if use_optimal_params:
            threshold, max_gap, overlap_count, endpoints = find_best_parameters(edges)
            min_length = 50  # As per best match search
        elif use_custom_params:
            endpoints = detect_lines_and_count(edges, threshold, min_length, max_gap)
            overlap_count = len(endpoints)
        else:
            st.warning('Please select a parameter option to proceed.')
            st.stop()

        # Create a copy of the edge image to draw lines
        lines_image = np.zeros_like(edges)

        # Draw the final detected lines on the lines_image
        for (x1, y1), (x2, y2) in endpoints:
            cv.line(lines_image, (x1, y1), (x2, y2), (255, 255, 255), 1)

        # Concatenate the original image, edge-detected image, and lines image
        con = np.concatenate((image, cv.cvtColor(edges, cv.COLOR_GRAY2BGR), cv.cvtColor(lines_image, cv.COLOR_GRAY2BGR)), axis=1)

        # Convert the concatenated image to PIL format for display
        con_image = Image.fromarray(con)

        num_files = overlap_count // 2

        st.image(con_image, caption='Edge Detection and Lines', use_column_width=True)
        st.write(f'Optimal threshold: {threshold}')
        st.write(f'Optimal minLength: {min_length}')
        st.write(f'Optimal maxLineGap: {max_gap}')
        st.write(f'Number of overlapping lines detected: {overlap_count}')
        st.write(f'Number of files or records present: {num_files}')
        st.write(f'Coordinates of line endpoints: {endpoints}')
