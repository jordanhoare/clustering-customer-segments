##########################################################
################ Load Packages / libraries ###############
##########################################################
import numpy as np
import pandas as pd
import pypyodbc as podbc
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


##########################################################
################ K-MEANS CLUSTERING CLASS ################
##########################################################
class Cluster_Prediction:
    """
    (1) Instantiate the model & tokenizer
    (2) Create_lenet
    (3) Inference
    (4) Predict & return list of prediction and probability

    """

    def __init__(self):
        self.con = podbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=H510I\SQLEXPRESS;"
            "Database=customers;"
            "Trusted_Connection=yes;"
        )

        self.preprocessing()
        self.train()
        self.predict()

    def preprocessing(self):
        """ """
        SQL_Query = pd.read_sql_query("""SELECT * FROM [dbo].[raw_data]""", self.con)

        features = SQL_Query.columns.values
        rem = [
            "id",
            "district",
            "constituency",
            "postcode",
            "latitude",
            "longitude",
        ]  # remove location based features
        features = np.setdiff1d(features, rem)

        # After feature removals
        features_data = SQL_Query[features]
        print(f"Shape of feature-removed data: ", features_data.shape)

        # Encoded data shape
        self.df = pd.get_dummies(features_data, columns=features)

    def train(self):
        """
        (1) Instantiate the model & tokenizer

        """
        self.X_train = self.df.values
        no_of_clusters = range(2, 16)
        inertia = []  # the within-cluster sum of squares

        # Running K means with multible Ks
        for f in no_of_clusters:
            kmeans = KMeans(n_clusters=f, random_state=100)
            kmeans = kmeans.fit(self.X_train)
            u = kmeans.inertia_
            inertia.append(u)

        # Creating the scree plot for Intertia - elbow method
        fig, (ax1) = plt.subplots(1, figsize=(15, 6))
        xx = np.arange(len(no_of_clusters))
        ax1.plot(xx, inertia)
        ax1.set_xticks(xx)
        ax1.set_xticklabels(no_of_clusters, rotation="vertical")
        plt.xlabel("Number of clusters")
        plt.ylabel("Inertia")
        plt.title("Inertia per K")
        plt.savefig("k-intertia-plot.png")

    def predict(self):
        """
        (1) Instantiate the model & tokenizer

        """
        # # Running K means on 6 clusters
        kmeans = KMeans(n_clusters=6, random_state=2)
        kmeans = kmeans.fit(self.X_train)
        kmeans.labels_
        predictions = kmeans.predict(self.X_train)

        # calculating the Counts of the cluster
        _, counts = np.unique(predictions, return_counts=True)
        counts = counts.reshape(1, 6)

        # Creating a datagrame
        countscldf = pd.DataFrame(
            counts,
            columns=[
                "Cluster 1",
                "Cluster 2",
                "Cluster 3",
                "Cluster 4",
                "Cluster 5",
                "Cluster 6",
            ],
        )
        return_csv = countscldf.to_csv("test_predictions.csv")
        return return_csv
