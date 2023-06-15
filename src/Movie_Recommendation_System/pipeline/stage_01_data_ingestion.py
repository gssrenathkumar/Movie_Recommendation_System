from Movie_Recommendation_System.config.configuration import ConfigurationManager
from Movie_Recommendation_System.components.data_ingestion import DataIngestion
from Movie_Recommendation_System.logging import logger

class DataIngestionTrainingPipeline:
    def __int__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()