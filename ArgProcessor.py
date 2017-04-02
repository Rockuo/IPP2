from typing import List


def process_format(format_file):
    if format_file:
        try:
            fp = open(format_file)
            if fp.readable():
                format_cont = fp.read()
            else:
                format_cont = ""
            fp.close()
            return format_cont
        except FileNotFoundError:
            return ""
    else:
        return ""


def process_input(input_file):
    if input_file:
        fp = open(input_file)
        if fp.readable():
            input_cont = fp.read()
        else:
            input_cont = ""
        fp.close()
        return input_cont
    else:
        return input()


def test_args(args: List[str]):
    try:
        valid_args = ["-f", "-F", "--format",
                      "-i", "-I", "--input",
                      "-o", "-O", "--output",
                      "--br"
                      ]
        used = []
        groups = [
            ["-f", "-F", "--format"],
            ["-i", "-I", "--input"],
            ["-o", "-O", "--output"],
            ["--br"]
        ]
        args.pop(0)

        for arg in args:
            name = "--br"
            value = "none"
            if arg != "--br":
                splited = arg.split('=')
                if len(splited) != 2:
                    exit(1)
                [name, value] = splited

            if name not in valid_args or len(value) == 0 or name in used:
                exit(1)

            for group in groups:
                if name in group:
                    used += group
                    break


    except:
        exit(1)