from typing import Optional


def get_logger(task_id: Optional[str] = None):
    """Retrieve the loguru logger

    Workaround for the following issue with loguru:
        https://github.com/ray-project/ray/issues/14717

    Args:
        task_id: ID of the task to add to the log traces.

    Returns:
        logger (from loguru import Logger)
    """
    from loguru import logger  # pylint: disable=import-outside-toplevel

    return logger.bind(taskId=task_id) if task_id else logger
