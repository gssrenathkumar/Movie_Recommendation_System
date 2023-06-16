from Movie_Recommendation_System.config.configuration import ConfigurationManager
from Movie_Recommendation_System.components.data_validation import DataValiadtion
from Movie_Recommendation_System.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()
        logger.info("Data Validation Pipeline is Sucessfully Implemeted")