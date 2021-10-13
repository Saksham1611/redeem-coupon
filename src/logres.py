import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn import preprocessing

def run(fold):

    #load training data (with folds)
    df=pd.read_csv("../input/train_data_folds.csv")

    #all cols are feature except id, redemption_status and kfold
    features=[f for f in df.columns if f not in {'id', 'redemption_status','kfold'}]

    #fill all NAN values with NONE
    #converting all columns to "strings" (as all the cols are categ.)

    for col in features:
        df.loc[:,col]=df[col].astype(str).fillna("NONE")

    #get training data using folds
    df_train=df[df.kfold!=fold].reset_index(drop=True)

    #get validation data using folds
    df_valid =df[df.kfold==fold].reset_index(drop=True)

    #initialize one hot encoder
    ohe=preprocessing.OneHotEncoder()

    #fit ohe on training +  validation features
    full_data=pd.concat([df_train[features],df_valid[features]],axis=0)

    ohe.fit(full_data[features])

    #transform training data
    x_train=ohe.transform(df_train[features])

    #transforms validation data 
    x_valid=ohe.transform(df_valid[features])

    #initialize Logistic Regression model
    model= linear_model.LogisticRegression()

    #fit model on training data(ohe)
    model.fit(x_train,df_train.redemption_status.values)

    #predict on validation data
    #get prob. values for calculating AUC
    valid_preds=model.predict_proba(x_valid)[:,1]
    
    #get roc auc score
    auc=metrics.roc_auc_score(df_valid.redemption_status.values,valid_preds)
    
    #print score
    print(f"At Fold {fold} : AUC score is {auc}")



if __name__=="__main__":
    for fold_ in range(5):
        run(fold_)





