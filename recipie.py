import re
from typing import List
from ingredient import Ingredient

from cookware import Cookware
from step import Step

metadataReg = re.compile(r">> (.+): (.*)")
class Recipe():
    def __init__(self) -> None:
        self.__steps : List[Step] = []
        self.metadata : dict = {}

    @property
    def ingredients(self) -> List[Ingredient]:
        ingredients = {}
        for step in self.__steps:
            for ingredient in step.ingredients:
                if ingredient.name not in ingredients:
                    ingredients[ingredient.name] = ingredient
                else:
                    ingredients[ingredient.name].amount += ingredient.amount #TODO: convert units
        return list(ingredients.values())

    @property
    def cookware(self) -> List[Cookware]:
        cw = {}
        for step in self.__steps:
            for cookware in step.cookware:
                if cookware.name not in cw:
                    cw[cookware.name] = cookware
        return list(cw.values())

    def parse(input:str) -> None:
        r = Recipe()
        r.__steps = []
        list(map((lambda x: Step.parse(x)), input.split("\n")))
        for step in input.split("\n"):
            if step.startswith(">>"):
                match = metadataReg.match(step)
                r.metadata[match.group(1)] = match.group(2)
            else:
                r.__steps.append(Step.parse(step))
        return r

    def __str__(self) -> str:
        return "\n".join(map((lambda x: str(x)), self.__steps))

    def fileOut(self) -> str:
        metadata = "".join(map(lambda x: ">> {0}: {1}\n".format(x[0], x[1]), self.metadata.items()))
        return metadata + "\n".join(map((lambda x: x.fileOut()), self.__steps))