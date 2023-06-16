from Movie_Recommendation_System.entity import ModelPredictionConfig
from Movie_Recommendation_System.logging import logger
import os
import pickle
import pandas as pd

class ModelPrediction:
    def __init__(self, config: ModelPredictionConfig):
        self.config = config

    def load_folder_pickle_files(self):
        files_array = []
        for file_name in os.listdir(self.config.data_path):
            if os.path.isfile(os.path.join(self.config.data_path, file_name)):
                files_array.append(file_name)

        with open(self.config.data_path+"/"+files_array[0], 'rb') as file:
            movie_list = pickle.load(file)
            logger.info("Movies list pickle file sucessfully loaded")
        with open(self.config.data_path+"/"+files_array[1], 'rb') as file1:
           similarity = pickle.load(file1)
           logger.info("Similarity pickle file sucessfully loaded")

        return movie_list,similarity

    def movie_titles(self,movies_dict):
        movies = pd.DataFrame(movies_dict)
        logger.info("Movies_title sucessfully loaded")
        return movies

    def recommendation(self,new_df,similarity,movie):
        movie_index = new_df[new_df["title"] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        with open(self.config.root_dir + "/" + "test.txt", 'w') as file1:
            file1.write("")

        for i in movies_list:
            data = new_df.iloc[i[0]].title
            with open(self.config.root_dir+"/"+"test.txt", 'a') as file:
                file.write(data)
                file.write("\n")
        logger.info("Recommendation data is sucessfully written in text file")









