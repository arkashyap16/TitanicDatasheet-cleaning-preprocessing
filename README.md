🚢 Titanic Dataset - Data Cleaning & Preprocessing
📌 Internship Task #1 — AI & ML
This project involves cleaning and preprocessing the Titanic dataset to prepare it for machine learning. The goal is to transform raw data into a usable form by handling missing values, encoding categorical features, scaling numerical features, and removing outliers.

🧰 Tools Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
📂 Dataset Description
The dataset includes information about Titanic passengers:

Demographics (age, sex, class)
Ticket info
Survival status
Port of embarkation
✅ Steps Performed
Exploratory Data Analysis (EDA)

Viewed dataset structure, null values, data types.
Missing Value Handling

Age: Filled with median
Embarked: Filled with mode
Cabin: Dropped due to excessive nulls
Categorical Encoding

Sex: Mapped (male → 0, female → 1)
Embarked: One-hot encoded
Feature Scaling

Age and Fare: Standardized using StandardScaler
Outlier Detection

Used IQR method to remove outliers from Fare
Saved Cleaned Dataset

Output: cleaned_titanic.csv
📦 Output Files
cleaned_titanic.csv: Final preprocessed data ready for modeling
data_cleaning_preprocessing.py: Python script with all steps
🚀 Author
Aman Raj Kashyap
Intern @ AI & ML | Python Enthusiast 💻
LinkedIn
