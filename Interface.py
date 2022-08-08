from abc import ABC, abstractmethod


class InformalParserInterface(ABC):
    @abstractmethod
    def load_data_source(self, file_name: str) -> str:
        pass

    def print_text(self, full_file_name: str) -> dict:
        pass