# Code Base Author: 

Michael Leow Hoe Seng

# AI300_Capstone : Telecom Churn Prediction

Simple Flask template for ML model predictions via (1) HTML Form (2) API requests to predict the probabilities of customer telecom churned result

## Folder Structure of my app

├── data
│   └── ai300_capstone_df.csv
├── Img
│   └── Post_API_result_260924.png
|   └── Web AWS Results page _270924-p09_DNS.png
|   └── Web AWS Results page _270924-p09.png
├── model
│   └── rf_auc_score.pkl
├── notebooks
│   └── api_query_example.ipynb
│   └── research.ipynb
├── src
│   └── static
│      └── style.css
│   └── templates
│      └── index.html
│   └── app.py
│   └── input_processing.py
│   └── model.py
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt

## About This Repo

- Package dependencies can be found in `requirements.txt` file.
- Command to start Flask app: `python src/app.py`

- Screenshot image of the web UI can be found in Img Folder

- ML model chosen will be RandomForest Classifier under model folder ----> rf_auc_score.pkl
- Accuracy Test for RandomForest will be :  0.8591482797855745

- Github repository to pull is under the address https://github.com/Heicoders-AI300/aug24-p09.git

- AWS Web interface address will be as follow (Public)
1) http://http://54.169.118.80/
2) http://ec2-54-169-118-80.ap-southeast-1.compute.amazonaws.com/

## Acknowledgements

Dataset Source: Heicoder - ai300_capstone converted to joined table combined csv file under data folder ---> ai300_capstone_df.csv


