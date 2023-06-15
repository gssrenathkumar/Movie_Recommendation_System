import os
from box.exceptions import BoxValueError
import yaml
from Movie_Recommendation_System.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import pandas as pd

@ensure_annotations  # This ensure_annotations is to make the input for the given data_type only else it raise error
def read_yaml(path_to_yaml:Path) -> ConfigBox:  # ConfigBox is use to make it like dictionary to access element with dot(.)
    """reads yaml file and returns the data from the file

    Args:
        path_to_yaml (str): path like input

    Raises:
          ValueError: if yaml file is empty
          e: empty file

    Returns:
          Configure: ConfigureBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool,optional): ignore if multiple dirs is to be created.Defalts to False.

    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path(Path): path of the file

    Returns:
        str:size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb}KB"

