import pandas as pd
from sklearn import model_selection

if __name__=="__main__":

    #read training data
    df=pd.read_csv("../input/train_data.csv")

    #create a new column Kfold and fill it with -1
    df["kfold"] = -1

    #randomize rows of data
    df=df.sample(frac=1).reset_index(drop=True)

    #fetch labels
    y=df.redemption_status.values

    #init the Kfold class from model selection module
    kf= model_selection.StratifiedKFold(n_splits=5) 

    #fill new kfold column
    for f , ( t_ ,v_) in enumerate(kf.split(X=df,y=y)):
        df.loc[v_,'kfold']=f

    df.to_csv("../input/train_data_folds.csv",index=False)
    



