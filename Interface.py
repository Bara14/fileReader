class InformalParserInterface:
    def load_data_source(self, file_name: str) -> str:
        pass

    def extract_text(self, full_file_name: str) -> dict:
        pass