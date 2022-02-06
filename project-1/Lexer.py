import re


class Lexer:
    def __init__(self) -> None:
        self.t_types = {
            "IDENTIFIER": "([a-z]|[A-Z]|)([a-z]|[A-Z]|[0-9])",
            "NUMBER": "[0-9]+",
            "SYMBOL": "\+ | \- | \* | / | \( | \)",
        }

    # check which token type current buffer is
    def getTokenType(self, buffer):
        token_type = ""
        for key, val in self.t_types:
            match = re.match(val, buffer)
            if match:
                return key
        return "INVALID TOKEN"
