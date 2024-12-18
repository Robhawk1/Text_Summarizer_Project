from textSummarizer.pipeline.stage_01_data_ingenstion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
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

STAGE_NAME3 = "Data Transformation State"

try:
    logger.info(f">>> stage {STAGE_NAME3} started <<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>> stage {STAGE_NAME3} completed <<<\n\n====")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME4 = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME4} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME4} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME5 = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME5} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME5} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e