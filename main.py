from Movie_Recommendation_System.logging import logger
from Movie_Recommendation_System.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Movie_Recommendation_System.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Movie_Recommendation_System.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Movie_Recommendation_System.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from Movie_Recommendation_System.pipeline.stage_05_model_prediction import ModelPredictionTrainingPipeline

STAGE_NAME = "Model Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelPredictionTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e