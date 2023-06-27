# flightPricePrediction_IBMWatson

People who work frequently travel through flight will have better knowledge on best discount and right time to buy the ticket. For the business purpose many airline companies change prices according to the seasons or time duration. They will increase the price when people travel more. Estimating the highest prices  of the airlines data for the route is collected with features such as Duration, Source, Destination, Arrival and Departure. Features are taken from chosen dataset and in the price wherein the airline price ticket costs vary overtime. we have implemented flight price prediction for users by using KNN, decision tree and random forest algorithms. Random Forest  shows the best accuracy of 80% for predicting the flight price. also, we have done correlation tests and metrics for the statistical analysis.

# Project Flow
•       User interacts with the UI to enter the input.

•       Entered input is analyzed by the model which is integrated.

•       Once model analyses the input the prediction is showcased on the UI


To accomplish this, we have to complete all the activities listed below,

•       Data collection

•       Collect the dataset or create the dataset

•       Visualizing and analyzing data

                        Importing Libraries

                        Read the DataSet

•       Data pre-processing

•       Checking for null values

•       Handling outlier

•       Handling categorical data

•       Splitting data into train and test

•       Model building
            A function named RandomForest, GradientBoosting, AdaBoost  is created and train and test data are passed as the parameters. Inside the function,                 RandomForest, GradientBoosting, AdaBoost  algorithm is initialized and training data is passed to the model with .fit() function. Test data is                   predicted with .predict() function and saved in new variable. For evaluating the model, r2_score, mean_absolute_error, and mean_squared_error report             is done.
            
•       Hypertuning the Model

•       Evaluation and saving the model in a pickle file

# Application Building


# Flight Price Prediction

This is a web application that predicts the price of flight tickets based on various features such as departure date, arrival date, source, destination, number of stops, and airline. It uses a machine learning model trained on historical flight data to make predictions.

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository


2. Navigate to the project directory:

```
cd Flight-Price-Prediction-master
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Start the Flask development server:

```
python app.py
```

5. Open your web browser and visit the assigned localhost to access the application.

## Usage

1. Fill in the necessary information in the input fields provided. This includes the departure date, arrival date, source, destination, number of stops, and airline.

2. Click on the "Submit" button to make the prediction.

3. The predicted flight price will be displayed on the screen.

## Dependencies

The following dependencies are required to run the application:

- Flask
- Scikit-learn
- Pandas
- NumPy

These dependencies can be installed by running the following command:

```
pip install -r requirements.txt
```

## Directory Structure

The directory structure of the project is as follows:

```
Flight-Price-Prediction-master/
  ├── app.py
  ├── static/
  │   ├── css/
  │   │   └── styles.css
  ├── templates/
  │   └── index.html
  ├── trained_models/
  │   └── model.pkl
  ├── .gitignore
  ├── LICENSE
  ├── Procfile
  ├── README.md
  └── requirements.txt
```
#Outputs - Model

One hot encoding
<img width="1200" alt="image" src="https://github.com/Anusha19011901/flightPricePrediction_IBMWatson/assets/75386520/4c0a14cd-531d-4302-bb4f-f5c4c1bfbc29">

Label encoding
<img width="1200" alt="image" src="https://github.com/Anusha19011901/flightPricePrediction_IBMWatson/assets/75386520/9004fac0-cf05-44c7-9bea-7ac5c4989828">

Heatmap
![image](https://github.com/Anusha19011901/flightPricePrediction_IBMWatson/assets/75386520/f82f539b-2a8a-4144-bef9-f178be72de86)

![image](https://github.com/Anusha19011901/flightPricePrediction_IBMWatson/assets/75386520/4fad3129-bad6-4917-9328-9818c084b4af)

Distplot - fitting model
![image](https://github.com/Anusha19011901/flightPricePrediction_IBMWatson/assets/75386520/e5373bbc-e209-40d1-bb9f-06f57b2df37c)

Scatterplot
![image](https://github.com/Anusha19011901/flightPricePrediction_IBMWatson/assets/75386520/72681a3c-70fd-479b-b26e-7abd150aeb95)

After Hupertuning
![image](https://github.com/Anusha19011901/flightPricePrediction_IBMWatson/assets/75386520/b7365242-61f4-4b89-96ae-4ff8192b2bc9)


```

```
#Outputs - Application

<img width="1289" alt="image" src="https://github.com/Anusha19011901/flightPricePrediction_IBMWatson/assets/75386520/cfe8fb07-66a0-403c-bf36-b40d5fb26acb">

<img width="932" alt="image" src="https://github.com/Anusha19011901/flightPricePrediction_IBMWatson/assets/75386520/a9aac75e-5484-40c6-97fc-60d875521129">

```


```

# Deployment using IBM

Upload the ipynb file on to the assets section in Watson Studio

Using the ibm_watson_machine_learning package to store a machine learning model in IBM Watson Studio

The model is stored in the repository using client.repository.store_model(), which takes the model, metadata properties, training data, and training target as parameters. The reg_rf model is stored with the specified metadata and training data.

Now create a deployment space and deploy the model. Include the endpoint url in the app.py code to connect to the backend.



```




