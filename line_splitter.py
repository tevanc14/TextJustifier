import settings


class LineSplitter:
    def __init__(self, input_text):
        self.input_text = input_text

        self.line_width = settings.LINE_WIDTH
        self.space = settings.SPACE

        self.current_word = ''
        self.current_line = ''
        self.words = []
        self.lines = []

    def text_to_lines(self):
        self.words = self.input_text.split()
        for word in self.words:
            self.current_word = word
            self.handle_word()
        self.add_line()

        return self.lines

    def handle_word(self):
        self.check_for_first_word_overflow()
        if self.should_add_another_word():
            self.add_word()
        else:
            self.add_line()
            self.handle_word()

    def check_for_first_word_overflow(self):
        if not self.current_line and len(self.current_word) > self.line_width:
            truncation_index = self.line_width - len(self.current_word)
            pre_truncation_index_word = self.current_word[:truncation_index]
            post_truncation_index_word = self.current_word[truncation_index:]

            self.current_word = pre_truncation_index_word
            self.add_word()
            self.add_line()
            self.current_word = post_truncation_index_word

    def should_add_another_word(self):
        proposed_length = len(self.current_line) + len(
            self.current_word) + len(self.space)

        return proposed_length < self.line_width

    def add_line(self):
        self.lines.append(self.current_line)
        self.clear_line()

    def clear_line(self):
        self.current_line = ''

    def add_word(self):
        if not self.current_line:
            self.current_line = self.current_line + self.current_word
        else:
            self.current_line = self.current_line + self.space + self.current_word