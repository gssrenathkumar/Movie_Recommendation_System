from Movie_Recommendation_System.config.configuration import ConfigurationManager
from Movie_Recommendation_System.components.model_prediction import ModelPrediction
from Movie_Recommendation_System.logging import logger


class ModelPredictionTrainingPipeline:
    def  __int__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_prediction_config()
        model_evaluation_config = ModelPrediction(config= model_evaluation_config)
        model_evaluation_config.load_folder_pickle_files()