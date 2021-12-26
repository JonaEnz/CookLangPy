import re
from typing import List


cookwareReg = re.compile(r"#([\w ]*){}|#(\w+)")

class Cookware():
    def __init__(self, name:str) -> None:
        self.name : str = name
    def parse(recipe:str) -> List['Cookware']:
        cookware = []
        for match in cookwareReg.findall(recipe):
            cookware.append(Cookware(match[0]) if match[0] != "" else Cookware(match[1]))
        return cookware

    def __str__(self):
        return self.name
    
    def fileOut(self):
        if " " in self.name:
            return "#" + self.name + "{}"
        else:
            return "#" + self.name