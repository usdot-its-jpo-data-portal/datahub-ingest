from abc import ABC, abstractmethod
from DHDataset import DHDataset


class FormatterInterface(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_data_objects(self, datasets, dataset_name=None) -> [DHDataset]:
        raise NotImplementedError
