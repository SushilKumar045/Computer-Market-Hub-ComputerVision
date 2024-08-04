# Sheet-Stack-Counter

This Streamlit application is designed to count the number of sheet stacks in a manufacturing plant using image processing techniques. The app allows users to upload an image of a sheet stack, process it to detect edges, and count the lines representing individual sheets. The application can either use custom parameters provided by the user or find the optimal parameters for line detection.



## Installation

* Install requirements with pip

```bash
  pip install streamlit opencv-python-headless numpy pillow

```

* Save the code in a Python file, e.g., final.py.

* Run the Streamlit application    

```bash
  streamlit run final.py

```

## Acknowledgments
 - [Streamlit](https://streamlit.io/)
 - [opencv](https://opencv.org/)
 - [pillow](https://pypi.org/project/pillow/)
 - [Numpy](https://numpy.org/)

## Features

- **Image Upload:** Users can upload images in JPG, JPEG, or PNG formats.
- **Image Resizing:** Uploaded images are resized to 256x256 pixels for consistent processing.
- **Edge Detection:** Converts the image to grayscale, applies Gaussian blur, and uses the Canny edge detection algorithm to identify edges.
- **Custom Parameters:** Users can toggle to use custom parameters for line detection including threshold, minimum line length, and maximum line gap.
- **Optimal Parameters:** The application can automatically find the best parameters for line detection to maximize the number of detected lines.
- **Line Detection and Counting:** Uses the Hough Line Transform to detect lines in the edge-detected image and counts the lines representing sheets.
- **Results Display:** Shows the original image, edge-detected image, and lines image side by side, along with the optimal parameters and the count of detected lines and sheets.

# Usage 

- **Upload an Image:** Click on the "Upload an image" button to upload an image of the sheet stack.
Toggle Parameter Options:
- **Use Custom Parameters:** Check this box to enter custom parameters for threshold, minimum line length, and maximum line gap.
- **Use Optimal Parameters:** Check this box to allow the application to find the optimal parameters automatically.
- **Run the Detection:** Click on the "Run" button to start the detection process.
- **View Results:** The application will display the processed images and the count of detected lines and sheets.

# Explanation of Parameters

- **Threshold Description:** 
The threshold parameter in the Hough Line Transform determines the minimum number of intersections needed in the accumulator to detect a line. Essentially, it sets the sensitivity for line detection.

- **Higher Values:** A higher threshold requires more intersections for a line to be considered valid, making the detection more stringent and resulting in fewer, more prominent lines being detected.
- **Lower Values:** A lower threshold allows for more lines to be detected, including weaker or less prominent lines, which might include noise.

```bash
  threshold = st.number_input('Threshold', min_value=1, max_value=200, value=80)
```
- **Minimum Line Length (min_length):**
The minimum line length parameter specifies the shortest length of a line segment that should be detected. Any line shorter than this length will be ignored.

- **Higher Values:** A higher minimum line length will ignore shorter lines, focusing on longer, more significant lines.
- **Lower Values:** A lower minimum line length will detect shorter lines, which can include more noise and minor features.
```bash
  min_length = st.number_input('Minimum Line Length', min_value=1, max_value=200, value=50)

```
- **Maximum Line Gap (max_gap):**
The maximum line gap parameter defines the maximum allowed gap between points on the same line to link them together. It is used to join broken line segments.

- **Higher Values:** A higher maximum line gap will connect distant line segments, potentially merging lines that are not actually connected.
- **Lower Values:** A lower maximum line gap will ensure that only closely spaced line segments are connected, preserving the separation of distinct lines.
```bash
max_gap = st.number_input('Maximum Line Gap', min_value=1, max_value=200, value=50)
```
## **Screenshots**

## **Interface**
![App Screenshot](https://github.com/SaiTeja250802/Computer-Market-Hub-1/blob/main/1.png)
![App Screenshot](https://github.com/SaiTeja250802/Computer-Market-Hub-1/blob/main/2.png)
## **Custom Parameters Setting**
- **Sample Image**
- **Result**
![App Screenshot](https://github.com/SaiTeja250802/Computer-Market-Hub-1/blob/main/3.png)
![App Screenshot](https://github.com/SaiTeja250802/Computer-Market-Hub-1/blob/main/4.png)
## **Use Optimal Parameters**
![App Screenshot](https://github.com/SaiTeja250802/Computer-Market-Hub-1/blob/main/5.png)
![App Screenshot](https://github.com/SaiTeja250802/Computer-Market-Hub-1/blob/main/6.png)
![App Screenshot](https://github.com/SaiTeja250802/Computer-Market-Hub-1/blob/main/7.png)
