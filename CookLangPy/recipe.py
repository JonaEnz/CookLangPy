import re
from typing import List
from CookLangPy.ingredient import Ingredient

from CookLangPy.cookware import Cookware
from CookLangPy.step import Step

metadataReg = re.compile(r">> (.+): (.*)")
class Recipe():
    def __init__(self) -> None:
        self.__steps : List[Step] = []
        self.__metadata : dict = {}

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

    def get_metadata(self, key:str) -> dict:
        return self.__metadata[key] if key in self.__metadata else None

    def set_metadata(self, key:str, value:str) -> None:
        self.__metadata[key] = value

    @property
    def source(self) -> str:
        return self.get_metadata("source")
    
    @source.setter
    def source(self, source:str) -> None:
        self.set_metadata("source", source)
    
    @property
    def servings(self) -> int:
        return self.get_metadata("servings") if self.get_metadata("servings") else 1
    
    @servings.setter
    def servings(self, servings:int) -> None:
        self.set_metadata("servings", servings)

    def parse(input:str) -> 'Recipe':
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

    def from_file(filename:str) -> None:
        with open(filename, "r") as f:
            return Recipe.parse(f.read())
    
    def to_file(self, filename:str) -> None:
        with open(filename, "w") as f:
            f.write(self.fileOut())

    def __str__(self) -> str:
        return "\n".join(map((lambda x: str(x)), self.__steps))

    def fileOut(self) -> str:
        metadata = "".join(map(lambda x: ">> {0}: {1}\n".format(x[0], x[1]), self.__metadata.items()))
        return metadata + "\n".join(map((lambda x: x.fileOut()), self.__steps))