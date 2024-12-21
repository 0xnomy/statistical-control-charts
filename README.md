# Concrete Strength Monitoring Using Machine Learning and Statistical Control Charts

## Overview
This project was part of the Advanced Linear Algebra course where we had to set up statistical control charts to monitor processes. It was taught by Dr. Babar Zaman, and this project represents my take on it.


---

## Features

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

---

## Dataset

The dataset used in this project is sourced from Kaggle and includes 1030 records with 8 distinct features:
- **Cement**
- **Blast Furnace Slag**
- **Fly Ash**
- **Water**
- **Superplasticizer**
- **Coarse Aggregate**
- **Fine Aggregate**
- **Age**

The target variable is **Strength**, representing the concrete’s compressive strength in megapascals (MPa).

---

## Methodologies

### Statistical Process Control
- **Shewhart Control Charts**: Monitor consistency and detect anomalies.
- **CUSUM Control Charts**: Identify gradual drifts in mean values.

### Dimensionality Reduction
- **Principal Component Analysis (PCA)**: Reduces dimensional complexity while retaining 95.19% of variance, highlighting key trends.

### Machine Learning
- **Random Forest Models**: Predict strength and rank feature importance, identifying Cement and Age as dominant predictors.

---

## Application
This project uses **Streamlit** to create an interactive dashboard for visualizing results and uploading datasets. The following visualizations are supported:

1. Scatter Plot
2. Feature Importance - Random Forest
3. PCA
4. CUSUM
5. Shewhart Charts
6. Ingredients vs. Strength
7. Confusion Matrix
8. Distribution Analysis

---

## Visuals
1. **Scatter Plot Analysis**
![Scatter Plot](scatter%20plot.png)

2. **Feature Importance - Random Forest**
![Feature Importance](feature%20importance%20-%20random%20forest.png)

3. **PCA - Principal Component Analysis**
![PCA](pca.png)

4. **CUSUM Control Chart**
![CUSUM](cumsum.png)

5. **Shewhart Control Chart**
![Shewhart](shewhart.png)

6. **Ingredients vs. Strength**
![Ingredients vs. Strength](ingredients%20vs.%20Strength.png)

7. **Confusion Matrix**
![Confusion Matrix](confusion%20matrix.png)

8. **Distribution Analysis**
![Distribution Analysis](distribution.png)

---

## Setup Instructions

1. Clone this repository:
```
git clone git@github.com:0xnomy/statistical-control-charts.git
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the application:
```
open multivariate-control-chart-analysis.ipynb
streamlit run app.py
```

---

## Technologies Used
- **Python**
- **Streamlit**
- **Scikit-learn**
- **Matplotlib**
- **Pandas**
- **NumPy**

---

## Results and Findings
- Cement and Age were identified as the most influential features.
- PCA captured 95.19% variance, simplifying analysis.
- Random Forest achieved 88% prediction accuracy.
- Control charts effectively detected anomalies and process deviations.

---

## Future Enhancements
- Incorporating additional machine learning algorithms.
- Adding time-series forecasting for dynamic process monitoring.
- Enhancing visualizations for better interpretability.

---

## License
This project is licensed under the MIT License

---

## References
- Montgomery, D. C. (2020). Introduction to Statistical Quality Control.
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning.

---

## Contact
For questions or suggestions, feel free to reach out via issues.
