import sys

from typing import List, Dict

from Elements.Constants import CommandType, RegexOptions
from Elements.Containers import Commands, Command
from Exceptions import RegexFormatException, CommandFormatException


def get_rules(format_str: str) -> List[Dict]:
    # if not format_str:
    #     return []
    check_format(format_str)
    lines = format_str.split("\n")
    rules: List[Dict] = []
    for line in lines:
        if not ''.join(line.split()):
            continue

        if "\t" not in line:
            raise RegexFormatException('Unexpected character')
        [regex_s, command_s] = line.split("\t", 1)
        regex = translate_regex(regex_s)
        commands: list = parse_commands(''.join(command_s.split()).split(','))
        rules.append({'regex': regex, 'commands': commands})
    return rules


def check_format(format_str: str):
    last_operator_type = ""
    escaped = False
    in_brackets = 0
    for c in format_str:
        if escaped:
            escaped = False
        elif c == '%':
            escaped = True
        elif c == '(':
            in_brackets += 1
        elif c == ')':
            if in_brackets != 0:
                in_brackets -= 1
            else:
                raise RegexFormatException('Unexpected character')

        if c in RegexOptions.ACTIONS:
            if last_operator_type:
                if (last_operator_type in RegexOptions.NEGATION) or (c in RegexOptions.ITERATIONS) or (
                                last_operator_type in RegexOptions.CONCATENATIONS and c in RegexOptions.CONCATENATIONS):
                    raise RegexFormatException('Unexpected character')
                last_operator_type = c
            else:
                last_operator_type = c
        else:
            last_operator_type = ""


def parse_commands(command_l: List[str]) -> Commands:
    commands: Commands = Commands()
    for command in command_l:
        if command in CommandType.CLASSIC_TYPES:
            commands.push(Command(command))
        elif ':' in command:
            [c_type, c_val] = command.split(':')
            if c_type in CommandType.COLOR:
                try:
                    int_val = int(c_val, 16)
                    if int_val < 0 or int_val > int('FFFFFF', 16):
                        raise ValueError
                    commands.push(Command(c_type, c_val))
                except ValueError:
                    sys.exit(4)
            elif c_type in CommandType.SIZE:
                try:
                    int_val = int(c_val, 16)
                    if int_val < 1 or int_val > 7:
                        raise ValueError
                    commands.push(Command(c_type, c_val))
                except ValueError:
                    sys.exit(4)
            else:
                raise CommandFormatException('Command ' + command + ' does not exist.')
        else:
            raise CommandFormatException('Command ' + command + ' does not exist.')
    return commands


def translate_regex(input_r: str):
    output_r = ""
    is_not_escaped = True
    is_negation = False
    for char in input_r:
        if is_not_escaped:
            if char == '%':
                is_not_escaped = False
            elif char == '!':
                is_negation = True
            elif ord(char) > 31:
                if char == '.':
                    continue
                out_c = char
                if out_c == '\\':
                    out_c = '\\\\'
                if is_negation:
                    is_negation = False
                    out_c = "[^" + out_c + "]"
                output_r += out_c
            else:
                raise RegexFormatException('Unexpected character')
        else:
            is_not_escaped = True
            if char in RegexOptions.SPECIAL:
                if char == '!':
                    output_r += '!'
                else:
                    output_r += '\\' + char
            elif char == '%':
                output_r += '%'
            elif char in RegexOptions.ACCEPTED_ESCAPED:
                output_r += RegexOptions.ESCAPE_MAP[char]
            else:
                raise RegexFormatException('Unexpected character')

    return output_r
