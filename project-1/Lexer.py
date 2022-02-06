class Lexer:
    def __init__(self) -> None:
        self.t_types = {
            "IDENTIFIER" : "([a-z]|[A-Z]|)([a-z]|[A-Z]|[0-9])",
            "NUMBER" : "[0-9]+",
            "SYMBOL" : "\+ | \- | \* | / | \( | \)",    
        }