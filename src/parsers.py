import re


def remove_empty_lines(code: str) -> str:
    return '\n'.join([line for line in code.split('\n') if line.strip()])


def remove_singe_line_comments(code: str) -> str:
    lines = [line.split('//')[0] for line in code.split('\n')]
    lines = [line for line in lines if line.strip()]
    return '\n'.join(lines)


def remove_multi_line_comments(code: str) -> str:
    return re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)


def remove_comments(code: str) -> str:
    code = remove_singe_line_comments(code)
    code = remove_multi_line_comments(code)
    return code
