import re


def remove_empty_lines(code: str) -> str:
    return '\n'.join([line for line in code.split('\n') if line.strip()])


def remove_single_line_comments(code: str) -> str:
    lines = [line.split('//')[0] for line in code.split('\n')]
    lines = [line for line in lines if line.strip()]
    return '\n'.join(lines)


def remove_multi_line_comments(code: str) -> str:
    return re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)


def remove_comments(code: str) -> str:
    code = remove_single_line_comments(code)
    code = remove_multi_line_comments(code)
    return code


def parse_package(code: str) -> str or None:
    code = remove_comments(code)
    code = remove_empty_lines(code)
    first_line = code.split('\n')[0]
    if not first_line.startswith('package'):
        return None
    first_line = first_line.split(';')[0]
    package = first_line.replace('package', '').strip()
    return package
