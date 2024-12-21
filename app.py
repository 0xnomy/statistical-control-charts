import streamlit as st
import os

# Title of the app
st.title("Project Dashboard - Data Analysis Reports")

# Section for project summary
st.header("Project Summary")
st.write("""
This project involves data analysis using statistical and machine learning techniques. 
It includes the following tasks:

1. **Multivariate Control Chart Analysis** - Monitors process stability using multivariate methods.
2. **Scatter Plot Analysis** - Visualizes relationships between variables.
3. **Feature Importance (Random Forest)** - Identifies important features in datasets using Random Forest models.
4. **PCA (Principal Component Analysis)** - Reduces dimensionality while retaining essential information.
5. **Cumulative Sum (CUSUM)** - Tracks process shifts over time.
6. **Shewhart Control Charts** - Evaluates process variations against control limits.
7. **Ingredients vs. Strength** - Analyzes the relationship between ingredients and strength.
8. **Confusion Matrix** - Evaluates classification model performance.
9. **Distribution Analysis** - Studies data distribution patterns.
10. **Concrete Data Analysis** - Evaluates data related to concrete strength and properties.
""")

# Display uploaded files
st.header("Uploaded Files")

file_list = [
    ("scatter plot", "scatter plot.png"),
    ("feature importance - random forest", "feature importance - random forest.png"),
    ("pca", "pca.png"),
    ("cusum", "cusum.png"),
    ("shewhart", "shewhart.png"),
    ("ingredients vs. Strength", "ingredients vs. Strength.png"),
    ("confusion matrix", "confusion matrix.png"),
    ("distribution", "distribution.png")
]

# Show each file with an image preview
for file_name, img_path in file_list:
    st.write(f"### {file_name}")
    if os.path.exists(img_path):
        st.image(img_path, caption=file_name, use_container_width=True)
    else:
        st.error(f"File not found: {img_path}")

# Footer
st.write("---")
st.write("Developed with Streamlit for Data Analysis Reporting.")
