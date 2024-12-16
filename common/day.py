class Day:
    def __init__(self, input_path):
        self.input_path = input_path

    def read_np(self):
        np.load(self.input_path)