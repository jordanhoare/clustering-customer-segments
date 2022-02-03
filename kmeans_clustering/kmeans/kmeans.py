import numpy as np
import pandas as pd
import pypyodbc as podbc
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

# # # # # # IMPROVEMENTS # # # # # #
# improve modular structure (atm, this is very linearly progress and doesn't follow any good OOP practices)
# type commenting


class KMeans_Prediction:
    """
    (1) Instantiate the df from the SSMS sql table
    (2) Preprocess to remove nulls and distance features
    (3) Create a plot of inertia over k to find best suitable k value
    (4) Use 'k' to predict clusters on train set
    (4) Send results to ../output folder

    """

    def __init__(self):
        self.df = self.sql_table_to_df()
        self.preprocessing()
        self.plotting()
        self.predict()

    def sql_table_to_df(self):
        con = podbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=H510I\SQLEXPRESS;"
            "Database=customers;"
            "Trusted_Connection=yes;"
        )
        SQL_Query = pd.read_sql_query("""SELECT * FROM [dbo].[raw_data]""", con)
        return SQL_Query

    def preprocessing(self):
        """ """
        features = self.df.columns.values
        rem = [
            "id",
            "district",
            "constituency",
            "postcode",
            "latitude",
            "longitude",
        ]  # remove location based features
        features = np.setdiff1d(features, rem)  # new list minus rem

        # After feature removals
        features_data = self.df[features]
        print(f"Shape of feature-removed data: ", features_data.shape)

        # Encoded data shape
        self.df = pd.get_dummies(features_data, columns=features)

    def plotting(self):
        """
        Instantiating the model on 2-15 clusters and plotting the change in inertia(over k) to find the most suitable k
        """
        X_train = self.df.values
        no_of_clusters = range(2, 16)
        inertia = []  # the within-cluster sum of squares

        # Running K means with multible Ks
        for f in no_of_clusters:
            kmeans = KMeans(n_clusters=f, random_state=100)
            kmeans = kmeans.fit(X_train)
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
        plt.savefig("output/k-inertia-plot.png")

    def predict(self):
        """
        Aftering reviewing the inertia plot, 5/6 clusters seem to be the most appropriate

        """
        # # Running K means on 6 clusters
        X_train = self.df.values
        kmeans = KMeans(n_clusters=6, random_state=2)
        kmeans = kmeans.fit(X_train)
        kmeans.labels_
        predictions = kmeans.predict(X_train)

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
        return_csv = countscldf.to_csv("output/test_predictions.csv")
        return return_csv
