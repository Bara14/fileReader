from abc import ABC, abstractmethod



class BaseParser(ABC):
    @abstractmethod
    def load_data_source(self, file_type, file_path) -> str:
        pass
