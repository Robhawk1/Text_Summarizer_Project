from dataclasses import dataclass
from pathlib import Path

#Creating an entity in which we have the return type of the data ingestion configuration
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path