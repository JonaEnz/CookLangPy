import re
from typing import List

from CookLangPy.ingredient import Ingredient
from CookLangPy.cookware import Cookware
from CookLangPy.timer import Timer

replaceSpecialReg = re.compile(r"(([#@])(?:[^#@\n{}]+{\S*}|\w+))")
stepOutReg = re.compile(r"(\$[CIT])(\d+)")
blockCommentReg = re.compile(r".*\[-(.*)-\]")
timerReg = re.compile(r"(~.*{\d+(?:\.\d+)?%(?:hour|minute|second)s?})")

class Step():
    def __init__(self) -> None:
        self.ingredients : List[Ingredient] = []
        self.cookware : List[Cookware] = []
        self.timers : List[Timer] = []
        self.__text : str = ""
        self.comment : str = ""

    def parse(text:str) -> 'Step':
        s = Step()
        if "--" in text:
            split = text.split("--")
            text = split[0]
            s.comment = "".join(split[1:])
        m = blockCommentReg.match(text)
        if bool(m):
            s.comment = m.group(1)
        s.setText(text)
        return s

    def setText(self, text:str):
        for match in replaceSpecialReg.findall(text):
            if match[1] == "#":
                self.cookware.append(Cookware.parse(match[0])[0])
                text = replaceSpecialReg.sub(r"$C{0}".format(len(self.cookware)-1), text, 1)
            elif match[1] == "@":
                self.ingredients.append(Ingredient.parse(match[0])[0])
                text = replaceSpecialReg.sub(r"$I{0}".format(len(self.ingredients)-1), text, 1)
        
        for match in timerReg.findall(text):
            self.timers.append(Timer.parse(match)[0])
            text = timerReg.sub(r"$T{0}".format(len(self.timers)-1), text, 1)

        self.__text = text
    
    def __str__(self) -> str:
        out = self.__text
        for match in stepOutReg.findall(self.__text):
            if match[0] == "$C":
                out= stepOutReg.sub(str(self.cookware[int(match[1])]), out, 1)
            elif match[0] == "$I":
                out = stepOutReg.sub(str(self.ingredients[int(match[1])]), out, 1)
            elif match[0] == "$T":
                out = stepOutReg.sub(str(self.timers[int(match[1])]), out, 1)
        return out

    def fileOut(self) -> str:
        out = self.__text
        for match in stepOutReg.findall(self.__text):
            if match[0] == "$C":
                out= stepOutReg.sub((self.cookware[int(match[1])].fileOut()), out, 1)
            elif match[0] == "$I":
                out = stepOutReg.sub((self.ingredients[int(match[1])].fileOut()), out, 1)
            elif match[0] == "$T":
                out = stepOutReg.sub((self.timers[int(match[1])].fileOut()), out, 1)
        return out