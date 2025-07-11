from Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Text_Summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Text_Summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from Text_Summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from Text_Summarizer.logging import logger






# Data Ingestion

STAGE_NAME = "Data Ingestion stage"

try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:

    logger.exception(e)
    raise e




# Data Validation

STAGE_NAME = "Data Validation stage"

try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:

    logger.exception(e)
    raise e






# Data Transformation

STAGE_NAME = "Data Transformation stage"

try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:

    logger.exception(e)
    raise e




# Model Trainer

STAGE_NAME = "Model Training stage"

try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_traniner = ModelTrainerTrainingPipeline()
    model_traniner.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:

    logger.exception(e)
    raise e




# Model Evaluation

STAGE_NAME = "Model Evaluation stage"

try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:

    logger.exception(e)
    raise e



