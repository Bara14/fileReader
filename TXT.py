from Interface import InformalParserInterface
class TXTReader(InformalParserInterface):
    def load_data_source(self, file_name):
        with open(file_name) as txtfile:
            text = txtfile.read()
            print(text)

