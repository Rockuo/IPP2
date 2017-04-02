import argparse
import sys

from typing import Dict, List
import ExecuteRules
import ArgProcessor
import FormatParser
from Exceptions import CommandFormatException, RegexFormatException

try:
    ArgProcessor.test_args(list(sys.argv))
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-f", "-F", "--format", dest="format", help="určení formátovacího souboru", type=str)
    argParser.add_argument("-i", "-I", "--input", dest="input", help="určení vstupního souboru v kódování UTF-8",
                           type=str)
    argParser.add_argument("-o", "-O", "--output", dest="output", help="určení výstupního souboru", type=str)
    argParser.add_argument("--br", dest="br", action='store_true',
                           help="přidá element <br/> na konec každého řádku původního vstupního textu")
    argParser.set_defaults(br=False)
    args = argParser.parse_args()

    inputStr = ArgProcessor.process_input(args.input)
    outputFile = ""
    fp = None
    if args.output:
        outputFile = args.output
        try:
            fp = open(outputFile, 'w')
            fp.write("")
        except FileNotFoundError:
            exit(3)

    try:
        rules: List[Dict] = FormatParser.get_rules(ArgProcessor.process_format(args.format))
        output: str = ExecuteRules.execute_rules(inputStr, rules, args.br)

        if outputFile:
            fp.write(output)
            fp.close()
        else:
            print(output, end='')
    except (RegexFormatException, CommandFormatException) as e:
        exit(4)
except FileNotFoundError:
    exit(2)
sys.exit(0)
