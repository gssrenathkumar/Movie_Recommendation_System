from Movie_Recommendation_System.entity import ModelPredictionConfig
import os
import pickle

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
        with open(self.config.data_path+"/"+files_array[1], 'rb') as file1:
           similarity = pickle.load(file1)

        return movie_list,similarity







