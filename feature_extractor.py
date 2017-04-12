import pandas as pd

def load_feature_matrix(path):
    df=pd.read_csv(path)
    df['TitleLength']=df.Title.apply(len)
    df['BodyLength']=df.BodyMarkdown.apply(len)
    df['Tag2nan']=pd.isnull(df['Tag2'])*1
    df['Tag3nan']=pd.isnull(df['Tag3'])*1
    return df
