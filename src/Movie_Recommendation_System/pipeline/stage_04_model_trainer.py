from Movie_Recommendation_System.config.configuration import ConfigurationManager
from Movie_Recommendation_System.components.model_trainer import ModelTrainer
from Movie_Recommendation_System.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.count_vectorizer_model()