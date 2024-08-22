from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from src.mlProject.pipeline.stage_02_data_validation import DataValidationPipeline 


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