from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from src.mlProject.pipeline.stage_02_data_validation import DataValidationPipeline 
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline 
from src.mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline 
from src.mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

logger.info("Welcome to custom logging")

STAGE_NAME = "Data Ingestion Started"


try:
    logger.info(f"stage {STAGE_NAME} started" )
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"stage {STAGE_NAME} completed" )
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation Started"

try:
    logger.info(f"stage {STAGE_NAME} started" )
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"stage {STAGE_NAME} completed" )
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Started"

try:
    logger.info(f"stage {STAGE_NAME} started" )
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f"stage {STAGE_NAME} completed" )
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training Started"

try:
    logger.info(f"stage {STAGE_NAME} started" )
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"stage {STAGE_NAME} completed" )
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Evaluation Started"

try:
    logger.info(f"stage {STAGE_NAME} started" )
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f"stage {STAGE_NAME} completed" )
except Exception as e:
    logger.exception(e)
    raise e