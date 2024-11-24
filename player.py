from dataclasses import dataclass

@dataclass(frozen=True)
class Player:
    acc: str
    char: str

    def __str__(self):
        return f"{self.acc}-{self.char}"