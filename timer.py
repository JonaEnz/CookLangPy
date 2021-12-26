

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
        return "(Timer {1}: {0} seconds".format(self.length, self.name) #TODO: Unit conversion

    def fileOut(self) -> str:
        return r"~" + self.name + r"{" + str(self.length) + r"%seconds}"