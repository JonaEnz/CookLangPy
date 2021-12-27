import re
from typing import List

from CookLangPy.unitconversion import largestUnitGreaterOne, unitConversion

timerReg = re.compile(r"~(.*){(\d+)%(hour|minute|second)s?}")

class Timer():
    """
    A timer is a string of the form "~name{length%unit}".
    length: the length of the timer in seconds.
    name: the name of the timer (Optional).
    """
    def __init__(self) -> None:
        """
        Initialize the timer.
        """
        self.length : int = 0
        self.name : str = ""

    def parse(input:str) -> List['Timer']:
        timers = []
        for match in timerReg.findall(input):
            t = Timer()
            t.length = unitConversion(match[2], "SECOND", float(match[1]))
            t.name = match[0]
            timers.append(t)
        return timers

    def __str__(self) -> str:
        unit = largestUnitGreaterOne(["SECOND","MINUTE", "HOUR"], "SECOND", float(self.length))
        val = unitConversion("SECOND", unit, float(self.length))
        if val > 1.0:
            unit += "S"
        return "(Timer {0}: {1} {2}".format(self.name, val, unit.lower())

    def fileOut(self) -> str:
        unit = largestUnitGreaterOne(["SECOND","MINUTE", "HOUR"], "SECOND", float(self.length))
        val = unitConversion("SECOND", unit, float(self.length))
        if val > 1.0:
            unit += "S"
        return r"~" + self.name + r"{" + str(val) + r"%" + unit.lower() + r"}"