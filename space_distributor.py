import settings


class SpaceDistributor:
    """Distribute spaces in a pretty fashion to extend the length of the line"""

    def __init__(self, line):
        self.line = line

        self.line_width = settings.LINE_WIDTH
        self.space = settings.SPACE

        self.number_of_spaces_to_add = self.line_width - len(self.line)
        self.last_space_index = self.find_rightmost_space(self.line)

    def distribute_spaces(self):
        """Place spaces evenly throughout a line from right to left

        :returns: The line with spaces distributed within

        """
        while self.number_of_spaces_to_add > 0:
            self.insert_space()
            self.number_of_spaces_to_add -= len(self.space)
        return self.line

    def insert_space(self):
        """Find an index and insert the space property at that index"""
        self.insert_space_at_index()
        sub_line = self.line[:self.last_space_index]
        self.last_space_index = self.find_rightmost_space(sub_line)

    def find_rightmost_space(self, string):
        """Find the first available space starting from the right side

        :param string: The string to find the rightmost space of
        :returns: The index of the rightmost space

        """
        string_rightmost_space = string.rfind(self.space)
        line_rightmost_space = self.line.rfind(self.space)
        if string_rightmost_space > 0:
            return string_rightmost_space
        # If the spaces have been run through once, start again at the end of the string
        elif line_rightmost_space > 0:
            return line_rightmost_space
        # The line has no spaces, so just append them to the end
        else:
            return len(self.line)

    def insert_space_at_index(self):
        """Insert the space property at a set index in the line"""
        pre_index = self.line[:self.last_space_index]
        post_index = self.line[self.last_space_index:]
        """
        In some cases, the remainder of spaces must be added if the length of
        the space property is more than one
        
        e.g.:
        line length:  19
        line width:   20
        space length:  2
        
        Only one space can be added as adding the space length would make the line
        length greater than the line width
        """
        if (len(self.space) + len(self.line)) > self.line_width:
            self.space = ' ' * (self.line_width - len(self.line))

        self.line = pre_index + self.space + post_index