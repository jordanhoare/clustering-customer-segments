[WIP] K-Means Clustering
============
[![GitHub Stars](https://img.shields.io/github/stars/jordanhoare/kmeans-clustering.svg)](https://github.com/jordanhoare/kmeans-clustering/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/jordanhoare/kmeans-clustering.svg)](https://github.com/jordanhoare/kmeans-clustering/issues) [![Current Version](https://img.shields.io/badge/version-0.5.0-green.svg)](https://github.com/jordanhoare/kmeans-clustering) 

</br>

A python app that utilises KMeans clustering to identify six market segments from event survey data. The analysis utilises Sklearn’s KMeans algorithm, and is spun up with FastAPI so a web-driven form can integrate new data down the pipeline to a PowerBI dashboard that provides prescriptive notes [Python, JavaScript, FastAPI, SQL, PowerBI].

</br>

## Project Features
- [x] instantiate the project using pyenv, poetry
- [x] connect to SQLite with sqlalchemy object related mapping
- [x] processing pipeline (csv -> SQL -> python -> SQL -> PowerBI)
- [ ] embed powerbi dashboard
- [ ] link a fastapi form to submit to db to store new data 
- [ ] CI/CD (automate data submission so that dashboard batch processes)
- [ ] host via Heroku for a live demo capability

</br>

## Data Processing

- [x] preprocessing
- [x] cleaning
- [ ] feature engineering 
- [x] inital modelling using SKLearn K-Means
- [ ] PCA (configure no. of components)
- [ ] retrain (adjust params accordingly)


</br>

## Dashboarding
- [ ] create events cluster dashboard
- [ ] analyse & summarise traits of each cluster
- [ ] interactive NPS analytics 
- [ ] breakdown tree 
- [ ] prescription analysis & formulate insights for actions

</br>

<!-- ## Installation
To demo this application: clone the repo, navigate to the project folder and run `poetry shell` to open the venv.  Run the ` __main__.py ` file to start the server.  You can then access the web UI @ `http://127.0.0.1:8000/` -->


## Requirements 
- Pyenv (python)
- Poetry (python)
- PowerBI

 
</br>

</br>


<p align="center">
    <a href="https://www.linkedin.com/in/jordan-hoare/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>&nbsp;&nbsp;
    <a href="https://www.kaggle.com/jordanhoare">
        <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" />
    </a>&nbsp;&nbsp;
    <a href="mailto:jordanhoare0@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
    </a>&nbsp;&nbsp;
</p>



