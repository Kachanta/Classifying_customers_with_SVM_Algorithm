def data_scaler(x):
    
    #Importing the standard scaler
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    
    #Scalling 
    new_data_scaled = scaler.fit_transform(x)
    return new_data_scaled