import numpy as np
import pandas as pd
from sklearn import linear_model
import joblib
import pickle
from sklearn import metrics
from sklearn import preprocessing

if __name__=="__main__":
    #load training data (with folds)
    df_train=pd.read_csv("../input/train_data.csv")

    #load test data for prediction of values
    df_test=pd.read_csv("../input/test_data.csv")

    #all cols are feature except id, redemption_status and kfold
    features=[f for f in df_train.columns if f not in {'id', 'redemption_status'}]

    #fill all NAN values with NONE
    #converting all columns to "strings" (as all the cols are categ.)

    for col in features:
        df_train.loc[:,col]=df_train[col].astype(str).fillna("NONE")
        df_test.loc[:,col]=df_test[col].astype(str).fillna("NONE")

    #initialize one hot encoder
    ohe=preprocessing.OneHotEncoder()

    ohe.fit(df_train[features])
    ohe.fit(df_test[features])

    #transform training data
    x_train=ohe.transform(df_train[features])

    with open("../models/one_hot.pkl","wb") as one_hot_file:
        pickle.dump(ohe,one_hot_file)

    #transforms validation data 
    x_test=ohe.transform(df_test[features])

    #initialize Logistic Regression model
    model= linear_model.LogisticRegression()

    print(f"Shape of x_train {x_train.shape}")
    print(f"Shape of x_test {x_test.shape}")
    #fit model on training data(ohe)
    model.fit(x_train,df_train.redemption_status.values)

    #save model 
    filepath = '../models/logres_model.pkl'
    joblib.dump(model,filename=filepath)

    #predict on test data
    test_preds=model.predict(x_test)
    

    #make a dataframe
    test_preds= pd.DataFrame(test_preds,columns=['redemption_status'])
    final=pd.concat([df_test,test_preds],axis=1)

    #save the prediction file
    final.to_csv("../prediction.csv",index=False)












