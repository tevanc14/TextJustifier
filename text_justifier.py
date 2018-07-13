import os

from line_splitter import LineSplitter
from space_distributor import SpaceDistributor


class TextJustifier:
    def __init__(self):
        self.input_text = self.read_input()

        self.output_text = []

    def read_input(self):
        with open('input.txt', 'r') as input_file:
            return input_file.read()

    def justify_text(self):
        splitter = LineSplitter(self.input_text)
        split_lines = splitter.text_to_lines()

        # Go up to the last line and append separately as the last
        # line does not need extra spaces
        for line in split_lines[:-1]:
            space_distributor = SpaceDistributor(line)
            self.output_text.append(space_distributor.distribute_spaces())
        self.output_text.append(split_lines[-1])
        self.write_output()

    def write_output(self):
        output_with_newlines = os.linesep.join(self.output_text)

        with open('output.txt', 'w') as output_file:
            output_file.write(output_with_newlines)


if __name__ == "__main__":
    justifier = TextJustifier()
    justifier.justify_text()
