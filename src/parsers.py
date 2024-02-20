import re


def remove_singe_line_comments(code: str) -> str:
    lines = [line.split('//')[0] for line in code.split('\n')]
    lines = [line for line in lines if line.strip()]
    return '\n'.join(lines)


def remove_multi_line_comments(code: str) -> str:
    return re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
