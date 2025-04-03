import re

regex = r"(<(.*?)>)"

def get_enclosed_strings(source_text: str) -> list[str] | None:
    result = []
    matches = re.finditer(regex, source_text, re.MULTILINE)
    for match in matches:
        result.append(match.group(2))
    return result