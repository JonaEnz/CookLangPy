

from unitconversion import largestUnitGreaterOne, unitConversion


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

    def __str__(self) -> str:
        unit = largestUnitGreaterOne(["SECOND","MINUTE", "HOUR"], "SECOND", float(self.length))
        val = unitConversion("SECOND", unit, float(self.length))
        return "(Timer {0}: {1} {2}".format(self.name, val, unit)

    def fileOut(self) -> str:
        return r"~" + self.name + r"{" + str(self.length) + r"%seconds}"