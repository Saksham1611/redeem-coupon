import numpy as np
import pandas as pd
import xgboost as xgb
import warnings
warnings.filterwarnings("ignore")
from sklearn import linear_model
from sklearn import ensemble
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

    #label encode the features
    for col in features:
        #initialize LabelEncoder for each feature col.
        lbl=preprocessing.LabelEncoder()
        #fir label encoder on all data
        lbl.fit(df[col])

        #transform all data 
        df.loc[:,col]=lbl.transform(df[col])

    #get training data using folds
    df_train=df[df.kfold!=fold].reset_index(drop=True)

    #get validation data using folds
    df_valid =df[df.kfold==fold].reset_index(drop=True)

    #get training data 
    x_train=df_train[features].values

    #get training data 
    x_valid=df_valid[features].values

    #initialize random forest model
    model=xgb.XGBClassifier(use_label_encoder =False,
                n_jobs=-1,
                max_depth=7,
                n_estimators=1000,
                learning_rate=0.05
    )

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





