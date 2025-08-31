# Student Performance Prediction

This project aims to predict student performance based on various factors such as gender, ethnicity, parental level of education, lunch type, test preparation course, and exam scores. The machine learning model trained on a dataset of student information can provide insights into predicting a student's performance in mathematics.

## Table of Contents

- [Introduction](#introduction)  
- [Note](#note-this-project-is-for-educational-purposes-only)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Dataset](#dataset)  
- [Model Training](#model-training)  
- [Results](#results)  
- [Contributing](#contributing)  
- [License](#license)  
- [Project Structure](#project-structure)  
- [Author](#author)  

## Introduction

In today's educational landscape, understanding the factors that contribute to a student's academic performance is crucial for educators, parents, and policymakers. This project leverages machine learning techniques to predict a student's performance in mathematics based on various factors. By providing accurate predictions, this tool can help identify students who may need additional support and tailor educational strategies accordingly.

## Note: This project is for Educational Purposes Only

The Student Exam Performance Predictor project is developed to showcase the application of machine learning techniques in predicting student performance. The results obtained from this project are based on a specific dataset and machine learning model, and should not be considered as definitive or accurate predictions for real-world scenarios. The primary goal of this project is to demonstrate the end-to-end process of developing a machine learning model and provide insights into the factors influencing student performance.

## Features

- Predicts student performance in mathematics based on multiple factors.  
- Provides insights into the influence of gender, ethnicity, parental level of education, lunch type, and test preparation course on student performance.  
- User-friendly interface for inputting student information and obtaining predictions.  

## Installation

Clone the repository:

```bash
git clone https://github.com/Aytech-1/student-performance-prediction.git


## Navigate to the project directory:

cd student-performance-prediction


## Install the required dependencies:

pip install -r requirements.txt

## Usage

Run the application:

python app.py


Access the web interface in your browser at http://localhost:5000.

Fill in the student information and submit the form to obtain the predicted math score.

## Dataset

The dataset used for training the machine learning model is sourced from Kaggle - Students Performance in Exams
.
It contains information about students' demographics, parental education, lunch type, test preparation course, and their corresponding exam scores.

## Model Training

The machine learning model is trained using supervised learning algorithms (e.g., Random Forest, XGBoost, CatBoost) to predict the math score based on the input features. The dataset is split into training and testing sets to evaluate the model's performance.

## Results

The trained model achieved an accuracy of around 85% in predicting student performance in mathematics. The results demonstrate the significant impact of factors such as parental education, test preparation course, and lunch type on student scores.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License
.

## Project Structure
student-performance-prediction/
├── artifacts/          # Contains artifacts generated during the model training process
├── catboost_info/      # Stores CatBoost model information
│   └── learn/
├── Notebook/           # Notebooks used for data exploration and analysis
│   └── data/
├── src/                # Source code for the project
│   ├── components/     # Components and modules used in the project
│   └── pipeline/       # Data processing and model training pipeline
├── static/             # Static files used in the web application (CSS, etc.)
│   └── css/
└── templates/          # HTML templates used in the web application



-artifacts: Contains artifacts generated during the model training process.

-catboost_info: Stores CatBoost model information.

-Notebook: Contains notebooks used for data exploration and analysis.

-src: Source code for the project.

-components: Components and modules used in the project.

-pipeline: Data processing and model training pipeline.

-static: Static files used in the web application (CSS, etc.).

-templates: HTML templates used in the web application.

## Author

👤 ADEYEMI AYOBAMI SAMSON

📧 Email: adeyemiayobami273@gmail.com

📞 Phone: 09030019355

🌍 Location: Abeokuta, Ogun State, Nigeria
GitHub: @Aytech-1

Feel free to reach out with any questions or feedback regarding the project.
