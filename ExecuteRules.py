from typing import Dict, List
import re


def execute_rules(input_s: str, regex_rules: List[Dict], use_br: bool) -> str:
    output: str = ""
    index_rules: List[Dict] = [None] * (len(input_s) + 1)
    ends = [[]] * (len(input_s) + 1)
    for i in range(0, len(input_s)+1):
        index_rules[i] = {'start': "", 'end': []}
        ends[i] = [""] * (len(input_s) + 1)

    for rule in regex_rules:
        for i_pair in [{'start': r.start(0), 'end': r.end(0)} for r in re.finditer(rule['regex'], input_s, flags=re.MULTILINE)]:
            if i_pair['start'] != i_pair['end']:
                index_rules[i_pair['start']]['start'] += rule['commands'].get_start()
                index_rules[i_pair['end']]['end'].append(rule['commands'].get_end())
    current_index: int = 0
    for char in input_s:
        for end in reversed(index_rules[current_index]['end']):
            output += end
        output += index_rules[current_index]['start']
        if use_br and char == '\n':
            output += '<br />'
        output += char
        current_index += 1
    for end in reversed(index_rules[current_index]['end']):
        output += end
    output += index_rules[current_index]['start']

    return output
