Anemia-Sense
Anemia Sense uses machine learning to predict whether a person has anemia based on key blood indicators such as MCHC, MCH, MCV, hemoglobin levels and gender.
This tool helps in early detection by analyzing these metrics to classify anemia presence.


Features:
- Machine learning-based prediction model.
- Analyzes MCHC, MCH, MCV, hemoglobin and gender to determine anemia risk.
- User-friendly interface to input blood test data and recieve predictions.


Technologies Used:
- scikit-learn (for the machine learning model)
- Flask (for backend)
- Html, CSS (for frontend)
- Pandas (for data analysis and data manipulation)
- Numpy (used to handle and structure the user-input data into arrays for feeding into the machine learning model for prediction)
- Matplotlib (data visualization)
- Seaborn (advanced data visualization)
- Joblib (for making pickle file and saving model)

Process for model:
Step 1: Use Model.ipynb file in google collab.
Step 2: Execute all the code in cells in the collab file and download the file by joblib.
Step 3: Use the joblib file instead of model.joblib in model folder.
