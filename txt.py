from Interface import InformalParserInterface
class TxtReader(InformalParserInterface):
    def load_data_source(self, file_name):
        with open(file_name) as txtfile:
            text = txtfile.read()
            print(text)

