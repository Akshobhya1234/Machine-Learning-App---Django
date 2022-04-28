from django.db import models
import requests
import getpass
import json
from urllib.parse import urlparse,urljoin
from django.contrib.auth.models import User
from .choices import *

class searchUser(models.Model):
    UserName = models.CharField(max_length=200)
    FileName = models.CharField(max_length=200,primary_key=True)
    UploadCSV = models.FileField(upload_to ="media/")
    label = models.CharField(max_length =200)
    model = models.CharField(max_length=200,choices=selectChoice)
    
    @property
    def FileHead(self):
        import pandas as pd 
        import numpy as np 
        dataFrame = pd.read_csv(self.UploadCSV,header=0)
        #return(dataFrame.head())
        
        from sklearn.naive_bayes import GaussianNB
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.preprocessing import LabelEncoder
        from sklearn.model_selection import train_test_split
        for column in dataFrame.columns:
            if dataFrame[column].dtype == type(object):
                le = LabelEncoder()
                dataFrame[column] = le.fit_transform(dataFrame[column].astype(str))
            dataFrame[column]=np.nan_to_num(dataFrame[column])
        
        df_label = dataFrame[self.label]
        del dataFrame[self.label]
        df_train_features, df_test_features, df_train_label, df_test_label = train_test_split(dataFrame, df_label , test_size=0.2)
        df_train_label = np.ravel(df_train_label)
        df_test_label = np.ravel(df_test_label)
        KNN_mod = KNeighborsClassifier(n_neighbors = 3)
        KNN_mod.fit(df_train_features, df_train_label)
        
        
        df_test = pd.DataFrame(df_test_features, columns = dataFrame.columns)
        
        df_test['predicted'] = KNN_mod.predict(df_test_features)
        df_test['correct'] = [1 if x == z else 0 for x, z in zip(df_test['predicted'], df_test_label)]
        accuracy = 100.0 * float(sum(df_test['correct'])) / float(df_test.shape[0])
        return(" "+str(accuracy))

    @property
    def dTypes(self):
        import pandas as pd 
        import numpy as np 
        dataFrame = pd.read_csv(self.UploadCSV,header=0)
        return(dataFrame.dtypes)
        

    @property
    def histPlot(self):
        import pandas as pd 
        import numpy as np 
        import matplotlib.pyplot as plt
        import seaborn as sns
        dataFrame = pd.read_csv(self.UploadCSV,header=0)
        def cond_hist(df,plot_cols,bins = 10):
        
            for col in plot_cols:
                fig = plt.figure()
                ax = fig.gca()
                df[col].plot.hist(ax = ax,bins = bins)
                ax.set_title('Histograms of '+col)
                ax.set_xlabel(col)
                ax.set_ylabel('Frequency')
                return(plt.show())
        return(cond_hist(dataFrame,self.label))


class userDetails(models.Model):
    userName = models.CharField(max_length=200)
    model = models.CharField(max_length=200,choices=selectChoice)



    def __str__(self):
        return self.userName

class modelResult(models.Model):
    userName=models.CharField(max_length=200,default="Akshobhya")


class hyperParameter(models.Model):

    userName = models.CharField(max_length=200)
    FileName=models.ForeignKey(searchUser, on_delete="cascade")

    #KNN
    n_neighbors = models.IntegerField(default=5)
    algorithm = models.CharField(max_length=100,default="auto")

    #decisionTree
    criterion = models.CharField(max_length=20,default="gini")
    min_sample_depth = models.IntegerField(default=2)
    splitter = models.CharField(max_length=20,default="best")
    max_depth = models.IntegerField(default=None)
    min_samples_leaf = models.IntegerField(default=1)
    min_weight_fraction_leaf = models.IntegerField(default=1)
    max_leaf_nodes = models.IntegerField(default = None)
    min_impurity_decrease =models.FloatField(default=0.0)
    min_impurity_split = models.FloatField(default=0.0)

    #SVM
    kernel = models.CharField(max_length=200,default="rbf")
    degree = models.IntegerField(default=3)
    gamma = models.CharField(max_length=200,default = "scale")
    probability = models.BooleanField(default=True)

    #RandomForest
    n_estimators = models.IntegerField(default=100)
    criterion = models.CharField(max_length=200,default="gini")
    max_depth1 = models.IntegerField(default=None)

    @property
    def accuracy(self):
        su = searchUser()
        if(su.UserName==self.userName):
            return(su.FileName)
