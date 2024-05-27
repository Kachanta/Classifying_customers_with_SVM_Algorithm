HOW TO LOAD THE MODEL 

load the exported model and assign it to any variable e.g. loaded_model
 - loaded_model = load("model.joblib")
 
 
 HOW TO USE THE MODEL
 
in order to use the model to make new predictions based on provided or new data 
we have to load the module `my_scaler` this is because the data used to train the model is scaled. hence, we have to scale every inpute to get an accurate prediction 

we start by loading the module 
- import my_scaler
- my_scaler.data_scaler(new_data)
or 
- from my_scaler import data_scaler(new_data)
where new_data is the newly provided data to be used for predictions