# Second DataSet: student_performance_grade:

### Dataset count
- 8000 rows and 18 columns

### Numerical Features (['Age', 'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Stress_Level','Screen_Time', 'Previous_GPA', 'Tutoring_Sessions_Per_Week','Exam_Anxiety_Score'])

- classification
- boxplots vs Grade  
- violinplots vs Grade

### Categorical Features (['Student_ID', 'Gender', 'Part_Time_Job', 'Study_Method', 'Diet_Quality','Internet_Quality', 'Extracurricular', 'Family_Income_Level', 'Grade'])
- countplots  
- group analysis  
- comparison between Grade groups 


### No missing Values
### No duplicates
### Data Types are correct


### Insight
Grade Distribution
- A = 55.9%  
- B = 27.6%  
- C = 13.1%  
- D = 2.8%  
- Fail = 0.4%  

- Hours_Studied: 
    1. mean -> 5 hours
    2. max  -> 12

- Stress_Level:
    1. mean  -> 5
    2. range ( 1 : 10)

- Exam_Anxiety_Score:
    1. mean -> 3.0
    2. range ( 1 : 10) 

- Previous_GPA: 
    1. mean -> 3.0
    2. max  -> 6.7

- Sleep_Hours:
    - mean -> 
    - range ( 3 : 10)

-  Attendance:
    1. mean -> 
    2. range ( 43% : 100%)
 

Insight:  
- The dataset is highly skewed toward high performance.  
- Very few failing students => synthetic or idealized educational system.  
- Similar pattern to FinalScore dataset.


## Columns that would effect Grade
    1. Positive Correlation:
        - Hours_Studied
        - Attendance
        - Previous_GPA
    2. Negative Correlation
        - Stress_Level
        - Screen_Time
        - Exam_Anxiety_Score

# 1. Numerical Columns: 
['Age', 'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Stress_Level',
       'Screen_Time', 'Previous_GPA', 'Tutoring_Sessions_Per_Week',
       'Exam_Anxiety_Score', 'Final_Score'] ( 8000 rows × 10 columns)

    - 1. more (Hours_Studied) => Grade -> Strong positive
    - 2. more (exam anxiety) less performance (Grade) -> Strong negative
    - 3. more (Tutoring Sessions Per Week) more (Grade) -> Correlation != causation -> we can't prove the reason directly.
    - 4. more (Stress Level) less (Grade) -> negative correlation 
    - 5. Who has a previous Good performance ability Would mostly still be good.
    - 6. (Screen Time) can cause a less grade -> Weak negative correlation
    - 7. Age -> No correlation

# 2. Categorical Columns Analysis

    - 1. Gender: Balanced distribution -> No strong effect on Grade.
    - 2. Study_Method: Offline slightly associated with better grades. Online shows more variation. Hybrid = middle performance.
    - 3. PartTimeJob: Interesting variable. Students with jobs may have slightly lower grades.
    - 4. FamilyIncomeLevel: Middle income dominant. Higher income slightly associated with better grades.
    - 5. DietQuality and InternetQuality: Weak but noticeable patterns. Better quality -> slightly better grades

### Most important positive factors: (Higher -> Better Grade)
1. Hours_Studied  
  - A: 5.91  
  - Fail: 1.55  
  - Strong, clean gradient A -> Fail  
2. Attendance  
  - Higher attendance -> higher grade  
3. Previous_GPA  
  - Students with strong academic history continue to perform well   

### Most important Negative factors (Higher -> Worse Grade)
1. Stress_Level  
  - A: 3.88  
  - Fail: 7.39  
  - Very strong negative pattern  
2. Exam_Anxiety_Score  
  - Higher anxiety -> lower grade  
3. Screen_Time  
  - Weak negative effect  

# Final Summary — 14-05-2026

## Key Patterns with Grade

1. Strong Positive Predictors
- Hours_Studied  
- Attendance  
- Previous_GPA  

2. Strong Negative Predictors
- Stress_Level  
- ExamAnxietyScore  

3. Weak Predictors
- Screen_Time  
- Sleep_Hours  

4. No Predictive Power
- Age  
# The cleaned df
- shape (8000, 17)

# Hypotheses (Before Visualization)

- (Students who study more hours tend to get higher grades).  
- (Higher stress and anxiety reduce academic performance).  
- (Students with strong academic history (GPA) maintain high grades).  
- Attendance is a key factor in achieving A/B grades.  
- Students with part-time jobs may face performance challenges.  

-------------------------------------------------------------------------------------------------------------------------

### DATA STORYTELLING (Grade Dataset - Grade Distribution)
 
- The system produces mostly high-performing students.  
- Failures are extremely rare → synthetic or idealized dataset.  

### DATA STORYTELLING (Grade Dataset - Hours_Studied vs Grade)
- Clear, strong gradient:  
  A > B > C > D > Fail  
- Studying is the strongest factor affecting Grade.  
- High-performance zone:  
  - 6–12 hours/day  
- Low-performance zone:  
  - 0–3 hours/day  

### DATA STORYTELLING (Grade Dataset - Stress_Level vs Grade)
- Strong negative relationship  
- Students with A have the lowest stress  
- Students with D/Fail have the highest stress  

### DATA STORYTELLING (Grade Dataset - Exam_Anxiety vs Grade)
- Anxiety strongly reduces performance  
- High anxiety → almost no A grades  
- Low anxiety → high concentration of A/B  

### DATA STORYTELLING (Grade Dataset - Study Method)
- Offline → best performance  
- Hybrid → medium  
- Online → more variation, some weak results  

### DATA STORYTELLING (Grade Dataset - Pairplot)
- Academic effort + psychological stability = best performance  
- Anxiety affects Grade more strongly than Stress_Level  