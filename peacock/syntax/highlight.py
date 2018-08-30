from .lexer import DataTypesLexer
from .styles import DarkLogsStyle
from pygments import highlight
from pygments.formatters import Terminal256Formatter

class DataHighlighter(object):

    formatter = Terminal256Formatter(style=DarkLogsStyle)
    lexer = DataTypesLexer()

    def __init__(self, **kwargs):
        pass

    def highlight_line(self,line):
         return highlight(line, self.lexer, self.formatter)
