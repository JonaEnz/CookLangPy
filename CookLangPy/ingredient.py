import re
from typing import List

recpReg = re.compile(r"@(?:([\w ]+){([\w \.]*)(?:%(\S+))?})|@(\w+)")

class Ingredient():
    def __init__(self, name:str, amount:str, unit:str):
        self.name : str = name
        self.amount : float = float(amount.replace(",", "."))
        self.unit : str = unit
    def parse(input:str) -> List['Ingredient']:
        ingredients = []
        for match in recpReg.findall(input):
            if match[3] != "":
                ingredients.append(Ingredient(match[3], "0", None))
            elif match[1] != "" and match[2] != "":
                ingredients.append(Ingredient(match[0], match[1], match[2]))
            elif match[1] != "":
                ingredients.append(Ingredient(match[0], match[1], ""))
            elif match[0] != "":
                ingredients.append(Ingredient(match[0], "0", ""))
        return ingredients

    def __str__(self):
        if self.amount != 0 and self.unit != "":
            return "{0} ({1} {2})".format(self.name, self.amount, self.unit)
        elif self.amount != 0:
            return "{0} ({1})".format(self.name, self.amount)
        else:
            return self.name
    
    def fileOut(self):
        if self.amount != 0 and self.unit != "":
            return "@{0}".format(self.name)+"{"+ str(self.amount) +"%"+self.unit+"}"
        elif self.amount != 0:
            return "@{0}".format(self.name) +"{" + str(self.amount) +"}"
        else:
            if " " in self.name:
                return "@" + self.name + "{}"
            else:
                return "@" + self.name