from Movie_Recommendation_System.config.configuration import ConfigurationManager
from Movie_Recommendation_System.components.model_prediction import ModelPrediction
from Movie_Recommendation_System.logging import logger
import random

class ModelPredictionTrainingPipeline:
    def  __int__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_prediction_config = config.get_model_prediction_config()
        model_prediction_config = ModelPrediction(config= model_prediction_config)
        movies_list_pkl,similarity_pkl = model_prediction_config.load_folder_pickle_files()
        movies_list = model_prediction_config.movie_titles(movies_list_pkl)
        value = random.randint(0,len(movies_list))
        model_prediction_config.recommendation(movies_list, similarity_pkl, movies_list["title"][value])
        logger.info("Model Prediction Pipeline is Sucessfully Implemeted")


