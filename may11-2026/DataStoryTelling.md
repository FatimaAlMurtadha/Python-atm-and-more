# Deepfake Dataset (2026)

1. Dataset Overview
The KK1 dataset contains 6,557 images labeled as either REAL or FAKE, along with metadata such as gender, age group, image quality, and confidence scores. The dataset is imbalanced, with 3,767 FAKE images and 2,790 REAL images, which has implications for model evaluation and potential bias.

---

2. Class Distribution (Bar Chart)
The bar chart comparing REAL and FAKE images reveals a clear class imbalance, with FAKE images forming the majority. This imbalance is important because it can influence model behavior, causing it to favor the dominant class unless corrective techniques (e.g., class weighting) are applied.

Insight:  
The dataset is not evenly distributed, and any model trained on it must account for this imbalance to avoid biased predictions.

---

3. Confidence Score Distribution (Histogram + KDE)
The histogram shows that confidence scores are generally high, ranging from 0.80 to 0.99. Both REAL and FAKE classes exhibit strong confidence, but REAL samples tend to cluster slightly more toward higher values.

Insight:  
The model appears to be confident overall, with REAL images receiving marginally higher confidence. The overlap between the two distributions suggests that the model treats both classes similarly, with no extreme bias.

---

4. Confidence by Class (Boxplot)
The boxplot highlights the median confidence for each class. REAL images show a slightly higher median confidence, while FAKE images display a wider spread and more outliers.

Insight:  
FAKE images are more variable in difficulty, indicating that the model encounters more challenging cases in this class.

---

5. Confidence vs. Label (Scatter Plot)
The scatter plot visualizes how confidence scores differ between REAL and FAKE labels. REAL samples tend to cluster at higher confidence values, while FAKE samples show more dispersion.

Insight:  
The model is somewhat more consistent when predicting REAL images, but the overlap indicates that both classes share similar confidence ranges.

---

6. Correlation Analysis (Heatmap)
The correlation heatmap shows the relationship between the numeric features: labelnumeric and confidencescore. The correlation is small but positive, suggesting that REAL images (label 1) tend to have slightly higher confidence.

Insight:  
There is no strong linear relationship between the variables, but the slight positive correlation aligns with earlier observations from the boxplot and histogram.

---

7. Confidence Trend Across Dataset (Line Plot)
The line plot shows how confidence scores change across the dataset index. The trend is stable, with occasional dips indicating difficult or ambiguous samples.

Insight:  
The model maintains consistent confidence across the dataset, with no major fluctuations or systematic weaknesses.

---

8. Pairplot (Numeric Feature Relationships)
The pairplot provides a compact view of the numeric features. The scatter plot between label and confidence reinforces earlier findings: REAL images tend to have slightly higher confidence, but both classes overlap significantly.

Insight:  
The dataset contains few numeric variables, but the pairplot confirms the stability and distribution patterns observed in earlier visualizations.

---

### Overall Conclusion
##### The visual analysis of the KK1 dataset reveals:

- Class imbalance favoring FAKE images  
- High overall confidence from the model  
- REAL images receiving slightly higher and more stable confidence  
- FAKE images showing more variability and outliers  
- No strong correlation between label and confidence, but a slight positive trend  
- Stable confidence trend across the dataset  

These insights help identify potential bias, understand model behavior, and guide future improvements such as balancing techniques, error analysis, and model calibration.

