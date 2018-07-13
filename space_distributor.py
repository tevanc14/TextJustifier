import settings


class SpaceDistributor:
    def __init__(self, line):
        self.line = line

        self.line_width = settings.LINE_WIDTH
        self.space = settings.SPACE

        self.number_of_spaces_to_add = self.line_width - len(self.line)
        self.last_space_index = self.find_rightmost_space(self.line)

    def distribute_spaces(self):
        while self.number_of_spaces_to_add > 0:
            self.insert_space()
            self.number_of_spaces_to_add -= len(self.space)
        return self.line

    def insert_space(self):
        self.insert_space_at_index()
        sub_line = self.line[:self.last_space_index]
        self.last_space_index = self.find_rightmost_space(sub_line)

    def find_rightmost_space(self, string):
        string_rightmost_space = string.rfind(self.space)
        line_rightmost_space = self.line.rfind(self.space)
        if string_rightmost_space > 0:
            return string_rightmost_space
        elif line_rightmost_space > 0:
            return line_rightmost_space
        else:
            return len(self.line)

    def insert_space_at_index(self):
        pre_index = self.line[:self.last_space_index]
        post_index = self.line[self.last_space_index:]
        '''
        In some cases, the remainder of spaces must be added if the length of
        the space property is more than one
        
        e.g.:
        line length:  19
        line width:   20
        space length:  2
        
        Only one space can be added as adding the space length would make the line
        length greater than the line width
        '''
        if (len(self.space) + len(self.line)) > self.line_width:
            self.space = ' ' * (self.line_width - len(self.line))

        self.line = pre_index + self.space + post_index