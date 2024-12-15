import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input
        
    Return:
    ConfigBox: parsed config
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(directory_paths: list, verbose = True):
    """ create list of directories
    
    Args:
        directory_paths (list): list of paths like input"""
    
    for path in directory_paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """ger size in KB
    
    Args:
        path (Path) : path of the file
    Returns:
        str : size in KB"""
    
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"