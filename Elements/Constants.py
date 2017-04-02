class CommandType:
    BOLD = 'bold'
    ITALIC = 'italic'
    UNDERLINE = 'underline'
    TELETYPE = 'teletype'
    SIZE = 'size'
    COLOR = 'color'
    CLASSIC_TYPES = [BOLD, ITALIC, UNDERLINE, TELETYPE]
    VALUE_TYPES = [SIZE, COLOR]

CommandTemplate = {
    'bold': {'start': "<b", 'end': "</b>"},
    'italic': {'start': "<i", 'end': "</i>"},
    'underline': {'start': "<u", 'end': "</u>"},
    'teletype': {'start': "<tt", 'end': "</tt>"},
    'size': {'start': "<font size=", 'end': "</font>"},
    'color': {'start': "<font color=#", 'end': "</font>"},
}

class RegexOptions:
    BRACKETS = '()'
    CONCATENATIONS = '.|'
    ITERATIONS = '*+'
    NEGATION = '!'
    ACTIONS = CONCATENATIONS+ITERATIONS+NEGATION
    SPECIAL = BRACKETS + ACTIONS
    ACCEPTED_ESCAPED = 'sadlLwWtn'

    ESCAPE_MAP = {
        's': '\\s',
        'a': '(.|\\s|\\n)',
        'd': '\\d',
        'l': '[a-z]',
        'L': '[A-Z]',
        'w': '([a-z]|[A-Z])',
        'W': '([a-z]|[A-Z]|\d)',
        't': '\\t',
        'n': '\\n',
    }
