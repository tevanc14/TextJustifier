import settings


class LineSplitter:
    """Split given text into lines under a certain line width"""

    def __init__(self, input_text):
        self.input_text = input_text

        self.line_width = settings.LINE_WIDTH
        self.space = settings.SPACE

        self.current_word = ''
        self.current_line = ''
        self.words = []
        self.lines = []

    def text_to_lines(self):
        """Iterate through words to separate into lines"""
        self.words = self.input_text.split()
        for word in self.words:
            self.current_word = word
            self.handle_word()
        self.add_line()

        return self.lines

    def handle_word(self):
        """Decide what should be done with the current word on the current line"""
        self.check_for_first_word_overflow()
        if self.should_add_another_word():
            self.add_word()
        else:
            self.add_line()
            self.handle_word()

    def check_for_first_word_overflow(self):
        """If the first word of a line is longer than the line width, it must be treated differently"""
        if not self.current_line and len(self.current_word) > self.line_width:
            truncation_index = self.line_width - len(self.current_word)
            pre_truncation_index_word = self.current_word[:truncation_index]
            post_truncation_index_word = self.current_word[truncation_index:]

            self.current_word = pre_truncation_index_word
            self.add_word()
            self.add_line()
            self.current_word = post_truncation_index_word

    def should_add_another_word(self):
        """Check if adding the word and the space property would be longer than the line width"""
        proposed_length = len(self.current_line) + len(
            self.current_word) + len(self.space)

        return proposed_length < self.line_width

    def add_line(self):
        """Add a finished line and clear the current line"""
        self.lines.append(self.current_line)
        self.clear_line()

    def clear_line(self):
        """Clear the current line to allow for a new line to be processed"""
        self.current_line = ''

    def add_word(self):
        """Add a word to the current line with a space unless it is the first word"""
        if not self.current_line:
            self.current_line = self.current_line + self.current_word
        else:
            self.current_line = self.current_line + self.space + self.current_word