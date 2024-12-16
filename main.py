from textSummarizer.pipeline.stage_01_data_ingenstion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME1 = "Data Ingestion stage"

try:
    logger.info(f">>> stage {STAGE_NAME1} started <<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAME1} completed <<<\n\n====")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME2 = "Data Validation State"

try:
    logger.info(f">>> stage {STAGE_NAME2} started <<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAME2} completed <<<\n\n====")
except Exception as e:
    logger.exception(e)
    raise e