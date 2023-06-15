from Movie_Recommendation_System.config.configuration import ConfigurationManager
from Movie_Recommendation_System.components.data_transformation import DataTransformation
from Movie_Recommendation_System.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        extracted_file = data_transformation.file_extraction()
        df = data_transformation.read_csv(extracted_file)
        new_df = data_transformation.csv_data_transformation(df)
        data_transformation.store_dataframe_as_csv(new_df)


